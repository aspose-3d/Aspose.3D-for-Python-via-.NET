from aspose.threed import Scene, FileFormat
from examples.Common import *

def Run():
    # ExStart:ExtractAll3DScenes

    scenes = FileFormat.PDF.extract_scene(get_data_path("House_Design.pdf"), None)
    i = 1
    # Iterate through the scenes and save in 3D files
    for scene in scenes:
        fileName = f"3d-{i}.fbx"
        i += 1
        scene.save(get_output_path(fileName))
    # ExEnd:ExtractAll3DScenes            
