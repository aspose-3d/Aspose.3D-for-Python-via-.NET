from aspose.threed import Scene, Node
from examples.Common import *

def Run():
    # ExStart:CreateCubeScene           
    # Initialize scene object
    scene = Scene()
    
    # Initialize Node class object
    cubeNode = Node("cube")

    # Call Common class create mesh using polygon builder method to set mesh instance 
    mesh = CreateCubeMesh()

    # Point node to the Mesh geometry
    cubeNode.entity = mesh
    
    # Add Node to a scene
    scene.root_node.child_nodes.append(cubeNode)
    
    # The path to the documents directory.
    output = get_output_path("CubeScene.fbx")

    # Save 3D scene in the supported file formats
    scene.save(output)
    # ExEnd:CreateCubeScene

    print("\nCube Scene created successfully.\nFile saved at " + output)

