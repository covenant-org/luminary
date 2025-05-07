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

# 05/05/2025
@VicmanGT
- Implemented sound based alarm that sound when a person's right side face is in front of the camera

https://github.com/user-attachments/assets/7112efbc-12bf-48ab-8224-840be2bcf940


- Created a requirements.txt to implement code in Zeus server
- Cloned code in Zeus server
- When tried to run code got following error: 

ALSA lib pulse.c:242:(pulse_connect) PulseAudio: Unable to connect: Connection refused
```
Traceback (most recent call last):
  File "/home/zeus/Documents/Nuclea_Projects/server-surveillance/main.py", line 14, in <module>
    pygame.mixer.init()
pygame.error: ALSA: Couldn't open audio device: Connection refused
```
- Possible causes are lack of permissions for the user to access the audio in the computer or lack of sound drivers or devices in it

# Activity Report - 06/05/2025

**Email:** brandon@nuclea.solutions

## Main Updates
- A tunnel was successfully created using RTSP and Ngrok to add the office webcam to the VST. It was configured correctly, although for some unknown reason, the webcam image hasn't been successfully displayed within Nvidia's VST.
- Tests were conducted with the Video Wall and Recorded Streams modules to record certain portions of the stream at a specific, configured schedule.
  ![image](https://github.com/user-attachments/assets/b94d2d02-5593-4c79-8494-13076f8bdb1c)
  ![image](https://github.com/user-attachments/assets/d9771467-008e-4401-8588-bc900a65ca02)
- There are plans to use the Wowza platform to access public RTSP services with higher quality and test them in the VST for ROI tracking and tripwire analysis.
- There is suspicion that the poor quality of the streams from Fimex's cameras may be due to the VPN server having very low hardware specs. I contacted Fernando (head of IT at Fimex) to look for a solution to this problem directly from their side.tection.
