from aspose.threed import Scene, Node
from aspose.threed.utilities import Vector3
from examples.Common import *

def Run():
    #ExStart: 1
    # Initialize node 
    n = Node()
    # Get Geometric Translation
    n.transform.geometric_translation = Vector3(10, 0, 0)
    # The first print will output the transform matrix that includes the geometric transformation 
    # while the second one will not.
    print(n.evaluate_global_transform(True))
    print(n.evaluate_global_transform(False))
    #ExEnd: 1
