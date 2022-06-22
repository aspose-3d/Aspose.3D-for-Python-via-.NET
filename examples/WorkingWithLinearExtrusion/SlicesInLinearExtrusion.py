from aspose.threed import Scene
from aspose.threed.profiles import RectangleShape
from aspose.threed.entities import LinearExtrusion
from aspose.threed.utilities import Vector3
from examples.Common import *

def Run():
    # ExStart:SlicesInLinearExtrusion
    # Initialize the base profile to be extruded
    profile = RectangleShape()
    profile.rounding_radius = 0.3
    # Create a scene 
    scene = Scene()
    # Create left node
    left = scene.root_node.create_child_node()
    # Create right node
    right = scene.root_node.create_child_node()
    left.transform.translation = Vector3(15, 0, 0)
    
    # Slices parameter defines the number of intermediate points along the path of the extrusion
    # Perform linear extrusion on left node using slices property
    left_ex = LinearExtrusion(profile, 2)
    left_ex.slices = 2
    left.create_child_node(left_ex)
    # Perform linear extrusion on right node using slices property
    right_ex = LinearExtrusion(profile, 2)
    right_ex.slices = 10
    right.create_child_node(right_ex)

    # Save 3D scene
    scene.save(get_output_path("SlicesInLinearExtrusion.obj"))
    # ExEnd:SlicesInLinearExtrusion            
