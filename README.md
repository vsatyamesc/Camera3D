# Camera3D :frog:
A Blender Addon to assist you with 3D rendering for VR/3D Screens/3D Monitors. Currently Only Supports Full-SBS Image Rendering. Star :star: this repo so you will be notified when it is updated.

You can get yourself a copy from the Release section for Stable Downloads. 

## Description

The settings are elementary. Set the Mode 2D/3D, you have to set 3D, I've added 2D for future update reasons

Resolution:
> It is image Resolution.

Set Samples:
> Your usual Render Samples.

View Mode: Multi-View / Stereo 3D
> 1. Multi View for setting up multiple cameras
> 2. Stereo 3D sets same camera into L/R Mode. Use this for LANDSCAPE, OBJECT FOCUS, HYBRID Camera Mode

IPD Value:
> 1. This is the tricky one. leave 65.0 if you do not understand the next line.
> 2. IPD is the distance between your Pupil in millimeters. It is set to create an illusion of depth in the eyes.

Set Lens Type:
> 1. There are 6 options to set. *180v1, 180v2, FLAT, LANDSCAPE, OBJECT FOCUS, HYBRID *.
> 2. If you want 180 SBS render then choose either of these.
> 3. If you want Diorama like 3D render choose FLAT
> 4. For specific cases, use LANDSCAPE/PARALLEL Lens, OBJECT-FOCUS/Toe-In, HYBRID/Off-Axis.

Environment Setup:
> 1. For Landscape, Object Focus and Hybrid you dont need to setup camera so you can skip.
> 2. After clicking "Setup Camera" The addon will add 3 cameras on the origin. and the Left and Right cameras will be hidden in Viewport, no need to enable those.
> 3. Do not change the Active Camera in the Scene. If you've changed, set the Active Camera to "Camera3D_L" in the "Camera3D" Collection.
> 4. "Camera3D" is the main camera. You need to move this camera only, the other camera will follow its position.

Copy Camera Transform:
> This option helps you copy the location of other cameras (need to select the Camera), so you do not need to set up the new 3D Cameras.

Camera3D helper:
> Links to this repo in case some issue arises or you need to read this again.

You might ask?
> what about Focal Length? Well the effect of Focal length can be studied here http://www.photographers-resource.co.uk/photography/3D/3D_stereo_base.htm
> I will add focal length change in later updates.
## Usage
Just select 3D from the Settings, set your wanted resolutions etc. and Apply Settings. Next Setup camera. You can copy location of other cameras if you want. Render :anatomical_heart:
