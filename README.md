![logo](img/logo.png)

Modernized Alternative (of) Yet Another Blender Egg Exporter (MAYBEE)
==============================================================
*Technically MAYABEE, but I don't want to call it that.*

----------------------------------

MAYBEE is a fork of the Yet Another Blender Egg Exporter (YABEE) plugin. It is a renewed Panda3D Egg file exporter for Blender that supports versions >=2.7+

With dozens of outdated YABEE repositories, it's hard to find which version supports modern versions of Blender. MAYBEE sticks out from the outdated YABEE variants.

# Features
MAYBEE has support for exporting the following:
- Meshes
- UV layers
- Materials 
- Vertex colors
- Textures (Diffuse textures and Normal maps)
- Armature (skeleton) animation
- ShapeKeys (morph) animation
- Non-cyclic NURBS Curves

# Limitations
The following are currently not supported/implemented by MAYBEE:
- Properties/tags
- Texture baking via Cycles
- Non-Shader Mode for Materials & Textures

# Installation
The add-on can be installed from the .zip file found in the [latest release](https://github.com/loonaticx/MAYBEE/releases) by following the [Blender documentation](https://docs.blender.org/manual/en/latest/editors/preferences/addons.html#add-on-settings).

# Usage
To export a model as an Egg:
- Ensure the add-on is enabled
- Select the desired objects in the 3D view
- From the navigation bar, select File -> Export -> Panda3D (.egg)
