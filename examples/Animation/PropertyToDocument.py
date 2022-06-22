from aspose.threed import Scene
from aspose.threed.animation import BindPoint, KeyframeSequence, Interpolation
from examples.Common import get_output_path
from examples import Common


def Run():
    # ExStart:AddAnimationPropertyToDocument
    # Initialize scene object
    scene = Scene()

    # Call Common class create mesh using polygon builder method to set mesh instance 
    mesh = Common.CreateCubeMesh()

    # Each cube node has their own translation
    cube1 = scene.root_node.create_child_node("cube1", mesh)

    # Find translation property on node's transform object
    translation = cube1.transform.find_property("Translation")
    
    # Create a bind point based on translation property
    bindPoint = BindPoint(scene, translation)

    # Create the animation curve on X component of the scale 
    seq = KeyframeSequence()
    # Move node's translation to (10, 0, 10) at 0 sec using bezier interpolation
    seq.add(0, 10.0, Interpolation.BEZIER)
    # Move node's translation to (20, 0, -10) at 3 sec
    seq.add(3, 20.0, Interpolation.BEZIER)
    # Move node's translation to (30, 0, 0) at 5 sec
    seq.add(5, 30.0, Interpolation.LINEAR)
    bindPoint.bind_keyframe_sequence("X", seq)


    seq = KeyframeSequence()
    # Move node's translation to (10, 0, 10) at 0 sec using bezier interpolation
    seq.add(0, 10.0, Interpolation.BEZIER)
    # Move node's translation to (20, 0, -10) at 3 sec
    seq.add(3, -10.0, Interpolation.BEZIER)
    # Move node's translation to (30, 0, 0) at 5 sec
    seq.add(5, 0.0, Interpolation.LINEAR)
    # Create the animation curve on Z component of the scale 
    bindPoint.bind_keyframe_sequence("Z", seq)

    # The path to the documents directory.
    output = get_output_path("PropertyToDocument.fbx");            

    # Save 3D scene in the supported file formats
    scene.save(output)
    # ExEnd:AddAnimationPropertyToDocument

    print("\nAnimation property added successfully to document.\nFile saved at " + output)
    
