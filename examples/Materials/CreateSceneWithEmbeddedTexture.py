#!/usr/bin/env python3
from examples import Common
import aspose.threed as a3d
from aspose.threed.shading import Texture, LambertMaterial, Material
from aspose.threed.entities import Torus
import io
from PIL import Image, ImageDraw, ImageFont


def CreateTextureContent():
    image = Image.new("RGB", (256, 32), "grey")
    draw = ImageDraw.Draw(image)
    draw.text((10, 10), "Aspose.3D", fill="yellow")
    buf = io.BytesIO()
    image.save(buf, format='JPEG')
    return buf.getvalue()

def run():
    #Create a FBX file with embedded textures
    scene = a3d.Scene()

    #Create an embedded texture
    tex = Texture()
    tex.content = CreateTextureContent()
    #file name is required if the embedded texture is used.
    tex.file_name = "test.png"
    tex.set_property("TexProp", "value")
    #create a material with custom property
    mat = LambertMaterial("my-mat")
    mat.set_texture(Material.MAP_DIFFUSE, tex)
    mat.set_property("MyProp", 1.0)

    #create a torus with this material applied
    scene.root_node.create_child_node(Torus()).material = mat
    #save this to file
    scene.save(Common.get_output_path("test.fbx"))
