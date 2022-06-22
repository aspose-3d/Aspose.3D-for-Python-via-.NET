from aspose.threed import Scene
from examples import Common

def Run():
    # ExStart:CreateEmpty3DDocument
    # The path to the documents directory.
    output = Common.get_output_path("document.fbx")

    # Create an object of the Scene class
    scene = Scene()
    # Save 3D scene document
    scene.save(output);
    # ExEnd:CreateEmpty3DDocument

    print("\nAn empty 3D document created successfully.\nFile saved at " + output);
