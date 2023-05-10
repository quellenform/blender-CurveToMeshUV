
***
FAQ
***

Are versions below 3.1 also supported?
======================================

No. This is technically not possible, because some relevant nodes are missing.

What is the technique based on?
===============================

This technique is mainly based on the nodes `Curve to Mesh <https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/curve_to_mesh.html>`_, `Mesh to Curve <https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/mesh_to_curve.html>`_, `Fill Curve <https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/fill_curve.html>`_ and `Extrude Mesh <https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/extrude_mesh.html>`_. Of course, any peculiarities (or bugs) existing in these nodes are inherited.

Why do I get an incorrect Mapping by Cyclic Curves?
===================================================

- Make sure you have set the *Group Outputs* to the **Face Corner** attribute domain
- Check if the curves you used are all ok
- Check the material you are using and the settings for *Scale*, *Offset* and *Rotation*

What does "Free UV Space" mean?
===============================

If this option is enabled, the UVs along the curves are calculated independently of the mesh topology, so that an even distribution can be achieved. Additionally, this distribution can be fixed to a certain size with *Lock UV Space*, so that these UVs are also calculated independently of the length of the curves.

How does Scaling, Offset and Rotation of UVs work?
==================================================

This manipulates the calculated values according to the parameters defined in Geometry Nodes before passing them to the shader. This way you can process multiple curves differently and exactly according to your needs, completely in Geometry Nodes, without having to use a separate mapping in the shader for each object.

How does "Smooth Angle" work?
=============================

With *Smooth Angle*, a detection of the edge angles is performed and all edges whose angles are above the defined value are assumed to be hard edges. However, the edges are split, resulting in a non-monifold mesh. Unfortunately there is no other option in Geometry Nodes, because here the normals of the faces cannot be influenced directly.

**Note:** This option is only available in conjunction with *Hole Tolerant*.

What is "Hole Tolerant"?
========================

In this mode, profile curves that overlap are merged together to create a solid mesh. This process recreates the profile curves and creates a new mesh topology that can correctly handle letters and other complex shapes. In addition, the normals of the resulting inward-facing faces are calculated correctly so that they point in the right direction when they overlap. The technique is primarily based on the `Fill Curve <https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/fill_curve.html>`_ node, which also inherits any disadvantages of this node, such as the deletion of identical edges, or the forced use of 2D curves.

Is it possible to convert the generic attributes to a UV map?
=============================================================

You can always create a UV map for any geometry you have created with Geometry Nodes, as long as you also create an attribute for it with Geometry Nodes (which is the case when using this node group). So you can do that with the PRO/LITE versions as well as with the FREE version.

However, and this is basically the prerequisite when you work with Geometry Nodes, you have to apply the modifier before. Unfortunately, there is no way around this, because Geometry Nodes is a modifier, and as long as it is not applied, no editable mesh exists.

To achieve the desired result you would have to convert the generic attribute created with Geometry Nodes into a UV map. To do this, do the following:

1. Apply the Geometry Nodes modifier by clicking on **Apply** in the *Modifier Properties*.
2. Then switch to the tab *Object Data Properties* and open the item *Attributes*. There you will see the attributes you created before with Geometry Nodes as generic attributes, which have the names you chose.
3. Change to *Object Mode*, select the entry of your UV map and click on the downward pointing arrow (*Attribute Specials*) and then on **Convert Attributes**.
4. As **Mode** you choose instead of **Generic** the entry **UV Map** and click on **OK**.

Now you have converted the UV map created with Geometry Nodes from a generic attribute into a standard UV map and you can change it individually as with any other editable mesh.

I have briefly summarized this in this video:

.. raw:: html

    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; height: auto; margin-bottom: 2em;">
        <iframe src="https://www.youtube.com/embed/Q8oopkJXE4o" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
    </div>
