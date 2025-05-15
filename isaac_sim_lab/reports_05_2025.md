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

# 06/05/2025
@VicmanGT
- Investigated causes of the error from yesterday
- pulseaudio is a general purpose sound server to communicate the software and the hardware, and it's not intalled
- Got following error while trying to install it:
```
sudo apt-get install pulseaudio
[sudo] password for zeus: 
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Some packages could not be installed. This may mean that you have
requested an impossible situation or if you are using the unstable
distribution that some required packages have not yet been created
or been moved out of Incoming.
The following information may help to resolve the situation:

The following packages have unmet dependencies:
 pop-pipewire : Depends: pipewire-alsa but it is not going to be installed
                Conflicts: pulseaudio
                Conflicts: pulseaudio:i386
E: Error, pkgProblemResolver::Resolve generated breaks, this may be caused by held packages.
```
- A possible solution is to use Pipewire instead, which is basically the same but more recent
- Also check if there's an actuall sound device or sound card in the server computer
- Also got following video error while ignoring the audio lines in the script:
```
warnings.warn( [ WARN:0@0.292] global cap_v4l.cpp:999 open VIDEOIO(V4L2:/dev/video0): can't open camera by index [ERROR:0@0.292] global obsensor_uvc_stream_channel.cpp:158 getStreamChannelGroup Camera index out of range
```
- This error occurs when the index in ```cv2.VideoCapture(index) ``` surpases the number of available cameras in the device
- Tried to access the camera via VCL -> Media -> Open capture device, on both video0 and video1
```
Your input can't be opened:
VLC is unable to open the MRL 'v4l2:///dev/video0'. Check the log for details.
Your input can't be opened:
VLC is unable to open the MRL 'v4l2:///dev/video1'. Check the log for details.
```
- Check connection with the webcam and Zeus server

# 07/05/2025
@VicmanGT
- Started with the function to detect a movement of the camera
- The idea of keeping track of an object is possibly not going to work as expected
- If for some reason, the detected object is moved or the model confuses the object or stop detecting it there could be a false positive
- The best solution at the moment is the direct comparation of two frames
- Substract the values of the pixel of each frame in grayscale
- If the result if bigger that a certain threshold so the camera has been moved and an alert is generated
- More info:
- https://www.hackersrealm.net/post/motion-detection-tutorial-using-opencv

# Activity Report - 07/05/2025

**Email:** brandon@nuclea.solutions

## Main Updates
- A meeting was scheduled with Fernando (IT manager at Fimex) to upgrade the hardware of the VPN server at the factory in order to improve video quality in the camera streamings, so that the corresponding analysis can be performed later. The hardware upgrade was scheduled for Friday, as the server cannot be shut down during the week.
- It was researched and confirmed that the VST Docker requires a Jetson device to function correctly, since there are specific libraries for those components.
- An attempt was made to test the analysis of the streamings using external libraries (without using VST), but there were many compatibility errors, so it was decided to wait until a Jetson is available to use VST directly and follow the VST documentation (https://docs.nvidia.com/jetson/jps/setup/quick-start.html).

# Activity Report - 08/05/2025

**Email:** brandon@nuclea.solutions

## Main Updates
- To begin ruling out possible errors explaining why the camera streamings at Fimex appear poor when played via RTSP, a Python script was created that launches a local RTSP server using the Mediamtx software. A local 4K video downloaded from YouTube was used and streamed at different resolutions—from 144p up to 4K—to visually assess the smoothness and quality.
- The script was also modified so that, in addition to streaming the videos at different qualities, it saves them locally in a folder organized by resolution.
  ![image](https://github.com/user-attachments/assets/a312dc90-37b7-4970-9988-fcad074b9074)
- The videos were analyzed, and it was observed that lower-quality videos play more smoothly than higher-quality ones. This is likely due to the frame transmission: fewer frames result in faster transmission, while more frames slow it down slightly—but the differences are minimal.
- An attempt will be made to adjust the Fimex streaming configurations to see if lowering the video quality improves streaming smoothness.

# Activity Report - 09/05/2025

**Email:** brandon@nuclea.solutions

## Main Updates
- The Python script was improved using the ffmpeg library to better re-stream local video via RTSP and to download videos in different qualities.
- A method was researched to download videos directly from Hikvision software using its API.
- A way to run Nvidia’s VST without using Jetson was researched and tested; configuration is ongoing, and further testing is needed to confirm its usability.

# 09/05/2025
@VicmanGT
- Fully implemented binary mask in the server surveillance
- Detects movement of the camera based of the average difference in the pixel of two frames
- If it's bigger than threshold then an alarm sounds
- Also detects then an object obstructs the camera view, covering also that case
- Some case that may affect funcitonality is when the camera is moved slowly the average diffence is small and therefore the alarm is not going to sound

https://github.com/user-attachments/assets/d587df69-1d0a-42c4-83e9-db9111e9a72e

# Activity Report - 12/05/2025

**Email:** brandon@nuclea.solutions

## Main Updates
- An attempt was made to reinstall and configure the NVIDIA graphics drivers to enable the nvidia-smi command and allow the system to detect the GPU. However, it could not be fully configured, as the message "Devices not found" continued to appear.
- A solution was sought to download streaming videos without losing quality. A Python script was created that saves the previous 5 minutes of the stream into short video clips. This method preserves both video quality and smooth playback.
- Research was conducted on the protocols used by Hikvision's iVMS-4200 software. It was found that it uses a combination of protocols such as ISUP (Inter-System Unified Protocol), RTSP (Real-Time Streaming Protocol), and ONVIF protocol.

# 12/05/2025
@VicmanGT
- The webcam is working again 
- Continued investigation of error while trying to initialize pygame audio mixer
```
Traceback (most recent call last):
  File "/home/zeus/Documents/Nuclea_Projects/server-surveillance/main.py", line 14, in <module>
    pygame.mixer.init()
pygame.error: ALSA: Couldn't open audio device: Connection refused
```
- Couldn't yet find pages where the specific error was being solved
- Added code to select _pulseaudio_ specifically as the audio driver
```
import os
os.environ['SDL_AUDIODRIVER'] = 'pulseaudio'
```
- And the error is different
```
Traceback (most recent call last):
  File "/home/zeus/Documents/Nuclea_Projects/server-surveillance/main.py", line 20, in <module>
    pygame.mixer.init()
pygame.error: Could not setup connection to PulseAudio
```
- To keep testing, code was added to ignore the audio in case is not available
- Next thing is to add the funcionality of a visual alarm instead of a sound one

# Activity Report - 13/05/2025

**Email:** brandon@nuclea.solutions

## Main Updates
- Another Python script was created to analyze and obtain the streaming videos from the 16 Fimex cameras, which resulted in 32 channels, as each camera offers a main channel with higher resolution and a secondary channel with lower resolution.
- The purpose of this script is to locally save one minute of footage from each camera with a delay of 1 to 5 seconds from the live stream. This recorded video no longer has issues with fluidity or quality, but the downside is that it’s not entirely live.
- It was detected that cameras 9, 10, and 11 on their main channel (channel 1) do not correctly record the full minute locally — they only save one literal second. However, the same cameras on their secondary channel (channel 2) do record the full minute correctly. The cause of this issue has not yet been identified.
- An attempt was made to reinstall the drivers to get the GPU on the Zeus computer working properly again, in order to transfer the Python script there and run it as a service. However, the system still does not properly detect the graphics card.

# Activity Report - 14/05/2025

**Email:** brandon@nuclea.solutions

## Main Updates
- All drivers, including NVIDIA and CUDA, were completely reconfigured again on the Zeus computer to ensure proper functionality of the 5070 graphics card.
- The Python script was improved to record every minute from the 16 camera streams of Fimex and save them locally on ZEUS's 14 TB hard drive.
- A service was created to run every time the Zeus computer starts, so that at the 55th second of every minute, it executes the recording script in parallel for all Fimex cameras for later analysis.
- Kevin was also assisted in setting up a VNC service with the MATE GUI for the Cronus computer. With this, we now have all three computers — Zeus, Gaia, and Cronus — equipped with a system for remote visualization.
