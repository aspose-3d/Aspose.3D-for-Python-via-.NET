# 3D Processing Python High Code API

[Product Page](https://products.aspose.com/3d/python-net/) | [Docs](https://docs.aspose.com/3d/python-net/) | [Demos](https://products.aspose.app/3d/family) | [API Reference](https://reference.aspose.com/3d/net/) | [Examples](https://github.com/aspose-3d/Aspose.3D-for-Python-via-.NET) | [Blog](https://blog.aspose.com/category/3d/) | [Free Support](https://forum.aspose.com/c/3d/18) | [Temporary License](https://purchase.aspose.com/temporary-license)

[Aspose.3D for Python via .NET](https://products.aspose.com/3d/python-net/) is an easy-to-use 3D game programming & CAD on-premise API. Enhance your Python applications to perform creation, processing & manipulation of 3D models, scenes, geometries, animations, and other three dimensional objects without the need to install any third-party 3D modeling or rendering software. Supports the read, write, edit, remove and other operations on a wide range of 3D file formats.

## 3D Python via .NET On-premise API Features

### 3D Scene Features

- [Create, read, save, import or export a 3D scene](https://docs.aspose.com/3d/python-net/creating-loading-and-saving-3d-scene/).
- Define metadata for the 3D scene to add asset information.
- Ability to flip the coordinate system in the supported (`3DS`, `STL`, `OBJ`, & `U3D`) 3D formats.
- Convert 3D Mesh into custom binary format.
- Export 3D Scene to `AMF` (Compressed) file format.
- Allows to change the orientation of a 3D Scene.

### 3D Geometry Features

- Create 3D Cube Mesh
- Create normal vectors and UV coordinates
- Add materials to 3D objects
- Apply Physical Based Rendering (PBR) Material for efficient and realistic rendering
- Rotate objects in 3D space using Euler angles, quaternion, & custom transformation matrix.
- Create the Transformation Matrix by the chain operations.
- Define logical structure of a 3D scene using node hierarchy.
- Attach geometries, cameras, & lights to nodes.
- Share mesh geometry data among multiple nodes.
- Ability to combine to quaternions to represent orientation in the 3D space.
- Scale geometry of a specific 3D node or scale geometries of all the nodes of a 3D scene.

### 3D Animation Features

- Ability to render the animated scene.
- Support for keeping the light-camera always facing a specified node. (some supported file formats only.)
- Perform object animation (key-frame animation).

### 3D Object Features

- Build binormal & tangent data in a 3D Model for all the meshes.
- Convert the single 3D object mesh into a `PLY` file.
- Convert a Mesh into a triangle mesh and access its vertices.
- Convert the following to Mesh:
  - 3D Sphere to Mesh
  - 3D Box to Mesh
  - 3D Plane to Mesh
  - 3D Cylinder to Mesh
  - 3D Torus to Mesh
- Create a parameterized rectangular torus into the 3D Scene.
- Create, edit & work with the custom  properties of a 3D Scene.
- Ability to split & merge meshes.
- Use the X-Path Query syntax to select specific or more objects under the current node.

### Rendering

- Set the camera & light position.
- Configure which objects may receive the shadow and which ones may cast the shadow.
- Supports creating a Fish-eye lens effect.
- Ability to program the GPU and configure the graphics hardware for 3D rendering.
- Navigate the camera in the 3D scene and place it at your desired position.
- Render a panoramic view of the 3D scene and export it to any of the supported conversion formats.

Please visit the [official documentation](https://docs.aspose.com/3d/python-net/) for a more detailed list of features.

## Read & Write 3D File Formats

**Autodesk&reg; 3D Studio:** 3DS\
**CAD:** AMF, OBJ\
**AVEVA PDMS:** RVM\
**COLLADA:** DAE\
**Google Draco:** DRC\
**MotionBuilder:** FBX\
**3D Models:** GLB\
**Acrobat&reg;:** PDF\
**3D Scanning:** PLY\
**3D Printing:** STL\
**3D PDF:** U3D

## Load 3D File Formats

**Microsoft&reg; 3D Builder:** 3MF\
**Autodesk&reg;:** ASE\
**AutoCAD&reg;:** DXF\
**Siemens&reg; PLM:** JT\
**Pixar&reg;:** USD, USDZ\
**Virtual Reality:** VRML\
**DirectX 3D:** X

## Save 3D Files AS

**Markup:** HTML

Please visit [Supported File Formats](https://docs.aspose.com/3d/python-net/supported-file-formats/) for further details.

## System Requirements

Your machine does not need to have modeling and rendering software installed.

### Supported Operating Systems

**Microsoft Windows&reg;:** Windows Desktop & Server (`x64`, `x86`)
**Linux:** Ubuntu, OpenSUSE, CentOS, and others
**Other:** Any operating system (OS) that can install Mono(.NET 4.0 Framework support) or use .NET core.

### Target Linux Platform

**Runtime Libraries:** `GCC-6` (or later)
**GDI+ API:** `[libgdiplus](https://github.com/mono/libgdiplus)`
**.NET Core:** Dependencies of .NET Core Runtime. Installing .NET Core Runtime itself is NOT required.
**For Python 3.5-3.7:** The `pymalloc` build of Python is needed. The `--with-pymalloc` Python build option is enabled by default. Typically, the `pymalloc` build of Python is marked with `m` suffix in the filename.
**Python Library:** `libpython` shared Python library

### Rendering

- Vulkan `x64` platform, `x86` is not supported.
- AMD Radeon 7700 series and newer
- NVIDIA GeForce 600 series and newer
- Intel Skylake and newer

## Get Started

### Installation via `pip`

The Aspose.3D for Python via .NET is [available at pypi.org](https://pypi.org/project/aspose-3d/). To install it, please run the following command:

`pip install aspose-3d`

### Using Aspose.3D for Python via .NET in your Code

```python
import aspose.threed as a3d

scene = a3d.Scene()
scene.root_node.create_child_node(a3d.entities.Cylinder())
scene.save("Cylinder.fbx", a3d.FileFormat.FBX7400ASCII)
```

## Create a 3D PDF with a Cylinder

{{< gist aspose-3d-gists cfde9f76113134443c76608c1d19453a >}}

[Product Page](https://products.aspose.com/3d/python-net/) | [Docs](https://docs.aspose.com/3d/python-net/) | [Demos](https://products.aspose.app/3d/family) | [API Reference](https://reference.aspose.com/3d/net/) | [Examples](https://github.com/aspose-3d/Aspose.3D-for-Python-via-.NET) | [Blog](https://blog.aspose.com/category/3d/) | [Free Support](https://forum.aspose.com/c/3d/18) | [Temporary License](https://purchase.aspose.com/temporary-license)
