# Camera3D
A Blender Addon to assist you with 3D rendering for VR/3D Screens/3D Monitors. Currently Only Supports Full-SBS Image Rendering.

You can get yourself a copy from the Release section for Stable Downloads.

## Description
![Preview](https://github.com/SatyamSSJ10/Camera3D/blob/main/Previews/Docs.png)

The settings are elementary. Set the Mode 2D/3D, you have to set 3D, I've added 2D for future update reasons

Resolution:
> It is image Resolution.

Set Samples:
> Your usual Render Samples.

IPD Value:
> This is the tricky one. leave 65.0 if you do not understand the next line.
> IPD is the distance between your Pupil in millimeters. It is set to create an illusion of depth in the eyes.

Environment Setup:
> After clicking "Setup Camera" The addon will add two cameras on the origin. and the Left and Right cameras will be hidden in Viewport, no need to enable those.
> Do not change the Active Camera in the Scene. If you've changed, set the Active Camera to "Camera3D_L" in the "Camera3D" Collection.
> "Camera3D" is the main camera. You need to move this camera only, the other camera will follow its position.

Copy Camera Transform:
> This option helps you copy the location of other cameras (need to select the Camera), so you do not need to set up the new 3D Cameras.

Camera3D helper:
> Links to this repo in case some issue arises or you need to read this again.
