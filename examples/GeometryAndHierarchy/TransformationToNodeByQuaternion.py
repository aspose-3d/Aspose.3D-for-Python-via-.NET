from aspose.threed import Scene, Node
from aspose.threed.utilities import Quaternion, Vector3
from examples.Common import *
def Run():
    # ExStart:AddTransformationToNodeByQuaternion            
    # Initialize scene object
    scene = Scene()

    # Initialize Node class object
    cubeNode = Node("cube")

    # Call Common class create mesh using polygon builder method to set mesh instance 
    mesh = CreateCubeMesh()
   
    # Point node to the Mesh geometry
    cubeNode.entity = mesh
    # Set rotation
    cubeNode.transform.rotation = Quaternion.from_rotation(Vector3(0, 1, 0), Vector3(0.3, 0.5, 0.1))
    # Set translation
    cubeNode.transform.translation = Vector3(0, 0, 20)
    # Add cube to the scene
    scene.root_node.child_nodes.append(cubeNode)

    # The path to the documents directory.
    output = get_output_path("TransformationToNode.fbx")
   
    # Save 3D scene in the supported file formats
    scene.save(output)
    # ExEnd:AddTransformationToNodeByQuaternion
    print("\nTransformation added successfully to node.\nFile saved at " + output)

