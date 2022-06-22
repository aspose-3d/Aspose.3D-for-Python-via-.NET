from aspose.threed import Scene, Node
from aspose.threed.entities import Cylinder
from examples.Common import *

def Run():
    # Initialize scene object
    scene = Scene()
    
    # Initialize Node class object
    cubeNode = Node("cylinder");

    # ExStart:ConvertCylinderPrimitivetoMesh
    # Initialize object by Cylinder class
    convertible = Cylinder()
    
    # Convert a Cylinder to Mesh
    mesh = convertible.to_mesh()
    # ExEnd:ConvertCylinderPrimitivetoMesh

    # Point node to the Mesh geometry
    cubeNode.entity = mesh

    # Add Node to a scene
    scene.root_node.child_nodes.append(cubeNode)

    # The path to the documents directory.
    output = get_output_path("CylinderToMeshScene.fbx")

    # Save 3D scene in the supported file formats
    scene.save(output)

    print("\n Converted the primitive Cylinder to a mesh successfully.\nFile saved at " + output)
