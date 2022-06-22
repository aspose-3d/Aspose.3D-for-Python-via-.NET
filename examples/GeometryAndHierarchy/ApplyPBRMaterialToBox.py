from aspose.threed import Scene
from aspose.threed.shading import PbrMaterial
from aspose.threed.entities import Box
from examples.Common import *

def Run():
    # ExStart:ApplyPBRMaterialToBox
    # initialize a scene
    scene = Scene()
    # initialize PBR material object
    mat = PbrMaterial()
    # an almost metal material
    mat.metallic_factor = 0.9
    # material surface is very rough
    mat.roughness_factor = 0.9
    # create a box to which the material will be applied
    boxNode = scene.root_node.create_child_node("box", Box())
    boxNode.material = mat
    # save 3d scene into STL format
    scene.save(get_output_path("PBR_Material_Box_Out.stl"))
    # ExEnd:ApplyPBRMaterialToBox  
