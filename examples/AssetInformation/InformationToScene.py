#!/usr/bin/env python3
from examples.Common import get_output_path
import aspose.threed as a3d


def Run():
    # ExStart:AddAssetInformationToScene           
    # Initialize a 3D scene
    scene = a3d.Scene()

    # Set application/tool name
    scene.asset_info.application_name = "Egypt"

    # Set application/tool vendor name
    scene.asset_info.application_vendor = "Manualdesk"

    # We use ancient egyption measurement unit Pole
    scene.asset_info.unit_name = "pole"

    # One Pole equals to 60cm
    scene.asset_info.unit_scale_factor = 0.6

    # The saved file
    output = get_output_path("InformationToScene.fbx")

    # Save scene to 3D supported file formats
    scene.save(output)
    # ExEnd:AddAssetInformationToScene

    print("\nAsset information added successfully to Scene.\nFile saved at " + output)

if __name__ == "__main__":
    run()
