from aspose.threed import Scene
from aspose.threed.entities import Sphere
from aspose.threed.formats import ObjSaveOptions
from examples.Common import *

# Gets or sets the flag whether the exporter should export the scene as point cloud(without topological structure), default value is False
# This method is supported by version 19.8 or greater.
def Run():
    # ExStart:1
    scene = Scene(Sphere())
    opt = ObjSaveOptions()
    opt.point_cloud = True
    scene.save(get_output_path("Export3DSceneAsPointCloud.obj"), opt)
    # ExEnd:1              
