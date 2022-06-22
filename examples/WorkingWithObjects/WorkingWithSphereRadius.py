from aspose.threed import Scene
from aspose.threed.entities import Sphere
from examples.Common import *

def Run():
    # ExStart:WorkingWithSphereRadius
    # Create a Scene
    scene = Scene()
    # Set Sphere Radius (Using Radius property you can get or set radius of Sphere)
    sphere = Sphere()
    sphere.radius = 10
    scene.root_node.create_child_node(sphere)
    # Save scene
    scene.save(get_output_path("sphere.obj"))
    # ExEnd:WorkingWithSphereRadius              
