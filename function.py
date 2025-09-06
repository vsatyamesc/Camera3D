import bpy
from . import callbacks
def make_collection(self, context=bpy.context, cols = "Camera3D"):
  if cols not in bpy.data.collections:
    new_col = bpy.data.collections.new(cols)
    bpy.context.scene.collection.children.link(new_col)
    return new_col
  else:
    context.window_manager.popup_menu(
            lambda self, context: self.layout.label(text=f"Collection '{cols}' Already Present in the Scene"),
            title="Info",
            icon='INFO'
        )
    return bpy.data.collections.get(cols)

def delete_camera(camera_list): #Delete if Exists
      for camera_name in camera_list:
        if camera_name in bpy.data.objects:
            camera_obj = bpy.data.objects[camera_name]
            bpy.data.objects.remove(camera_obj, do_unlink=True)
        if camera_name in bpy.data.cameras:
            camera_data = bpy.data.cameras[camera_name]
            bpy.data.cameras.remove(camera_data)

def add_camera(self, context,cols=None):
  callbacks.set_3d_mode(self, context)
  if cols is None:
        cols = bpy.data.collections.get("Camera3D")
        if cols is None:
            cols = make_collection(self, context, "Camera3D")

  camera_list = ["Camera3D", "Camera3D_R","Camera3D_L"]

  delete_camera(camera_list)

  camera_camera = [bpy.data.cameras.new(name=x) for x in camera_list]
  camera_obj = [bpy.data.objects.new(name=x, object_data=y) for x,y in zip(camera_list, camera_camera)]

  for i in camera_obj:
    bpy.context.scene.collection.objects.link(i)
    cols.objects.link(i)
    bpy.context.scene.collection.objects.unlink(i)

  IPD = float(bpy.context.scene.IPD_value)/2000

  displace_camera(camera_camera[1],IPD)
  displace_camera(camera_camera[2],-IPD)

  add_contraint(camera_obj[1],camera_obj[0])
  add_contraint(camera_obj[2],camera_obj[0])

  set_active_camera(camera_obj[0], camera_obj[1])

  for i in camera_obj[1:]:
     obj = bpy.data.objects.get(i.name)
     obj.hide_set(True)

def displace_camera(obj, loc):
  #obj.location[0] = loc
  obj.shift_x = loc

def copy_transform(obj):
  destination = bpy.data.objects["Camera3D"]
  source = obj

  destination.location[0] = source.location[0]
  destination.location[1] = source.location[1]
  destination.location[2] = source.location[2]

  destination.rotation_euler[0] = source.rotation_euler[0]
  destination.rotation_euler[1] = source.rotation_euler[1]
  destination.rotation_euler[2] = source.rotation_euler[2]

def add_contraint(obj, target):
  if obj.type == "CAMERA" and target.type == "CAMERA":
    ctr = obj.constraints.new(type='CHILD_OF')
    ctr.target = target
    ctr.influence = 1.0
  else:
    bpy.context.window_manager.popup_menu(
            lambda self, context: self.layout.label(text="Both objects must be cameras"), 
            title="Error", 
            icon='ERROR'
        )

def set_active_camera(obj1, obj2):
  bpy.data.scenes['Scene'].camera = obj2
  bpy.context.view_layer.objects.active = obj1

