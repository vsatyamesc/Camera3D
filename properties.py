import bpy
from bpy.types import PropertyGroup
from bpy.props import EnumProperty, IntProperty, FloatProperty, PointerProperty
from . import callbacks

class CameraSelector(PropertyGroup):
    target_object: PointerProperty(
        name="Target Camera",
        type= bpy.types.Object,
        description="Copy Location from another Camera"
    ) # type: ignore

def register():
    bpy.utils.register_class(CameraSelector)

    bpy.types.Scene.camera_resolution = EnumProperty(name="Camera Resolution", default=3, items=[("2k","2K","",1),("4k","4K","",2),("6k","6K","",3),("8k","8K","",4)], update=callbacks.set_resolution)

    bpy.types.Scene.samples_value = IntProperty(name="Samples", default=4096, min=512, max=4096, update=callbacks.set_samples)

    bpy.types.Scene.IPD_value = FloatProperty(name="IPD", description="Distance between your Iris at default position, usually 65 for teen/adults, usually ranges from 61-68 for average person. \nNote: Once this is set and Camera is added, you can't change the IPD again", default=65.0, min=58.0, max=72.0, soft_min=61.0, soft_max=68.0)

    bpy.types.Scene.object_selector_props = PointerProperty(type=CameraSelector)

    bpy.types.Scene.CameraMode = EnumProperty(name="Mode", default=1, items=[("2D","2D","",1), ("3D","3D","",2)], update=callbacks.set_mode)

    bpy.types.Scene.RenderEngine = EnumProperty(name="Render Engine", default=1, items=[("BLENDER_EEVEE","EEVEE","",1), ("CYCLES","CYCLES","",2)], update=callbacks.set_render_engine)

def unregister():
    bpy.utils.unregister_class(CameraSelector)
    del bpy.types.Scene.camera_resolution
    del bpy.types.Scene.samples_value
    del bpy.types.Scene.IPD_value
    del bpy.types.Scene.object_selector_props
    del bpy.types.Scene.CameraMode
    del bpy.types.Scene.RenderEngine