
bl_info = {
    "name": "Camera3D",
    "blender": (4, 1, 1),
    "category": "3D View",
    "category":"Tool",
    "version": (0,1,0),
    "author": "Satyam",
    "description":"This addon is used to setup 3D camera space so you can render actual 3D within Blender. Currently only supports Full-SBS Mode. Planning to Add Half-SBS and 180 L/R VR. You can use Quest,Vive,Google Cardboard or any other VR to see the renders in 3D"
    "docs": "https://github.com/vsatyamesc/Camera3D"
}

import bpy
from . import properties
from .ui import Camera3DHelper, Camera3DPanel, Camera3DSetup
from .ops import OTCameraRetarget, OTCameraSetup, OTCameraApply

classes = [Camera3DPanel,Camera3DSetup,Camera3DHelper, OTCameraSetup, OTCameraRetarget, OTCameraApply]

def register():
    properties.register()
    for clas in classes:
        bpy.utils.register_class(clas)

def unregister():
    properties.unregister()
    for clas in classes:
        bpy.utils.unregister_class(clas)
