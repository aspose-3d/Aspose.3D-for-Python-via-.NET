from aspose.threed import Scene
from examples.Common import *

def Run():
    # ExStart:FlipCoordinateSystem
    # The path to the input file
    input = get_data_path("camera.3ds");            
    # Initialize scene object
    scene = Scene.from_file(input)
    output = get_output_path( "FlipCoordinateSystem.obj")
    scene.save(output)
    # ExEnd:FlipCoordinateSystem
    print("\nCoordinate system has been flipped successfully.\nFile saved at " + output)
