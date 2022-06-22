import io
from aspose.threed import Scene
from examples.Common import *


# WARN: 22.7 is required for this
def run():
    scene = Scene.from_file(get_data_path("EmbeddedTexture.fbx"))
    mat = scene.root_node.child_nodes[0].material.cast(LambertMaterial)
    print(f"Material {mat.name}'s information:")
    print(f"\tDiffuse color = {mat.diffuse_color}", )
    print(f"\tAmbient color = {mat.ambient_color}")
    print(f"\tEmissive color = {mat.emissive_color}")
    print(f"\tTransparency = {mat.transparency}")
    print(f"\tTransparent color = {mat.transparent_color}")
    print(f"\tCustom prop `MyProp` = {mat.get_property('MyProp')}", )
    #dump textures
    tex = mat.get_texture(Material.MAP_DIFFUSE)
    print(f"Texture {tex.name}'s information:")
    print(f"File name = {tex.file_name}")
    print(f"Custom prop `TexProp` = {tex.get_property('TexProp')}")
    if tex.content:
        with open(get_output_path("texture.png", "w")) as f:
            f.write(tex.content)
