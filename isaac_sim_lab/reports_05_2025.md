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

# Activity Report - 02/05/2025

**Email:** brandon@nuclea.solutions

## Main Updates
- An RTSP service was configured so that the webcam from Nuclea's office could be accessed via RTSP streaming.
  ![image](https://github.com/user-attachments/assets/b61ce0a9-2fab-4214-b8f6-0b5952fc7410)

- A separate Docker container was used and configured to manage the VST more effectively.
- The streaming from 4 Fimex cameras was successfully added directly to the VST UI for further analysis.
  ![image](https://github.com/user-attachments/assets/ecb63238-7012-470d-85f0-bb0adc70357e)
  ![image](https://github.com/user-attachments/assets/dc4d4c34-1403-49ae-a588-eb566a55e01b)

- Investigate why the RTSP stream from the webcam did not work within the VST.
- Check why I haven't been able to draw ROI zones and Tripwires on the Fimex streams that appear.

# Activity Report - 05/05/2025

**Email:** brandon@nuclea.solutions

## Main Updates
- Several cameras were configured within the VST (Video Stream Toolkit) in order to enable real-time streaming visualization from the Fimex system. This setup allows for continuous monitoring of the video feeds through the VST interface.
- Some modifications were made to the existing script to enable local recording of the video streams from the Fimex cameras. The purpose of this change was to improve the recording quality and minimize frame loss, which had been an issue in previous versions of the setup.
- An attempt was made to add ROI (Region of Interest) and tripwire tracking to all camera streams using NVIDIA's VST container. However, during testing it was discovered that errors persist in the ROI and tripwire processing logic, preventing the system from correctly handling and analyzing the drawn areas. Further investigation and debugging are required to resolve these issues and ensure accurate event detection.
- A new VNC service was created so that we now have two different accesses to the UI of the Zeus computer, with the objective that Victor and I can work on different desktops, so to speak, and avoid conflicts from working at the same time or moving or closing each other's things.
 ![image](https://github.com/user-attachments/assets/125e015f-c551-4516-8417-7bdf34c7da2e)


