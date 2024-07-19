import bpy
from . import function
from .callbacks import set_resolution, set_samples, set_mode
class OTCameraSetup(bpy.types.Operator):
  """This will add the Neccessary Camera Setup to your Blend Scene"""
  bl_idname = "base_operator.add_camera_lr"
  bl_label = "Camera L/R Side-by-Side"
  bl_options = {"REGISTER", "UNDO"}

  def execute(self, context):
    function.make_collection(self, context)
    function.add_camera(self, context)
    return {'FINISHED'}

class OTCameraApply(bpy.types.Operator):
  """Apply the Settings in case the defaults aren't applying"""
  bl_idname = "base_operator.apply_settings"
  bl_label = "Apply Settings"
  bl_options = {"REGISTER", "UNDO"}

  def execute(self, context):
    set_mode(self, context)
    set_resolution(self, context)
    set_samples(self, context)
    return {'FINISHED'}
  
class OTCameraRetarget(bpy.types.Operator):
  """Copy the Location and Rotation of the Target Camera Object to your 3D Camera Setup"""
  bl_idname = "base_operator.copy_transform_camera"
  bl_label = "Camera 3D Location Copier"
  bl_options = {"REGISTER", "UNDO"}

  def execute(self, context):
    scene = context.scene
    camera_target = scene.object_selector_props
    target = camera_target.target_object
    if target:
      function.copy_transform(target)
      return {'FINISHED'}
    else:
        self.report({'WARNING'}, "Target Camera not set.")
        return {'CANCELLED'}
