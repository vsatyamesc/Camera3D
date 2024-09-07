# Camera3D :frog:
A Blender Addon to assist you with 3D rendering for VR/3D Screens/3D Monitors. Currently Only Supports Full-SBS Image Rendering. Star :star: this repo so you will be notified when it is updated.

You can get yourself a copy from the Release section for Stable Downloads. 

## Description
![Preview](https://github.com/SatyamSSJ10/Camera3D/blob/main/Previews/Docs1.png)

The settings are elementary. Set the Mode 2D/3D, you have to set 3D, I've added 2D for future update reasons

Resolution:
> It is image Resolution.

Set Samples:
> Your usual Render Samples.

IPD Value:
> This is the tricky one. leave 65.0 if you do not understand the next line.
> IPD is the distance between your Pupil in millimeters. It is set to create an illusion of depth in the eyes.

Set Lens Type:
> There are 3 options to set. *180v1, 180v2, FLAT*.
> If you want 180 SBS render then choose either of these.
> If you want Diorama like 3D render choose FLAT

Environment Setup:
> After clicking "Setup Camera" The addon will add 3 cameras on the origin. and the Left and Right cameras will be hidden in Viewport, no need to enable those.
> Do not change the Active Camera in the Scene. If you've changed, set the Active Camera to "Camera3D_L" in the "Camera3D" Collection.
> "Camera3D" is the main camera. You need to move this camera only, the other camera will follow its position.

Copy Camera Transform:
> This option helps you copy the location of other cameras (need to select the Camera), so you do not need to set up the new 3D Cameras.

Camera3D helper:
> Links to this repo in case some issue arises or you need to read this again.

You might ask?
> what about Focal Length? Well the effect of Focal length can be studied here http://www.photographers-resource.co.uk/photography/3D/3D_stereo_base.htm
> I will add focal length change in later updates.
## Usage
Just select 3D from the Settings, set your wanted resolutions etc. and Apply Settings. Next Setup camera. You can copy location of other cameras if you want. Render :anatomical_heart:
