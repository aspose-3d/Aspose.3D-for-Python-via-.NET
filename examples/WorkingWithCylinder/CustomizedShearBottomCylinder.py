from aspose.threed import Scene
from aspose.threed.entities import Cylinder
from aspose.threed.utilities import Vector2, Vector3
from examples.Common import *

def Run():
    # ExStart:1
    # Create a scene
    scene = Scene()
    # Create cylinder 1
    cylinder1 = Cylinder(2, 2, 10, 20, 1, False)
    # Customized shear bottom for cylinder 1
    cylinder1.shear_bottom = Vector2(0, 0.83)# shear 47.5deg in xy plane(z-axis)
    # Add cylinder 1 to the scene
    scene.root_node.create_child_node(cylinder1).transform.translation = Vector3(10, 0, 0)
    # Create cylinder 2
    cylinder2 = Cylinder(2, 2, 10, 20, 1, False)
    # Add cylinder to without a ShearBottom to the scene
    scene.root_node.create_child_node(cylinder2)
    # Save scene
    scene.save(get_output_path("CustomizedShearBottomCylinder.obj"))

    # ExEnd:1              
