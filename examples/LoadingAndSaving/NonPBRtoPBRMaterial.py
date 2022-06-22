from aspose.threed import Scene, FileFormat
from aspose.threed.utilities import Vector3
from aspose.threed.shading import PhongMaterial
from aspose.threed.entities import Box
from aspose.threed.formats import GltfSaveOptions
from examples.Common import *

def Run():
    # ExStart:Non_PBRtoPBRMaterial
    # initialize a 3D scene
    s = Scene()
    mat = PhongMaterial()
    mat.diffuse_color = Vector3(1, 0, 1)
    s.root_node.create_child_node("box1", Box()).material = mat
    opt = GltfSaveOptions(FileFormat.GLTF2)
    # save in GLTF 2.0 format
    s.save(get_output_path("Non_PBRtoPBRMaterial_Out.gltf"), opt)
    # ExEnd:Non_PBRtoPBRMaterial
