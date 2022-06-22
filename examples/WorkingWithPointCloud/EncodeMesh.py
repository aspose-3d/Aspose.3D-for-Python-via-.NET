from aspose.threed import FileFormat
from aspose.threed.entities import Sphere
from examples.Common import get_output_path

def Run():
    # ExStart:1
    FileFormat.DRACO.encode(Sphere(), get_output_path("sphere.drc"), None)
    # ExEnd:1              
