from aspose.threed import Scene
from aspose.threed.profiles import RectangleShape
from aspose.threed.entities import LinearExtrusion
from aspose.threed.utilities import Vector3
from examples.Common import *

def Run():
    # ExStart:CenterInLinearExtrusion
    # Initialize the base profile to be extruded
    profile = RectangleShape()
    profile.rounding_radius = 0.3
    # Create a scene 
    scene = Scene()
    # Create left node
    left = scene.root_node.create_child_node()
    # Create right node
    right = scene.root_node.create_child_node()
    left.transform.translation = Vector3(5, 0, 0)

    # If Center property is True, the extrusion range is from -Height/2 to Height/2, otherwise the extrusion is from 0 to Height
    # Perform linear extrusion on left node using center and slices property
    extrusion = LinearExtrusion(profile, 2)
    extrusion.center = False
    extrusion.slices = 3
    left.create_child_node(extrusion)
    # Set ground plane for reference
    left.create_child_node(Box(0.01, 3, 3))
    # Perform linear extrusion on left node using center and slices property
    extrusion = LinearExtrusion(profile, 2)
    extrusion.center = True
    extrusion.slices = 3
    right.create_child_node(extrusion)
    # Set ground plane for reference
    right.create_child_node(Box(0.01, 3, 3))

    # Save 3D scene
    scene.save(get_output_path("CenterInLinearExtrusion.obj"))
    # ExEnd:CenterInLinearExtrusion            
