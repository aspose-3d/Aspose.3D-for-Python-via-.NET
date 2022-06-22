from aspose.threed import Scene
from aspose.threed.entities import Camera
from aspose.threed.utilities import Vector3
from examples.Common import *

def Run():
    # ExStart:SetupTargetAndCamera
    # Initialize scene object
    scene = Scene()
    # Get a child node object
    cameraNode = scene.root_node.create_child_node("camera", Camera())
    # Set camera node translation
    cameraNode.transform.translation = Vector3(100, 20, 0)
    cameraNode.entity.cast(Camera).target = scene.root_node.create_child_node("target")
    output = get_output_path("camera-test.3ds")
    scene.save(output)
    # ExEnd:SetupTargetAndCamera
    print("\nThe target and camera has been setup successfully.\nFile saved at " + output)
