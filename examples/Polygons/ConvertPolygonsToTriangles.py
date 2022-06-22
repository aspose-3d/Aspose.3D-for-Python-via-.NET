from aspose.threed import Scene
from aspose.threed.entities import PolygonModifier
from examples.Common import *

def Run():
    # ExStart:ConvertPolygonsToTriangles
    # Load an existing 3D file
    scene = Scene(get_data_path("document.fbx"))
    # Triangulate a scene
    PolygonModifier.triangulate(scene)
    # Save 3D scene
    scene.save(get_output_path("triangulated_out.fbx"))
    # ExEnd:ConvertPolygonsToTriangles 
