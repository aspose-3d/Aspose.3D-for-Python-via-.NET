from aspose.threed.entities import Mesh
from examples.Common import *

# Create a polygon with 3 vertices(triangle) or 4 vertices(quad)
# This method is supported by version 19.8 or greater.
def Run():
    # ExStart:1
    mesh = Mesh()
    mesh.create_polygon(0, 1, 2)

    #Or You can create a polygon using 4 vertices(quad)
    #mesh.create_polygon(0, 1, 2, 3)
    # ExEnd:1              
