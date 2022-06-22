from aspose.threed import Scene, Node
from aspose.threed.entities import Sphere
from examples.Common import *

def Run():
    # Initialize scene object
    scene = Scene()

    # Initialize Node class object
    cubeNode = Node("sphere")

    # ExStart:ConvertSpherePrimitivetoMesh
    # Initialize object by Sphere class
    convertible = Sphere()
    
    # Convert a Sphere to Mesh
    mesh = convertible.to_mesh()
    # ExEnd:ConvertSpherePrimitivetoMesh

    # Point node to the Mesh geometry
    cubeNode.entity = mesh

    # Add Node to a scene
    scene.root_node.child_nodes.append(cubeNode)

    # The path to the documents directory.
    output = get_output_path("SphereToMeshScene.fbx")

    # Save 3D scene in the supported file formats
    scene.save(output)

    print("\n Converted the primitive Sphere to a mesh successfully.\nFile saved at " + output)
