import bpy

def set_render_engine(self, context):
  engine = str(bpy.context.scene.RenderEngine)
  scene = bpy.data.scenes["Scene"]
  if engine == "CYCLES":
    scene.render.engine = engine
    scene.cycles.feature_set = "SUPPORTED"
    scene.cycles.device = "GPU"
    set_samples(self, context)
  else:
    scene.render.engine = "BLENDER_EEVEE"
    set_samples(self, context)

def set_samples(self, context):
  bpy.data.scenes["Scene"].cycles.samples = bpy.context.scene.samples_value
  bpy.data.scenes["Scene"].cycles.use_adaptive_sampling = True
  bpy.data.scenes["Scene"].cycles.adaptive_threshold = 0.05

def set_resolution(self, context):
  scene = bpy.context.scene
  if scene.camera_resolution == "2k":
    x = 2880
    y = 1620
  elif scene.camera_resolution == "4k":
    x = 3840
    y = 2160
  elif scene.camera_resolution == "6k":
    x = 6144
    y = 3321
  elif scene.camera_resolution == "8k":
    x = 8192
    y = 4428
  scene = bpy.data.scenes["Scene"]
  scene.render.resolution_x = x
  scene.render.resolution_y = y

def set_3d_mode(self, context):
  set_render_engine(self, context)
  format="MULTIVIEW"
  scene = bpy.data.scenes["Scene"]
  render = scene.render
  render.use_multiview = True
  render.views_format = format
  render.image_settings.views_format = "STEREO_3D"
  render.image_settings.stereo_3d_format.display_mode = "SIDEBYSIDE"
  render.image_settings.stereo_3d_format.use_sidebyside_crosseyed = False #Right eye should see left image and vice versa, usually an option inside VR players too so we dont need to worry 
  render.image_settings.stereo_3d_format.use_squeezed_frame = False #Combine L/R to same Image

def set_2d_mode(self, context):
  scene = bpy.data.scenes["Scene"]
  render = scene.render
  render.use_multiview = False
  if "Camera3D" in bpy.data.objects and "Camera3D" in bpy.data.cameras:
    scene.camera = bpy.data.objects["Camera3D"]

def set_mode(self, context):
  if bpy.context.scene.CameraMode == "3D":
    set_3d_mode(self, context)
  else:
    set_2d_mode(self, context)
  