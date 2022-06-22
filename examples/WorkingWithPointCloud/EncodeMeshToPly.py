from aspose.threed import FileFormat
from aspose.threed.entities import Sphere
from examples.Common import *

def Run():
    # ExStart:1
    FileFormat.PLY.encode(Sphere(), get_output_path("sphere.ply"), None)
    # ExEnd:1              
