from aspose.threed import Scene
from aspose.threed.utilities import Quaternion, Vector3
import math
from examples.Common import *

def Run():
    # ExStart:AddNodeHierarchy
    # Initialize scene object
    scene = Scene()

    # Get a child node object
    top = scene.root_node.create_child_node()
    # Each cube node has their own translation
    cube1 = top.create_child_node("cube1")
    # Call Common class create mesh using polygon builder method to set mesh instance 
    mesh = CreateCubeMesh()
    # Point node to the mesh
    cube1.entity = mesh
    # Set first cube translation
    cube1.transform.translation = Vector3(-10, 0, 0)
    cube2 = top.create_child_node("cube2")
    # Point node to the mesh
    cube2.entity = mesh
    # Set second cube translation
    cube2.transform.translation = Vector3(10, 0, 0)

    # The rotated top node will affect all child nodes
    top.transform.rotation = Quaternion.from_euler_angle(math.pi, 4, 0)
  
    # The path to the documents directory.
    output = get_output_path("NodeHierarchy.fbx")
    
    # Save 3D scene in the supported file formats
    scene.save(output)
    # ExEnd:AddNodeHierarchy
   
    print("\nNode hierarchy added successfully to document.\nFile saved at " + output)

