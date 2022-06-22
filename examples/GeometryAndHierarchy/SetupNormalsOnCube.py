from aspose.threed import Scene
from aspose.threed.entities import VertexElementType, MappingMode, ReferenceMode, VertexElementNormal
from examples.Common import *

def Run():
    # ExStart:SetupNormalsOnCube
    # Raw normal data
    normals = [
        Vector4(-0.577350258,-0.577350258, 0.577350258, 1.0),
        Vector4( 0.577350258,-0.577350258, 0.577350258, 1.0),
        Vector4( 0.577350258, 0.577350258, 0.577350258, 1.0),
        Vector4(-0.577350258, 0.577350258, 0.577350258, 1.0),
        Vector4(-0.577350258,-0.577350258,-0.577350258, 1.0),
        Vector4( 0.577350258,-0.577350258,-0.577350258, 1.0),
        Vector4( 0.577350258, 0.577350258,-0.577350258, 1.0),
        Vector4(-0.577350258, 0.577350258,-0.577350258, 1.0)
    ]

    # Call Common class create mesh using polygon builder method to set mesh instance 
    mesh = CreateCubeMesh()

    elementNormal = mesh.create_element(VertexElementType.NORMAL, MappingMode.CONTROL_POINT, ReferenceMode.DIRECT).cast(VertexElementNormal)
    # Copy the data to the vertex element
    elementNormal.data.add_range(normals)
    # ExEnd:SetupNormalsOnCube

    print("\nNormals has been setup successfully on cube.")
