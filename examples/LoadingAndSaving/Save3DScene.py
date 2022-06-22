from aspose.threed import Scene, FileFormat
from aspose.threed.formats import FbxSaveOptions
from examples.Common import *
import io

def Run():
    # ExStart:Save3DScene
                
    # Load a 3D document into Aspose.3D
    scene = Scene()

    # Open an existing 3D scene
    scene.open(get_data_path("document.fbx"))

    # Save Scene to a stream
    dstStream = io.BytesIO()
    scene.save(dstStream, FileFormat.FBX7500ASCII)
    
    # Save Scene to a local path
    scene.save(get_output_path("output_out.fbx"), FileFormat.FBX7500ASCII)
    # ExEnd:Save3DScene

    print("\nConverted 3D document to stream successfully.")

def Compression():
    # ExStart:Compression

    # Load a 3D document into Aspose.3D
    scene = Scene(get_data_path("document.fbx"))

    opt = FbxSaveOptions(FileFormat.FBX7500ASCII)
    opt.enable_compression = False
    scene.save(get_output_path("UncompressedDocument.fbx"), opt)
    # ExEnd:Compression
