
************
Installation
************

First, download the appropriate file for the version of Blender you are using. There are three versions available:

- Blender 3.1
- Blender 3.2 - 3.3
- Blender 3.4+

For this product, I have decided against turning it into an installable add-on, as I am convinced that the many add-ons end up creating too many entries in the context menu, through which the node groups can be added in the node editor.

Instead, this is simply a blend file that contains this node group, allowing it to be added individually to one's project at any time.

.. tip::
    In general, the Blender integrated add-on `Node Presets <https://docs.blender.org/manual/en/latest/addons/node/node_presets.html>`_ is available for this purpose, through which individual node groups can be easily added to the personal collection.

    To do this, enable the add-on and save the blend file in a directory of your choice. This automatically makes the node group available to you for reuse under "Template".

    Here you can find more help on this:

    - `How to make an Asset Library for node groups? <https://blender.stackexchange.com/questions/249624/>`_
    - `How can I use custom node groups as node templates/presets? <https://blender.stackexchange.com/questions/260853/>`_

In this case, this is even the preferred variant, since the blend file, even if it contains further application examples, was also built to be used in exactly this way (for example, no subgroups are used, but only a single node tree).

Blender 3.2+
============

Then, if you are using Blender 3.2+, follow these steps:

1. Add the node group from the blend file or import it via :guilabel:`File` > :guilabel:`Append`.
2. Connect your base curve and the profile curve with the corresponding inputs of the node group
3. Add a `Set Material <https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html>`_ node to the geometry in front of *Group Output*
4. Use a shader of your choice, where you use the node `Attribute <https://docs.blender.org/manual/en/latest/render/shader_nodes/input/attribute.html>`_ and the attributes with the name you gave to it

Blender 3.1
===========

If you use this node group in version 3.1, you have to connect the *UV Map* with a *Group Output*, because in this Blender version the node `Store Named Attribute <https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html>`_ is missing.

So the procedure in version 3.1 or when connecting manually is as follows:

1. Connect the socket *UV Map* to a new socket of the *Group Output*.
2. Connect the output *Caps Mask* to a new socket of the *Group Output* (optional, if you want to make the scaling/texturing of the caps independent from the side faces).
3. Set the *Attribute Domain* of these sockets to `Face Corner <https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attributes_reference.html#attribute-domains>`_ (**!!!**).
4. Add a `Set Material <https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html>`_ node to the geometry in front of *Group Output*.
5. Assign an identifier to this attribute in *Output Attributes*.
6. Load the attributes into the shader with the previously assigned identifier.