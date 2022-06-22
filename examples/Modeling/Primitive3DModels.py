from aspose.threed import Scene
from aspose.threed.entities import Box, Cylinder
from examples.Common import *

def Run():
    # ExStart:Primitive3DModels
    # The path to the documents directory.

    # Initialize a Scene object
    scene = Scene()
    # Create a Box model
    scene.root_node.create_child_node("box", Box())
    # Create a Cylinder model
    scene.root_node.create_child_node("cylinder", Cylinder())
    # Save drawing in the FBX format
    output = get_output_path("test.fbx")
    scene.save(output)

    # ExEnd:Primitive3DModels
    print("\nBuilding a scene from primitive 3D models successfully.\nFile saved at " + output);
