# Curve to Mesh UV [Free Version]

[![Blender](https://img.shields.io/badge/Blender-3.1+-%23ea7600?style=for-the-badge)](https:/www.blender.org/)
![License](https://img.shields.io/github/license/quellenform/blender-CurveToMeshUV?style=for-the-badge)
[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg?style=for-the-badge)](https://www.paypal.me/quellenform)
[![Buy](https://img.shields.io/badge/Buy-BlenderMarket-green.svg?style=for-the-badge)](https://www.paypal.me/quellenform)

A node group for [Blender](https://www.blender.org/) that creates curve-based meshes with UVs based on [Geometry Nodes](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/index.html).

![Screenshot](https://i.stack.imgur.com/7gbPI.jpg)



## What does it do?

Unfortunately, Blender does not currently generate UVs with the [Curve to Mesh](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_to_mesh.html) node, which means that texture mapping is not really possible.
This node group generates these missing UVs for you, based on the existing face corners.

Unlike the approach of calculating the UVs based on vertices, this variant calculates UVs based on the face corners. The node works with all types of curves and can also process cyclic curves as well as multiple curves simultaneously.

![Complete Node v1.7.02](https://i.stack.imgur.com/dSjQM.png)



## Want more?

The solution presented here is an excerpt from an even more extensive project available in the *Blender Market*, which can also handle overlapping profile curves, as well as correct the normals of the generated faces (interesting for letters or other complex shapes):  
![Complete Node v1.7.02 - Pro Version](https://i.stack.imgur.com/xbSzt.png)

Open source may be all well and good, but development costs time and money. With your contribution you support new features and further updates. Thank you!

Get the full version here: [Curve to Mesh UV - Perfect UVs with Geometry Nodes](https://blendermarket.com/products/curve-to-mesh-uv)

See it in action on [YouTube](https://www.youtube.com/watch?v=tcePCjJxZ20)



## Usage

1. Add/import the node group from the blend-file
2. Connect the base curve and the profile curve to the node
3. Connect the output `UV Map` to a new socket of `Group Output`
4. Connect the output `Caps Mask` to a new socket of `Group Output` (optional, if you want to make the scaling/texturing of the caps independent of the side faces)
5. Set the `Attribute Domain` of this group outputs to [Face corner](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attributes_reference.html#attribute-domains) (!!!)
6. Add a [Set Material](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html) node to the geometry before `Group Output`
7. Assign an identifier for this attributes in `Output Attributes`
8. Load the attributes in the shader with the previously assigned identifier

Remember: This node works with **Face Corners** and not with **Points**, so always pay attention to the outputs.



## Notes
- This free version is optimized for Blender 3.4, but can be easily adapted to version 3.1 with a few minor changes (*Lite* and *Pro* are compatible to 3.1+)
- The *Lite* and *Pro* editions include more functions for processing intersecting profile curves and other very nice features
- The *Lite* and *Pro* edition can be purchased at [Blender Market](https://blendermarket.com/products/curve-to-mesh-uv)
- A more detailed description can be found on [blender.stackexchange.com](https://blender.stackexchange.com/questions/258246)
- On [blenderartists.org](https://blenderartists.org/t/curve-to-mesh-with-uvs-node-group-for-blender-3-0-geometry-nodes/1362714/3), the very talented user *[zeroSkilz](https://blenderartists.org/u/zeroskilz)* has an interesting project in which an older version of this mechanism is also used:
[Z-Curve-Sweeper for Blender 3.0 (Curve-to-Mesh with superpowers)](https://blenderartists.org/t/z-curve-sweeper-for-blender-3-0-curve-to-mesh-with-superpowers/1365277)

> Please consider a small donation if you like this project, or buy the full version at [Blender Market](https://blendermarket.com/products/curve-to-mesh-uv) to support further development. Thank you!



## Credits

Dedicated to **Dominik Mörth**

Written by **Stephan Kellermayr**
