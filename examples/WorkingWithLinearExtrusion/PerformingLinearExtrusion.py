from aspose.threed import Scene
from aspose.threed.profiles import RectangleShape
from aspose.threed.entities import LinearExtrusion
from aspose.threed.utilities import Vector3
from examples.Common import *

def Run():
    # ExStart:PerformingLinearExtrusion
    # Initialize the base profile to be extruded
    profile = RectangleShape()
    profile.rounding_radius = 0.3
    # Perform Linear extrusion by passing a 2D profile as input and extend the shape in the 3rd dimension
    extrusion = LinearExtrusion(profile, 10)
    extrusion.slices = 100
    extrusion.center = True
    extrusion.twist = 360
    extrusion.twist_offset = Vector3(10, 0, 0)
    # Create a scene 
    scene = Scene()
    # Create a child node by passing extrusion 
    scene.root_node.create_child_node(extrusion)
    # Save 3D scene
    scene.save(get_output_path( "LinearExtrusion.obj"))
    # ExEnd:PerformingLinearExtrusion            
