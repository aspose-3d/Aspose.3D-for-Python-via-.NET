from aspose.threed import Scene
from aspose.threed.entities import Box, VertexElementType, MappingMode, ReferenceMode, VertexElementMaterial, SplitMeshPolicy, PolygonModifier
from examples.Common import *

def Run():
    # ExStart:SplitMeshbyMaterial

    # Create a mesh of box(A box is composed by 6 planes)
    box = (Box()).to_mesh()
    # Create a material element on this mesh
    mat = box.create_element(VertexElementType.MATERIAL, MappingMode.POLYGON, ReferenceMode.INDEX).cast(VertexElementMaterial)
    # And specify different material index for each plane
    mat.indices.add_range([0, 1, 2, 3, 4, 5])
    # Now split it into 6 sub meshes, we specified 6 different materials on each plane, each plane will become a sub mesh.
    # We used the CloneData policy, each plane will has the same control point information or control point-based vertex element information.
    planes = PolygonModifier.split_mesh(box, SplitMeshPolicy.CLONE_DATA)

    mat.indices.clear()
    mat.indices.add_range([0, 0, 0, 1, 1, 1])
    # Now split it into 2 sub meshes, first mesh will contains 0/1/2 planes, and second mesh will contains the 3/4/5th planes.
    # We used the CompactData policy, each plane will has its own control point information or control point-based vertex element information.
    planes = PolygonModifier.split_mesh(box, SplitMeshPolicy.COMPACT_DATA)

    # ExEnd:SplitMeshbyMaterial
    print("\nSpliting a mesh by specifying the material successfully.")
