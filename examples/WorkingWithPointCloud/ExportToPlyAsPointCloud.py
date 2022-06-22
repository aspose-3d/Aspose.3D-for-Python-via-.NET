from aspose.threed import FileFormat
from aspose.threed.formats import PlySaveOptions
from aspose.threed.entities import Sphere
from examples.Common import get_output_path

def Run():
    # ExStart:1
    opt = PlySaveOptions()
    opt.point_cloud = True
    FileFormat.PLY.encode(Sphere(), get_output_path( "sphere.ply"), opt)

    # ExEnd:1              
