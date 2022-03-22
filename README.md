# CurveToMeshUV

[![Blender](https://img.shields.io/badge/Blender-3.1-%23ea7600?style=for-the-badge)](https:/www.blender.org/)
![License](https://img.shields.io/github/license/quellenform/blender-CurveToMeshUV?style=for-the-badge)
[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg?style=for-the-badge)](https://www.paypal.me/quellenform)

A node group for [Blender](https://www.blender.org/) that creates curve-based meshes with UVs based on [Geometry Nodes](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/index.html).

![Screenshot](https://i.stack.imgur.com/FWlfm.jpg)

## What does it do?

Unfortunately, Blender does not currently generate UVs with the [Curve to Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_to_mesh.html) node, which means that texture mapping is not really possible.
This node group generates these missing UVs for you, based on the existing face corners.

Unlike the approach of calculating the UVs based on vertices, this variant does not modify the curves. The node works with all kinds of curves, and can also handle cyclic curves.

![Complete Node](https://i.stack.imgur.com/lN4MF.jpg)



## Usage

1. add/import the node group from the blend-file
2. connect the base curve and the profile curve to the node
3. connect the output `UVs` to a new socket of `Group Output`
4. set the `Attribute Domain` of this group output to [Face corner](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attributes_reference.html#attribute-domains)
5. add a [Set Material](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html) node to the geometry before `Group Output`
6. assign an identifier for this attribute in `Output Attributes`
7. load the attribute in the shader with the previously assigned identifier



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



## TODO/WIP

- The scaling of cap UVs needs to be optimized.
