from aspose.threed import Scene, FileContentType, FileFormat
from aspose.threed.formats import *
from aspose.threed.entities import Sphere, Box, Cylinder, Light, LightType
from aspose.threed.shading import PhongMaterial, LambertMaterial
from aspose.threed.utilities import MemoryFileSystem, Vector3
from examples import Common
from examples.Common import get_output_path, get_data_path

def RunColladaSaveOption():
    # ExStart:ColladaSaveOption
    saveColladaopts = ColladaSaveOptions()
    # Generates indented XML document
    saveColladaopts.indented = True
    # The style of node transformation
    saveColladaopts.transform_style = ColladaTransformStyle.MATRIX
    # Configure the lookup paths to allow importer to find external dependencies.
    # The path to the documents directory.
    saveColladaopts.lookup_paths = [str(Common.data_path)]
    # ExEnd:ColladaSaveOption
def RunDiscreet3DSSaveOption():
    # ExStart:Discreet3DSSaveOption
    # Initialize an object
    saveOpts = Discreet3dsSaveOptions()
    # The start base for generating name for duplicated names.
    saveOpts.duplicated_name_counter_base = 2
    # The format of the duplicated counter.
    saveOpts.duplicated_name_counter_format = "NameFormat"
    # The separator between object's name and the duplicated counter.
    saveOpts.duplicated_name_separator = "Separator"
    # Allows to export cameras
    saveOpts.export_camera = True
    # Allows to export light
    saveOpts.export_light = True
    # Flip the coordinate system
    saveOpts.flip_coordinate_system = True
    # Prefer to use gamma-corrected color if a 3ds file provides both original color and gamma-corrected color.
    saveOpts.gamma_corrected_color = True
    # Use high-precise color which each color channel will use 32bit float.
    saveOpts.high_precise_color = True
    # Configure the look up paths to allow importer to find external dependencies.
    # The path to the documents directory.
    saveOpts.lookup_paths = [str(Common.data_path)]
    # Set the master scale
    saveOpts.master_scale = 1
    # ExEnd:Discreet3DSSaveOption
def RunFBXSaveOption():
    # ExStart:FBXSaveOption
    # Initialize an object
    saveOpts = FbxSaveOptions(FileFormat.FBX7500ASCII)
    # Generates the legacy material properties.
    saveOpts.export_legacy_material_properties = True
    # Fold repeated curve data using FBX's animation reference count
    saveOpts.fold_repeated_curve_data = True
    # Always generates material mapping information for geometries if the attached node contains materials.
    saveOpts.generate_vertex_element_material = True
    # Configure the look up paths to allow importer to find external dependencies.
    # The path to the documents directory.
    saveOpts.lookup_paths = [str(Common.data_path)]
    # Generates a video object for texture.
    saveOpts.video_for_texture = True
    # ExEnd:FBXSaveOption
def RunObjSaveOption():
    # ExStart:ObjSaveOption
    # Initialize an object
    saveObjOpts = ObjSaveOptions()
    # Import materials from external material library file
    saveObjOpts.enable_materials = True
    # Flip the coordinate system.
    saveObjOpts.flip_coordinate_system = True
    # Configure the look up paths to allow importer to find external dependencies.
    # The path to the documents directory.
    saveObjOpts.lookup_paths = [str(Common.data_path)]
    # Serialize W component in model's vertex position
    saveObjOpts.serialize_w = True
    # Generate comments for each section
    saveObjOpts.verbose = True
    # ExEnd:ObjSaveOption
def RunSTLSaveOption():
    # ExStart:STLSaveOption
    # Initialize an object
    saveSTLOpts = StlSaveOptions()
    # Flip the coordinate system.
    saveSTLOpts.flip_coordinate_system = True
    # Configure the look up paths to allow importer to find external dependencies.
    # The path to the documents directory.
    saveSTLOpts.lookup_paths = [str(Common.data_path)]
    # ExEnd:STLSaveOption
def RunU3DSaveOption():
    # ExStart:U3DSaveOption
    # Initialize an object
    saveU3DOptions = U3dSaveOptions()
    # Export normal data.
    saveU3DOptions.export_normals = True
    # Export the texture coordinates.
    saveU3DOptions.export_texture_coordinates = True
    # Export the vertex diffuse color.
    saveU3DOptions.export_vertex_diffuse = True
    # Export vertex specular color
    saveU3DOptions.export_vertex_specular = True
    # Flip the coordinate system.
    saveU3DOptions.flip_coordinate_system = True
    # Configure the look up paths to allow importer to find external dependencies.
    saveU3DOptions.lookup_paths = [str(Common.data_path)]
    # Compress the mesh data
    saveU3DOptions.mesh_compression = True
    # ExEnd:U3DSaveOption
def RunGlTFSaveOptions():
    # ExStart:glTFSaveOptions
    # Initialize Scene object
    scene = Scene()
    # Create a child node
    scene.root_node.create_child_node("sphere", Sphere())
    # Set glTF saving options. The code example embeds all assets into the target file usually a glTF file comes with some dependencies, a bin file for model's vertex/indices, two .glsl files for vertex/fragment shaders
    # Use opt.EmbedAssets to tells the Aspose.3D API to export scene and embed the dependencies inside the target file.
    opt = GltfSaveOptions(FileContentType.ASCII)
    opt.embed_assets = True
    # Use KHR_materials_common extension to define the material, thus no GLSL files are generated.
    opt.use_common_materials = True
    # Customize the name of the buffer file which defines model
    opt.buffer_file = "mybuf.bin"
    # Save GlTF file
    scene.save(get_output_path("glTFSaveOptions_out.gltf"), opt)

    # Save a binary glTF file using KHR_binary_glTF extension
    scene.save(get_output_path("glTFSaveOptions_out.glb"), FileFormat.GLTF_BINARY)

    # Developers may use saving options to create a binary glTF file using KHR_binary_glTF extension
    opts = GltfSaveOptions(FileContentType.BINARY)
    scene.save(get_output_path("Test_out.glb"), opts)
    # ExEnd:glTFSaveOptions
def RunDRCSaveOptions():
    # ExStart:DRCSaveOptions
    # Initialize Scene object
    scene = Scene()
    # Create a child node
    scene.root_node.create_child_node("sphere", Sphere())
    # Initialize .DRC saving options. 
    opts = DracoSaveOptions()
    # Quantization bits for position
    opts.position_bits = 14
    # Quantization bits for texture coordinate
    opts.texture_coordinate_bits = 8
    # Quantization bits for vertex color
    opts.color_bits = 10
    # Quantization bits for normal vectors
    opts.normal_bits = 7
    # Set compression level
    opts.compression_level = DracoCompressionLevel.OPTIMAL

    # Save Google Draco (.drc) file
    scene.save(get_output_path("DRCSaveOptions_out.drc"), opts)
    # ExEnd:DRCSaveOptions
def DiscardSavingMaterial():
    # ExStart:DiscardSavingMaterial
    # The code example uses the DummyFileSystem, so the material files are not created.
    # Initialize Scene object
    scene = Scene()
    # Create a child node
    scene.root_node.create_child_node("sphere", Sphere()).material = PhongMaterial()
    # Set saving options
    opt = ObjSaveOptions()
    opt.file_system = DummyFileSystem()
    # Save 3D scene
    scene.save(get_output_path("DiscardSavingMaterial_out.obj"), opt)
    # ExEnd:DiscardSavingMaterial
def SavingDependenciesInLocalDirectory():
    # ExStart:SavingDependenciesInLocalDirectory
    # The code example uses the LocalFileSystem class to save dependencies to the local directory.
    # Initialize Scene object
    scene = Scene()
    # Create a child node
    scene.root_node.create_child_node("sphere", Sphere()).material = PhongMaterial()
    # Set saving options
    opt = ObjSaveOptions()
    opt.file_system = LocalFileSystem(dataDir)
    # Save 3D scene
    scene.save(get_output_path("SavingDependenciesInLocalDirectory_out.obj"), opt)
    # ExEnd:SavingDependenciesInLocalDirectory
def SavingDependenciesInMemoryFileSystem():
    # ExStart:SavingDependenciesInMemoryFileSystem
    # The code example uses the MemoryFileSystem to intercepts the dependencies writing.
    # Initialize Scene object
    scene = Scene()
    # Create a child node
    scene.root_node.create_child_node("sphere", Sphere()).material = PhongMaterial()
    # Set saving options
    opt = ObjSaveOptions()
    mfs = MemoryFileSystem()
    opt.file_system = mfs
    # Save 3D scene
    scene.save(get_output_path("SavingDependenciesInMemoryFileSystem_out.obj"), opt)
    # Get the test.mtl file content
    mtl = mfs.get_file_content("SavingDependenciesInMemoryFileSystem_out.mtl")
    with open(get_output_path("Material.mtl"), "wb") as f:
        f.write(mtl)
    # ExEnd:SavingDependenciesInMemoryFileSystem
#/ <summary>
#/ The JSON content of GLTF file is indented for human reading, default value is false
#/ This method is supported by version 19.8 or greater.
#/ </summary>
def PrettyPrintInGltfSaveOption():
    # ExStart:PrettyPrintInGltfSaveOption
    # Initialize 3D scene
    scene = Scene(Sphere())
    # Initialize GLTFSaveOptions
    opt = GltfSaveOptions(FileFormat.GLTF2)
    # The JSON content of GLTF file is indented for human reading, default value is false
    opt.pretty_print = True
    # Save 3D Scene
    scene.save(get_output_path("prettyPrintInGltfSaveOption.gltf"), opt)
    # ExEnd:PrettyPrintInGltfSaveOption
#/ <summary>
#/ Save the 3D scene to HTML5 document
#/ This method is supported by version 19.9 or greater.
#/ </summary>
def RunHtml5SaveOption():
    # ExStart:HtmlSaveOption
    # Initialize 3D scene
    scene = Scene()
    # Create a child node
    node = scene.root_node.create_child_node(Cylinder())
    # Set child node properites
    mat = LambertMaterial()
    mat.diffuse_color = Vector3(0.46, 0.12, 0.56)
    node.material = mat
    light = Light()
    light.light_type = LightType.POINT
    scene.root_node.create_child_node(light).transform.translation = Vector3(10, 0, 10)
    # Create a HTML5SaveOptions
    opt = Html5SaveOptions()
    #Turn off the grid
    opt.show_grid = False
    #Turn off the user interface
    opt.show_ui = False
    # Save 3D to HTML5
    scene.save(get_output_path("HtmlSaveOption.html"), opt)
    # ExEnd:HtmlSaveOption

def RunRVMSaveOptions():
    #ExStart: RVMSaveOptions
    scene = Scene()
    node = scene.root_node.create_child_node("Box", Box())
    node.set_property("rvm:Refno", "=3462123")
    node.set_property("rvm:Description", "This is the description of the box")
    #The RVM attribute's prefix is rvm:, all properties that starts with rvm: will be exported to .att file(the prefix will be removed)
    opt = RvmSaveOptions()
    opt.attribute_prefix = "rvm:"
    opt.export_attributes = True
    scene.save(get_output_path("test.rvm"), opt)
    #ExEnd: RVMSaveOptions

def Run():
    RunColladaSaveOption()
    RunDiscreet3DSSaveOption()
    RunFBXSaveOption()
    RunObjSaveOption()
    RunGlTFSaveOptions()
    RunDRCSaveOptions()
    RunRVMSaveOptions()
    RunHtml5SaveOption()
