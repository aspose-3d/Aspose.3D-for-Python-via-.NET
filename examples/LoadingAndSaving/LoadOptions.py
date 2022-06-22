from aspose.threed import Scene
from aspose.threed.formats import *
from examples import Common
from examples.Common import get_data_path, get_output_path

def RunDiscreet3DSLoadOption():
    # ExStart:Discreet3DSOption
    loadOpts = Discreet3dsLoadOptions()
    # Sets wheather to use the transformation defined in the first frame of animation track.
    loadOpts.apply_animation_transform = True
    # Flip the coordinate system
    loadOpts.flip_coordinate_system = True
    # Prefer to use gamma-corrected color if a 3ds file provides both original color and gamma-corrected color.
    loadOpts.gamma_corrected_color = True
    # Configure the look up paths to allow importer to find external dependencies.
    # The path to the documents directory.
    loadOpts.lookup_paths = [str(Common.data_path)]
    # ExEnd:Discreet3DSOption
def RunObjLoadOption():
    # ExStart:ObjLoadOption
    # Initialize an object
    loadObjOpts = ObjLoadOptions()
    # Import materials from external material library file
    loadObjOpts.enable_materials = True
    # Flip the coordinate system.
    loadObjOpts.flip_coordinate_system = True
    # Configure the look up paths to allow importer to find external dependencies.
    loadObjOpts.lookup_paths = [str(Common.data_path)]
    # ExEnd:Discreet3DSOption
def RunObjLoadOption():
    # ExStart:ObjLoadOption
    # Initialize an object
    loadObjOpts = ObjLoadOptions()
    # ExEnd:ObjLoadOption
def RunSTLLoadOption():
    # ExStart:STLLoadOption
    # Initialize an object
    loadSTLOpts = StlLoadOptions()
    # Flip the coordinate system.
    loadSTLOpts.flip_coordinate_system = True
    # Configure the look up paths to allow importer to find external dependencies.
    loadSTLOpts.lookup_paths = [str(Common.data_path)]
    # ExEnd:STLLoadOption
def RunU3DLoadOption():
    # ExStart:U3DLoadOption
    # Initialize an object
    loadU3DOpts = U3dLoadOptions()
    # Flip the coordinate system.
    loadU3DOpts.flip_coordinate_system = True
    # Configure the look up paths to allow importer to find external dependencies.
    loadU3DOpts.lookup_paths = [str(Common.data_path)]
    # ExEnd:U3DLoadOption
def RunglTFLoadOptions():
    # ExStart:glTFLoadOptions
    # Initialize Scene class object
    scene = Scene()
    # Set load options
    loadOpt = GltfLoadOptions()
    # The default value is True, usually we don't need to change it. Aspose.3D will automatically flip the V/T texture coordinate during load and save.       
    loadOpt.flip_tex_coord_v = True
    scene.open(get_data_path("Duck.gltf"), loadOpt)
    # ExEnd:glTFLoadOptions
def RunPlyLoadOptions():
    # ExStart:PlyLoadOptions
    # initialize Scene class object
    scene = Scene()
    # initialize an object
    loadPLYOpts = PlyLoadOptions()
    # Flip the coordinate system.
    loadPLYOpts.flip_coordinate_system = True
    # load 3D Ply model
    scene.open(get_data_path("vase-v2.ply"), loadPLYOpts)
    # ExEnd:PlyLoadOptions
def RunXLoadOptions():
    # ExStart:XLoadOptions
    # initialize Scene class object
    scene = Scene()
    # initialize an object
    loadXOpts = XLoadOptions(FileContentType.ASCII)
    # flip the coordinate system.
    loadXOpts.flip_coordinate_system = True
    # load 3D X file
    scene.open(get_data_path("warrior.x"), loadXOpts)
    # ExEnd:XLoadOptions
def RunFBXLoadOptions():
    #ExStart: FBXLoadOptions
    #This will output all properties defined in GlobalSettings in FBX file.
    scene = Scene()
    opt = FbxLoadOptions()
    opt.keep_builtin_global_settings = True
    scene.open(get_data_path("test.fbx"), opt)
    for property in scene.root_node.asset_info.properties:
        print(property)
    #ExEnd: FBXLoadOptions

def Run():
    RunDiscreet3DSLoadOption()
    RunObjLoadOption()
    RunSTLLoadOption()
    RunU3DLoadOption()
    RunglTFLoadOptions()
    RunPlyLoadOptions()
    RunFBXLoadOptions()
