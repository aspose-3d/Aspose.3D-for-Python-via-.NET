from aspose.threed import Scene
from aspose.threed.entities import Box, VertexElementType, PolygonModifier
from examples.Common import *

def Run():

    # ExStart:GenerateUV
    scene = Scene()
    #since all primitive entities in Aspose.3D will have builtin UV generation
    #here we manually remove it to assume we have a mesh without UV data
    mesh = (Box()).to_mesh()
    mesh.vertex_elements.remove(mesh.get_element(VertexElementType.UV))
    #then we can manually generate UV for it
    uv = PolygonModifier.generate_uv(mesh)
    #generated UV data is not associated with the mesh, we should manually do this
    mesh.add_element(uv)
    #put it to the scene
    node = scene.root_node.create_child_node(mesh)
    #then save it
    scene.save(get_output_path("Aspose.obj"))
    # ExEnd:GenerateUV
