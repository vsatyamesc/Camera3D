import bpy
from .function import displace_camera
def show_message_box(msg="", title="Message Box", icon="INFO"):
  def draw(self, context):
            self.layout.label(text=msg)
  bpy.context.window_manager.popup_menu(draw, title = title, icon = icon)

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

def set_ipd(self, context):
    bpy.data.cameras["Camera"].stereo.interocular_distance = float(bpy.context.scene.IPD_value)/1000

    camera_list = ["Camera3D", "Camera3D_R","Camera3D_L"]
    camera_objs = [bpy.data.cameras.get(name=x) for x in camera_list]

    if None in camera_objs:
      return
    
    displace_camera(camera_objs[1], float(bpy.context.scene.IPD_value)/2000)
    displace_camera(camera_objs[2], - float(bpy.context.scene.IPD_value)/2000)

def set_3d_mode(self, context):
  set_render_engine(self, context)
  format= str(bpy.context.scene.ViewMode)
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

def return_cameras():
  cameras = ["Camera3D","Camera3D_L", "Camera3D_R"]
  camera_ = [bpy.data.cameras.get(x) for x in cameras]

  if None in camera_:
    show_message_box(msg="1 or more camera couldn't be found; Recreate the Camera. This shouldn't happend unless you did something.")
    return None

  return camera_

def set_lens_type(self, context):
  lens_type = str(bpy.context.scene.LensType)
  ocs = return_cameras()
  active_camera = bpy.data.cameras.get(bpy.context.scene.camera.name)
  scene_render_settings = bpy.data.scenes["Scene"].render.views_format
  if lens_type == "PANO1":
    for cam in ocs:
      cam.type = "PANO"
      cam.panorama_type = "FISHEYE_EQUISOLID"
      cam.fisheye_lens = 15
      cam.fisheye_fov = 22/7
  elif lens_type == "PANO2":
    for cam in ocs:
      cam.type = "PANO"
      cam.panorama_type = "FISHEYE_LENS_POLYNOMIAL"
      #cam.fisheye_lens = 15
      cam.fisheye_fov = 22/7
  elif lens_type == "PERSP":
    for cam in ocs:
      cam.type = "PERSP"
      cam.lens = 50
  elif lens_type == "PARALLEL":
    active_camera.stereo.convergence_mode = "PARALLEL"
    pass
  elif lens_type == "TOE-IN":
    active_camera.stereo.convergence_mode = "TOE"
    pass
  elif lens_type == "OFF-AXIS":
    active_camera.stereo.convergence_mode = "OFFAXIS"
    pass
  


  