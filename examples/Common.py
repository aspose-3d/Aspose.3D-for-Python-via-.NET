import pathlib
from aspose.threed.entities import Box
from aspose.threed.utilities import Vector4

base_dir = pathlib.Path(__file__).parent.parent.absolute()
output_path = base_dir.joinpath("output")
data_path = base_dir.joinpath("data")


def get_output_path(fileName):
    if not output_path.exists():
        output_path.mkdir()
    return str(output_path.joinpath(fileName))

def get_data_path(fileName):
    if not data_path.exists():
        data_path.mkdir()
    return str(data_path.joinpath(fileName))

def DefineControlPoints():
    # ExStart:DefineControlPoints
    # Initialize control points
    return [
        Vector4( -5.0, 0.0, 5.0, 1.0),
        Vector4( 5.0, 0.0, 5.0, 1.0),
        Vector4( 5.0, 10.0, 5.0, 1.0),
        Vector4( -5.0, 10.0, 5.0, 1.0),
        Vector4( -5.0, 0.0, -5.0, 1.0),
        Vector4( 5.0, 0.0, -5.0, 1.0),
        Vector4( 5.0, 10.0, -5.0, 1.0),
        Vector4( -5.0, 10.0, -5.0, 1.0)
    ]
    # ExEnd:DefineControlPoints
            
def CreateCubeMesh():
    return (Box()).to_mesh()
