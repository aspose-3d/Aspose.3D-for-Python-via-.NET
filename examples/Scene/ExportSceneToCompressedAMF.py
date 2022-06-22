from aspose.threed import Scene
from aspose.threed.utilities import Vector3
from aspose.threed.entities import Box
from examples.Common import *

def Run():
    # ExStart:CompressedAMF
    # Load a scene
    scene = Scene()
    box = Box()
    tr = scene.root_node.create_child_node(box).transform
    tr.scale = Vector3(12, 12, 12)
    tr.translation = Vector3(10, 0, 0)
    tr = scene.root_node.create_child_node(box).transform
    # Scale transform
    tr.scale = Vector3(5, 5, 5)
    # Set Euler Angles
    tr.euler_angles = Vector3(50, 10, 0)
    scene.root_node.create_child_node()
    scene.root_node.create_child_node().create_child_node(box)
    scene.root_node.create_child_node().create_child_node(box)
    # Save compressed AMF file
    scene.save(get_output_path("Aspose.amf"))
    # ExEnd:CompressedAMF
