from aspose.threed import Scene
from aspose.threed.profiles import RectangleShape
from aspose.threed.entities import LinearExtrusion
from aspose.threed.utilities import Vector3
from examples.Common import *

def Run():
    # ExStart:DirectionInLinearExtrusion
    # Initialize the base profile to be extruded
    profile = RectangleShape()
    profile.rounding_radius = 0.3
    # Create a scene 
    scene = Scene()
    # Create left node
    left = scene.root_node.create_child_node()
    # Create right node
    right = scene.root_node.create_child_node()
    left.transform.translation = Vector3(8, 0, 0)

    # Direction property defines the direction of the extrusion.
    # Perform linear extrusion on left node using twist and slices property
    extrusion = LinearExtrusion(profile, 10)
    extrusion.twist = 360
    extrusion.slices = 100
    left.create_child_node(extrusion)
    # Perform linear extrusion on right node using twist, slices, and direction property
    extrusion = LinearExtrusion(profile, 10)
    extrusion.twist = 360
    extrusion.slices = 100
    extrusion.direction = Vector3(0.3, 0.2, 1)
    right.create_child_node(extrusion)

    # Save 3D scene
    scene.save(get_output_path("DirectionInLinearExtrusion.obj"))
    # ExEnd:DirectionInLinearExtrusion            
