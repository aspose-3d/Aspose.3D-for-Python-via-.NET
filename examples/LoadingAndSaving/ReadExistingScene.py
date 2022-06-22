from aspose.threed import Scene,FileFormat
from examples.Common import *

def ReadExistingSceneFromDisc():
    # ExStart:ReadExistingScene
    # The path to the documents directory.

    # Initialize a Scene class object
    scene = Scene()
    # Load an existing 3D document
    scene.open(get_data_path("document.fbx"))

    # ExEnd:ReadExistingScene
    print("\n3D Scene is ready for the modification, addition or processing purposes.")

def ReadRVMWithAttributes():
    #ExStart:ReadRVMWithAttributes
    scene = Scene.from_file(get_data_path("att-test.rvm"))

    FileFormat.RVM_BINARY.load_attributes(scene, get_data_path("att-test.att"), 'rvm:')
    #ExEnd: ReadRVMWithAttributes

def Run():
    ReadExistingSceneFromDisc()
    ReadRVMWithAttributes()
