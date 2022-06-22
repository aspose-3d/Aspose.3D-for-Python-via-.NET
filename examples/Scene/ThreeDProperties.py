from aspose.threed import Scene
from examples.Common import *

def Run():
    #ExStart: ThreeDProperties
    scene = Scene(get_data_path("EmbeddedTexture.fbx"))
    material = scene.root_node.child_nodes[0].material
    props = material.properties
    #List all properties using foreach
    for prop in props:
        print(f"{prop.name} = {prop.value}")
    #Get property instance by name
    pdiffuse = props.find_property("Diffuse")
    print(pdiffuse)
    #Since Property is also inherited from A3DObject
    #It's possible to get the property of the property
    print("Property flags = {0}", pdiffuse.get_property("flags"))
    #and some properties that only defined in FBX file:
    print("Label = {0}", pdiffuse.get_property("label"))
    print("Type Name = {0}", pdiffuse.get_property("typeName"))
    #so traversal on property's property is possible
    for pp in pdiffuse.properties:
        print(f"Diffuse.{pp.name} = {pp.value}")
    #ExEnd: ThreeDProperties
