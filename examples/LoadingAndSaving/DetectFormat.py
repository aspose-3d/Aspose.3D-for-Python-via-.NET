from aspose.threed import FileFormat
from examples.Common import *

def Run():
    # ExStart:DetectFormat
    # Detect the format of a 3D file
    inputFormat = FileFormat.detect(get_data_path("document.fbx"))
    # Display the file format
    print(f"File Format: {inputFormat}")
    # ExEnd:DetectFormat            
