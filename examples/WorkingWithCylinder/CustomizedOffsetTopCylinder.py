from aspose.threed import Scene
from aspose.threed.entities import Cylinder
from aspose.threed.utilities import Vector3
from examples.Common import *

def Run():
    # ExStart:1
    # Create a scene
    scene = Scene()
    # Initialize cylinder
    cylinder1 = Cylinder(2, 2, 10, 20, 1, False)
    # Set OffsetTop
    cylinder1.offset_top = Vector3(5, 3, 0)
    # Create ChildNode
    scene.root_node.create_child_node(cylinder1).transform.translation = Vector3(10, 0, 0)
    # Intialze second cylinder without customized OffsetTop
    cylinder2 = Cylinder(2, 2, 10, 20, 1, False)
    # Create ChildNode
    scene.root_node.create_child_node(cylinder2)
    # Save
    scene.save(get_output_path("CustomizedOffsetTopCylinder.obj"))
    # ExEnd:1              
