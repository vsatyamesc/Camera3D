import bpy

class Camera3DPanel(bpy.types.Panel):
    bl_label = "Camera3D"
    bl_idname = "VIEW3D_PT_camera3d_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Camera3D'

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        
        box00 = layout.box()
        box00.label(text="Camera3D v0.1")

        box0 = layout.box()
        box0.label(text="Settings")
        box0_row00 = box0.row() # 2D/3D
        box0_row0 = box0.row() # Resolution
        box0_row1 = box0.row() # Samples
        box0_row2 = box0.row() # IPD
        box0_row01 = box0.row() # Engine
        box0_row02 = box0.row() # FLAT / FISHEYE LENS TYPE
        box0_row3 = box0.row() # Apply Settings
        box0_row00.prop(scene, "CameraMode", expand = True)
        box0_row01.prop(scene,"RenderEngine",expand=True)
        box0_row0.prop(scene,"camera_resolution", text="Resolution")
        box0_row1.prop(scene,"samples_value",text="Set Samples")
        box0_row2.prop(scene,"IPD_value",text="Set IPD Value")
        box0_row3.operator("base_operator.apply_settings", text="Apply Settings")
        
        box0_row2.enabled = False
        if scene.CameraMode == "3D" and "Camera3D" not in bpy.data.objects:
            box0_row2.enabled = True

class Camera3DSetup(bpy.types.Panel):
    bl_label = "Camera3D Setup"
    bl_idname = "VIEW3D_PT_camera3dSetup"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Camera3D'

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        
        box0 = layout.box()
        box0.label(text="Environment Setup")
        box0_row0 = box0.row()
        box0_row0.operator("base_operator.add_camera_lr", text="Setup Camera")

        box2 = layout.box()
        box2.label(text="Lens Setup")
        box2_row1 = box2.row()
        box2_row1.prop(scene,"LensType")
        box2_row1.enabled = False
        if "Camera3D" in bpy.data.objects:
            box2_row1.enabled = True

        box1 = layout.box()
        box1.label(text="Copy Camera Transform")
        box1_row0 = box1.row()
        box1_row1 = box1.row()
        object_selector_props = scene.object_selector_props
        box1_row0.prop(object_selector_props, "target_object")
        box1_row1.operator("base_operator.copy_transform_camera", text="Transform")
      
    
class Camera3DHelper(bpy.types.Panel):
    bl_label = "Camera3D Helper"
    bl_idname = "VIEW3D_PT_camera3d_panel_helper"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Camera3D'
    bl_options = {"DEFAULT_CLOSED"}
    
    def draw_header(self, context):
        layout = self.layout
        layout.label(text="", icon="URL")

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        row = layout.row()
        col = row.column()
        docs = col.operator("wm.url_open", text="Documentation", icon="HELP")
        docs.url = "https://github.com/vsatyamesc/Camera3D"        
        error = col.operator("wm.url_open", text="Report Issue", icon="GREASEPENCIL")
        error.url = "https://github.com/vsatyamesc/Camera3D/issues"
