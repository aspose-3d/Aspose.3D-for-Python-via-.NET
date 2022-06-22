from aspose.threed import Scene, Node
from aspose.threed.shading import PhongMaterial, Texture
from aspose.threed.utilities import Vector3
from examples.Common import *

def Run():
    # ExStart:AddMaterialToCube                      
    # Initialize scene object
    scene = Scene()
    
    # Initialize cube node object
    cubeNode = Node("cube")

    # Call Common module create mesh using polygon builder method to set mesh instance 
    mesh = CreateCubeMesh();
 
    # Point node to the mesh
    cubeNode.entity = mesh
    
    # Add cube to the scene
    scene.root_node.child_nodes.append(cubeNode)
    
    # Initiallize PhongMaterial object
    mat = PhongMaterial()
    
    # Initiallize Texture object
    diffuse = Texture()
    
    # The path to the documents directory.
    
    # Set local file path
    diffuse.file_name = get_output_path("surface.dds")

    # Set Texture of the material
    mat.set_texture("DiffuseColor", diffuse)

    # Embed raw content data to FBX (only for FBX and optional)
    # Set file name
    diffuse.file_name = "embedded-texture.png"
    # Set binary content
    with open(get_data_path("aspose-logo.jpg"), "rb") as f:
        diffuse.content = f.read()

    # Set color
    mat.specular_color = Vector3(1, 0, 0)

    # Set brightness
    mat.shininess = 100

    # Set material property of the cube object
    cubeNode.material = mat
    
    output = get_output_path("MaterialToCube.fbx")

    # Save 3D scene in the supported file formats
    scene.save(output)
    # ExEnd:AddMaterialToCube

    print("\nMaterial added successfully to cube.\nFile saved at " + output)

