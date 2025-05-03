# 02/05/2025
@VicmanGT
- Now the program starts recording a video when a right face profile is detected
- Once the face is not detected or isn't in that position, a timer starts to check the time since the last detection
- if 10 secs have transcurred and the face is no detected the video is saved with a time stamt in .mp4 format
- if the face is again detected the recording continues
- this way, there are no micro videos of a couple frames because the model fails the prediction

## Todo: 
- Clone code in Zeus to try in its webcam
- Implement sound alarm when a right profile is detected 
