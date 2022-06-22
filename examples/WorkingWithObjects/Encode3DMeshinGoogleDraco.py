from aspose.threed import Scene, FileFormat
from aspose.threed.entities import Sphere
from aspose.threed.formats import DracoSaveOptions, DracoCompressionLevel
from examples.Common import *

def Run():
    # ExStart:Encode3DMeshinGoogleDraco
    
    # Create a sphere
    sphere = Sphere()
    # Encode the sphere to Google Draco raw data using optimal compression level.
    opt = DracoSaveOptions()
    opt.compression_level = DracoCompressionLevel.OPTIMAL
    b = FileFormat.DRACO.encode(sphere.to_mesh(), opt)
    # Save the raw bytes to file
    with open(get_output_path("SphereMeshtoDRC_Out.drc"), "wb") as f:
        f.write(b)
    # ExEnd:Encode3DMeshinGoogleDraco              
