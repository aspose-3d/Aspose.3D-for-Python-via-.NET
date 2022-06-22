from aspose.threed import Scene
from aspose.threed.entities import Cylinder
from aspose.threed.utilities import Quaternion, Vector3
from examples.Common import *
import math

def Run():
    # ExStart:ConcatenateQuaternions     

    scene = Scene()

    q1 = Quaternion.from_euler_angle(math.pi * 0.5, 0, 0)
    q2 = Quaternion.from_angle_axis(-math.pi * 0.5, Vector3.X_AXIS)
    # Concatenate q1 and q2. q1 and q2 rotate alone x-axis with same angle but different direction,
    # So the concatenated result will be identity quaternion.
    q3 = q1.concat(q2)

    # Create 3 cylinders to represent each quaternion
    cylinder = scene.root_node.create_child_node("cylinder-q1", Cylinder(0.1, 1, 2))
    cylinder.transform.rotation = q1
    cylinder.transform.translation = Vector3(-5, 2, 0)

    cylinder = scene.root_node.create_child_node("cylinder-q2", Cylinder(0.1, 1, 2))
    cylinder.transform.rotation = q2
    cylinder.transform.translation = Vector3(0, 2, 0)

    cylinder = scene.root_node.create_child_node("cylinder-q3", Cylinder(0.1, 1, 2))
    cylinder.transform.rotation = q3
    cylinder.transform.translation = Vector3(5, 2, 0)
    output = get_output_path("test_out.fbx")
    # Save to file
    scene.save(output)
    # ExEnd:ConcatenateQuaternions

    print("\nQuaternions concatenated successfully.\nFile saved at " + output)

