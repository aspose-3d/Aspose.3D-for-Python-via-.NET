from aspose.threed import Scene
from aspose.threed.entities import Cylinder
from aspose.threed.utilities import MathUtils, Vector3
from examples.Common import *

def Run():
    # ExStart:1
    # Create a Scene
    scene = Scene()
    # Create a cylinder
    fan = Cylinder(2, 2, 10, 20, 1, False)
    # Set GenerateGanCylinder to True
    fan.generate_fan_cylinder = True
    # Set ThetaLength
    fan.theta_length = MathUtils.to_radian(270)
    # Create ChildNode
    scene.root_node.create_child_node(fan).transform.translation = Vector3(10, 0, 0)
    # Create a cylinder without a fan
    nonfan = Cylinder(2, 2, 10, 20, 1, False)
    # Set GenerateGanCylinder to False
    nonfan.generate_fan_cylinder = False
    # Set ThetaLengeth 
    nonfan.theta_length = MathUtils.to_radian(270)
    # Create ChildNode
    scene.root_node.create_child_node(nonfan)
    # Save scene
    scene.save(get_output_path("CreateFanCylinder.obj"))
    # ExEnd:1              
