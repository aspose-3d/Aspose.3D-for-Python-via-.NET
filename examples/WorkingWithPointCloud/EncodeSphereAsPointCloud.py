from aspose.threed.formats import DracoSaveOptions
from aspose.threed import FileFormat
from aspose.threed.entities import Sphere
from examples.Common import *

def Run():
    # ExStart:1
    opt = DracoSaveOptions()
    opt.point_cloud = True
    FileFormat.DRACO.encode(Sphere(), get_output_path("sphere.drc"), opt)
    # ExEnd:1              
