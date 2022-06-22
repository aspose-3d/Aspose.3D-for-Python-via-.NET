from aspose.threed import Scene
from aspose.threed.entities import Cylinder
from aspose.threed.shading import PhongMaterial
from aspose.threed.formats import PdfSaveOptions, PdfLightingScheme, PdfRenderMode
from aspose.threed.utilities import Vector3
from examples.Common import *

def Run():
    # ExStart:Save3DInPdf

    # Create a new scene
    scene = Scene()
    # Create a cylinder child node
    mat = PhongMaterial()
    mat.diffuse_color = Vector3(0, 0.3, 0.56)
    
    scene.root_node.create_child_node("cylinder", Cylinder()).material = mat
    
    # Set rendering mode and lighting scheme
    opt = PdfSaveOptions()
    opt.lighting_scheme = PdfLightingScheme.CAD
    opt.render_mode = PdfRenderMode.SHADED_ILLUSTRATION
    # Save in the PDF format
    scene.save(get_output_path("output_out.pdf"), opt)
    # ExEnd:Save3DInPdf           
