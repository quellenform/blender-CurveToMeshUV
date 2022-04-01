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

![Complete Node v1.0.5](https://i.stack.imgur.com/hyKRa.jpg)



## Usage

1. Add/import the node group from the blend-file
2. Connect the base curve and the profile curve to the node
3. Connect the output `UVs` to a new socket of `Group Output`
4. Connect the output `Caps Mask` to a new socket of `Group Output` (optional, if you want to make the scaling/texturing of the caps independent of the side faces)
5. Set the `Attribute Domain` of this group outputs to [Face corner](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attributes_reference.html#attribute-domains) (!!!)
6. Add a [Set Material](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html) node to the geometry before `Group Output`
7. Assign an identifier for this attributes in `Output Attributes`
8. Load the attributes in the shader with the previously assigned identifier

...Remember: This node works with **Face Corners** and not with **Points**, so always pay attention to the outputs.



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



## Notes
- A more detailed description can be found on [blender.stackexchange.com](https://blender.stackexchange.com/questions/258246)
- On [blenderartists.org](https://blenderartists.org/t/curve-to-mesh-with-uvs-node-group-for-blender-3-0-geometry-nodes/1362714/3), the very talented user *[zeroSkilz](https://blenderartists.org/u/zeroskilz)* has an interesting project in which this mechanism is now also used:
[Z-Curve-Sweeper for Blender 3.0 (Curve-to-Mesh with superpowers)](https://blenderartists.org/t/z-curve-sweeper-for-blender-3-0-curve-to-mesh-with-superpowers/1365277)

> Please leave the credits/authors unchanged if you use this node group in your public projects to support my work and consider a small donation if you like this project.



## Credits

Dedicated to **Dominik Mörth**

Written by **Stephan Kellermayr**
