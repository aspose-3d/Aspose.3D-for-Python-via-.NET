from aspose.threed import Scene
from aspose.threed.entities import Camera, Light
from examples.Common import *

def Run():
    # ExStart:XPathLikeObjectQueries
    #Create a scene for testing 
    s = Scene()
    a = s.root_node.create_child_node("a")
    a.create_child_node("a1")
    a.create_child_node("a2")
    s.root_node.create_child_node("b")
    c = s.root_node.create_child_node("c")
    c.create_child_node("c1").add_entity(Camera("cam"))
    c.create_child_node("c2").add_entity(Light("light"))
    #The hierarchy of the scene looks like:
    # - Root
    #    - a
    #        - a1
    #        - a2
    #    - b
    #    - c
    #        - c1
    #            - cam
    #        - c2
    #            - light
    #select objects that has type Camera or name is 'light' whatever it's located.
    objects = s.root_node.select_objects("#*[(@Type = 'Camera') or (@Name = 'light')]")
    #Select single camera object under the child nodes of node named 'c' under the root node
    c1 = s.root_node.select_single_object("/c/*/<Camera>")
    # Select node named 'a1' under the root node, even if the 'a1' is not a directly child node of the 
    obj = s.root_node.select_single_object("a1")
    #Select the node itself, since the '/' is selected directly on the root node, so the root node is selected.
    obj = s.root_node.select_single_object("/")
    # ExEnd:XPathLikeObjectQueries              
