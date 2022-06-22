#!/usr/bin/env python3
from examples.AssetInformation import InformationToScene
from examples.Materials import *
from examples.LoadingAndSaving import *
from examples.WorkingWithCylinder import *
from examples.WorkingWithLinearExtrusion import *
from examples.WorkingWithObjects import *
from examples.WorkingWithPointCloud import *
from examples.WorkingWithLinearExtrusion import *
from examples.Animation import *
from examples.Scene import *
from examples.GeometryAndHierarchy import *
from examples.Modeling import *
from examples.Polygons import *
from aspose.threed  import TrialException


print("Open RunExamples.cs. \nIn Main() method uncomment the example that you want to run.")
print("=====================================================")

TrialException.set_suppress_trial_exception(True)

# Uncomment the one you want to try out          

# =====================================================
# =====================================================
# Material and texture access
# =====================================================
# =====================================================

# CreateSceneWithEmbeddedTexture.run()
# DumpEmbeddedTextures.run() #22.7 Required

# =====================================================
# =====================================================
# Loading and Saving
# =====================================================
# =====================================================

# CreateEmpty3DDocument.Run()
# ReadExistingScene.Run()
# DetectFormat.Run()
# Save3DInPdf.Run() #22.7 required
# OpenSceneFromProtectedPdf.Run() # 22.7 required
# ExtractAll3DScenes.Run()
# SaveOptions.SavingDependenciesInMemoryFileSystem() # 22.7 required
# LoadOptions.Run() # 22.7 required
# SaveOptions.Run() # 22.7 required
# NonPBRtoPBRMaterial.Run() # 22.7 required
# Save3DScene.Run() #22.7 required
# Save3DScene.Compression() # 22.7 required
# SaveOptions.PrettyPrintInGltfSaveOption() # 22.7 required


# =====================================================
# =====================================================
# Animation
# =====================================================
# =====================================================

# PropertyToDocument.Run()
# SetupTargetAndCamera.Run()

# =====================================================
# =====================================================
# 3DScene
# =====================================================
# =====================================================

# FlipCoordinateSystem.Run()
# ExportSceneToCompressedAMF.Run()
# ChangePlaneOrientation.Run()
# ThreeDProperties.Run()

# =====================================================
# =====================================================
# Asset Information
# =====================================================
# =====================================================
# InformationToScene.Run()

# =====================================================
# =====================================================
# Geometry and Hierarchy
# =====================================================

# CubeScene.Run()
# MaterialToCube.Run()            
# TransformationToNodeByQuaternion.Run()
# TransformationToNodeByEulerAngles.Run()
# TransformationToNodeByTransformationMatrix.Run()
# NodeHierarchy.Run()
# MeshGeometryData.Run()
# SetupNormalsOnCube.Run() # 22.7 required
# ConcatenateQuaternions.Run()
# ApplyPBRMaterialToBox.Run()
# ExposeGeometricTransformation.Run()

# =====================================================
# =====================================================
# 3D Modeling
# =====================================================
# =====================================================

# Primitive3DModels.Run()

# =====================================================
# =====================================================
# Working with Objects
# =====================================================
# =====================================================

# SplitMeshbyMaterial.Run() # 22.7 required
# ConvertSpherePrimitivetoMesh.Run()
# ConvertBoxPrimitivetoMesh.Run()
# ConvertPlanePrimitivetoMesh.Run()
# ConvertCylinderPrimitivetoMesh.Run()
# ConvertTorusPrimitivetoMesh.Run()
# ConvertSphereMeshtoTriangleMeshCustomMemoryLayout.Run()
# ConvertBoxMeshtoTriangleMeshCustomMemoryLayout.Run()
# BuildTangentAndBinormalData.Run()
# Encode3DMeshinGoogleDraco.Run()
# XPathLikeObjectQueries.Run()
# WorkingWithSphereRadius.Run()
# CreatePolygonInMesh.Run()


# =====================================================
# =====================================================
# Polygons
# =====================================================
# =====================================================
# ConvertPolygonsToTriangles.Run()
# GenerateUV.Run()

# =====================================================
# =====================================================
# Working With Linear Extrusion
# =====================================================
# =====================================================
# PerformingLinearExtrusion.Run()
# SlicesInLinearExtrusion.Run()
# CenterInLinearExtrusion.Run()
# TwistInLinearExtrusion.Run()
# DirectionInLinearExtrusion.Run()

# =====================================================
# =====================================================
# Working With Cylinder
# =====================================================
# =====================================================
# CustomizedOffsetTopCylinder.Run()
# CreateFanCylinder.Run()
# CustomizedShearBottomCylinder.Run()

# =====================================================
# =====================================================
# Working With Point Cloud
# =====================================================
# =====================================================
# DecodeMesh.Run() # 22.7 required
# EncodeMesh.Run()
# EncodeSphereAsPointCloud.Run()
# EncodeMeshToPly.Run()
# ExportToPlyAsPointCloud.Run()
# Export3DSceneAsPointCloud.Run() # 22.7 required

# Stop before exiting
print("\n\nProgram Finished.")
