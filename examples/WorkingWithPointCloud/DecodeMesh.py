from aspose.threed import FileFormat
from aspose.threed.entities import PointCloud
from examples.Common import *

def Run():
    # ExStart:1
    pointCloud = FileFormat.DRACO.decode(get_data_path("point_cloud_no_qp.drc")).cast(PointCloud)
    # ExEnd:1              
