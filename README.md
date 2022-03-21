# CurveToMeshUV

[![Blender](https://img.shields.io/badge/Blender-3.1-%23ea7600?style=for-the-badge)](https:/www.blender.org/)
![License](https://img.shields.io/github/license/quellenform/blender-CurveToMeshUV?style=for-the-badge)
[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg?style=for-the-badge)](https://www.paypal.me/quellenform)

A NodeGroup for [Blender](https://www.blender.org/) that creates curve-based meshes with UVs.



## What does it do?

Unfortunately, Blender does not generate UVs with the [Curve to Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_to_mesh.html) node, which means that texture mapping is not really possible.
This NodeGroup generates these missing UVs for you, based on the existing Face Corners.



## Options

| Option | Description |
| ----- | ----------- |
| `Free U-Space (Sides)` | If this option is activated, the texture is distributed over the entire length. This allows vertical mapping that is not bound to individual faces. |
| `Fixed U-Scale` | If you activate this option, the U-axis will not be scaled together with the object. Instead, it retains its defined size. (*Available only when "Free U-Space (Sides)" is enabled)* |
| `Free V-Space (Sides)` | If this option is activated, the texture is distributed over the entire width. This allows horizontal mapping that is not bound to individual faces. |
| `Fixed V-Scale` | If you activate this option, the V-axis will not be scaled together with the object. Instead, it retains its defined size. (*Available only when "Free V-Space (Sides)" is enabled)* |
| `Fill Caps` | Add additional faces for the Caps |
| `Fixed UV-Scale (Caps)` | If this option is activated, the texture retains a fixed size and is not distributed over the entire length/width. |
| `Triangulate Caps` | Triangulate the Caps of the Mesh |



## Changelog

### v1.04
- FEATURE: Triangulate Caps
- Node cleanup & inline documentation

### v1.03
- Restructured Options for UV-Scaling

### v1.02
- Changed the behaviour of UV scaling

### v1.01
- Cleanup

### v1.00
- Initial release (first stable version)



## TODO/WIP

- The scaling of cap UVs needs to be optimized.
