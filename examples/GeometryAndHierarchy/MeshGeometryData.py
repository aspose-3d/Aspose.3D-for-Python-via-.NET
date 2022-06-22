from aspose.threed import Scene, Node
from aspose.threed.shading import LambertMaterial
from aspose.threed.utilities import Vector3
from examples.Common import *

def Run():
    # ExStart:ShareMeshGeometryData          
    # Initialize scene object
    scene = Scene()

    # Define color vectors
    colors = [
        Vector3(1, 0, 0),
        Vector3(0, 1, 0),
        Vector3(0, 0, 1)
    ]

    # Call Common class create mesh using polygon builder method to set mesh instance 
    mesh = CreateCubeMesh()
   
    idx = 0
    for color in colors:
        # Initialize cube node object
        cube = Node("cube")
        cube.entity = mesh
        mat = LambertMaterial()
        # Set color
        mat.diffuse_color = color
        # Set material
        cube.material = mat
        # Set translation
        cube.transform.translation = Vector3(idx * 20, 0, 0)
        idx += 1
        # Add cube node
        scene.root_node.child_nodes.append(cube)
    
    # The path to the documents directory.
    output = get_output_path("MeshGeometryData.fbx")

    # Save 3D scene in the supported file formats
    scene.save(output)
    # ExEnd:ShareMeshGeometryData
    print("\nMesh’s geometry data shared successfully between multiple nodes.\nFile saved at " + output)

