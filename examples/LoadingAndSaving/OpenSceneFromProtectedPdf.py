from aspose.threed import Scene
from aspose.threed.formats import PdfLoadOptions
from examples.Common import *

def Run():
    # ExStart:OpenSceneFromProtectedPdf
    # Create a new scene
    scene = Scene()
    # Use loading options and apply password
    opt = PdfLoadOptions()
    opt.password = "password".encode("utf-8")
    # Open scene
    scene.open(get_data_path("House_Design.pdf"), opt)
    # ExEnd:OpenSceneFromProtectedPdf            
