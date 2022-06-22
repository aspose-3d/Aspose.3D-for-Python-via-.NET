from aspose.threed import Scene
from aspose.threed.entities import Plane
from aspose.threed.utilities import Vector3
from examples.Common import *

def Run():
    # ExStart:ChangePlaneOrientation
    # Initialize scene object
    scene = Scene()
    # Set Vector
    plane = Plane()
    plane.up = Vector3(1, 1, 3)
    scene.root_node.create_child_node(plane)
    #This will generate a plane that has customized orientation
    scene.save(get_output_path( "ChangePlaneOrientation.obj"))
    # ExEnd:ChangePlaneOrientation
