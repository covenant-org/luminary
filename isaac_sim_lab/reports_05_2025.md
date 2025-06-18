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

# Activity Report - 15/05/2025

**Email:** brandon@nuclea.solutions

## Main Updates
- The Python script for recording Fimex camera streams was modified to remove the audio from all streams, and the organization for saving the videos was improved by structuring them by day and minute within their respective folders.
- A new Docker container was configured using DeepStream together with NVIDIA VST to analyze the RTSP video streams from the cameras. However, the setup has not yet been able to complete the ROI and tripwire mapping on the streams, although an improvement in the smoothness and quality of each stream was observed.
- An attempt will be made to run VST locally on the Zeus computer to analyze each saved video individually without relying on a specific NVIDIA Docker container, since there is a suspicion that it only works—or is better optimized—on Jetson devices.

# 15/05/2025
@VicmanGT
- Fixed audio driver problem by changing from ```pulseaudio``` to ```pipewire```
- Setup of virtual environment to have better control of library's version
- Got past errors:
```
UserWarning: 
NVIDIA GeForce RTX 5070 Ti with CUDA capability sm_120 is not compatible with the current PyTorch installation.
The current PyTorch install supports CUDA capabilities sm_50 sm_60 sm_70 sm_75 sm_80 sm_86 sm_90.
If you want to use the NVIDIA GeForce RTX 5070 Ti GPU with PyTorch, please check the instructions at https://pytorch.org/get-started/locally/
```
```
RuntimeError: CUDA error: no kernel image is available for execution on the device
CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.
For debugging consider passing CUDA_LAUNCH_BLOCKING=1
Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions.
```
- Fixed with the already found solution
```
pip uninstall torch
pip install --pre torch torchvision --index-url https://download.pytorch.org/whl/nightly/cu128
```
## Todo: 
- Check how to make the script run at all times
- Implement robust error handling
- Check what causes error message and if it affects:
```
Qt: Session management error: None of the authentication protocols specified are supported
```

# Activity Report - 16/05/2025

**Email:** brandon@nuclea.solutions

## Main Updates
- Another attempt was made to configure VST for analyzing the video streams from some of the Fimex cameras, but it was unsuccessful. The method to draw ROI lines and tripwires in the system has not yet been figured out.
- YOLOv5 was installed and configured on Zeus, along with the PyTorch libraries adapted for CUDA version 12.9.
- Since VST has not been able to function properly, a local test was conducted using YOLOv5 and a new Python script designed to read all the videos recorded on a specific day for a specific camera, with the purpose of detecting people who appear or pass through each frame of the video. This was the first version of the script, but it still needs improvement.
- I also provided support at Elite to restore functionality to a computer that suddenly failed, which was an urgent issue to resolve.

# 19/05/2025
@VicmanGT
- Fully implemented the alarm system for the Zeus server
- Setted a service to make it run 24/7
- Added logging statements to debug in case of errors
- Commented lines of code from cv2 to prevent it to make calls to the GUI
- There's need for physical testing to see if the alarm works

# Activity Report - 19/05/2025

**Email:** brandon@nuclea.solutions

## Main Updates
- The Python algorithm for detecting people using YOLO was slightly improved, although progress on that was paused as the priority shifted to improving the streaming quality of the Fimex cameras.
- To improve the quality of video downloads from the Fimex cameras, the algorithm was changed to enhance the frame rate and avoid encoding in a format that causes frame loss. However, we encountered an issue where the VPN server stopped working since the morning. I contacted Fernando (Fimex’s IT manager) to find a solution, but I haven’t received any response yet.
- I also developed another Python algorithm that takes the saved one-minute video clips and generates an RTSP stream, so it can later be used in the VST, since it seems to only accept that format.

# Activity Report - 20/05/2025

**Email:** brandon@nuclea.solutions

## Main Updates
- I downloaded the code from the VST container in Envida to inspect it locally, file by file. After the inspection, I realized that there are binaries or executables, headers, .json configuration files, and libraries being used, but I couldn’t find actual source code that shows the full programming logic of the VST module.
- I created an account on Wowza to be able to stream RTSP publicly from that platform in order to later test it with the VST. Although I managed to stream a video I downloaded from YouTube, for some reason the VST still didn’t detect it to display an image — even though both FFplay and VLC did.
- I also made the Python algorithm stream previously recorded videos (before the Fimex VPN failed) over RTSP, so I could stream them locally from the VST. However, this also failed — it was not able to detect any image.
- The issue with the VPN used to access the Fimex cameras’ streams still persists, so I couldn’t make any further progress in resolving the video transmission quality issue.

# Activity Report - 27/05/2025

**Email:** brandon@nuclea.solutions

## Main Updates
- The VNC UI was changed to the Mate UI on the ZEUS computer, as it had recently been replaced with a more basic one.
- A test was performed with the office camera to connect it via RTSP to NVIDIA's VS; the video could be viewed, but unfortunately, the ROI and tripwire drawing have not yet been achieved.
- Initial configurations and implementations of NVIDIA’s Video Search and Summarization Agent were carried out. The web UI was successfully launched and one of the videos was selected for analysis, although the database still needs to be configured due to some errors.
  ![image](https://github.com/user-attachments/assets/b7cbf7cf-5d70-47ce-be0e-6583c3f841b2)
- Final modifications and bug fixes were made on Fidestech.

# Activity Report - 30/05/2025

**Email:** brandon@nuclea.solutions

## Main Updates
- Alternatives were researched to use NVIDIA's VST through libraries like DeepStream locally, as well as other visual interpretation libraries, since the Docker or container provided by NVIDIA is highly optimized for use on a Jetson device.
- Additional configurations were made to NVIDIA's Video Search and Summarization to run it locally. Tests were conducted using a pre-recorded video from the Fimex camera we had stored and with the RTSP stream from the office camera at Nuclea. While we were able to retrieve the video feed, an error related to the database appeared when attempting to analyze or summarize the content.
- Based on that error, a Python script was developed to simulate a service called NIM from NVIDIA, aiming to launch an embedding-based database on a specific local computer port. However, even with this workaround, it has not been possible to successfully analyze videos uploaded to the Video Search and Summarization UI.
- In other projects, new versions were delivered and bugs were fixed on the Fidestech platform.

# Activity Report - 02/06/2025

**Email:** brandon@nuclea.solutions

## Main Updates
- A new solution was sought to run NVIDIA's Video Research and Summarization locally by removing some libraries and configuring new ports in order to run both the frontend and backend from the computer named Zeus. However, the expected result has not yet been achieved.
- Recorded videos from NVIDIA's VST using the office camera via RTSP were analyzed and downloaded. It was discovered that the videos are indeed saved in the folder specified in the configuration file, stored in .mkv format within the previously set time intervals. They are also saved using the timestamp in milliseconds of the recording time, organized into folders named after the recording date.
- Initial setup of the Jetson device at NUCLEA was started to perform a test using NVIDIA's VST, as the reason why the ROI and tripwire lines are not being traced in the recordings has not yet been identified.

# Activity Report - 03/06/2025

**Email:** brandon@nuclea.solutions

## Main Updates
- VNC was installed and configured on Nuclea's Jetson to remotely view the Mate UI from my local computer.
- There were some issues getting browsers like Firefox or Chromium to work, but it was resolved by installing some missing Snap dependencies and configuring VNC to successfully run the Chromium browser on the Jetson.
- The NVIDIA VST UI was successfully launched, and the initial configurations were completed from the Jetson.
  ![image](https://github.com/user-attachments/assets/4fbf70aa-1127-4e86-84a8-53f60a7da86b)
- There were problems when trying to ping or view the office camera stream from the Jetson, as it is on a different network. An attempt was made to configure WireGuard to remotely connect to the camera's IP, but unfortunately, it was unsuccessful. Further tests will be attempted tomorrow or assistance will be requested during the meeting.

# Activity Report - 04/06/2025

**Email:** brandon@nuclea.solutions

## Main Updates
- Additional local tests were performed on Zesu's machine to get the backend with embeddings working for NVIDIA's Video Research and Summarization tool.
- The necessary configurations were made to successfully launch the VST from the Jetson.
- The office camera at Nuclea was successfully connected to the Jetson through VPN configurations applied in the WireGuard config file, allowing access to the camera's IP addresses.
- The camera was successfully added to NVIDIA's VST, but when drawing the ROI and tripwire lines, the same rendering error appeared. An investigation will be conducted to determine which Jetson library is missing in order to fix this issue.
  ![image](https://github.com/user-attachments/assets/1ad0c1e8-e17a-4ee3-a05e-01e0ed017f55)

# Activity Report - 10/06/2025

**Email:** brandon@nuclea.solutions

## Main Updates
- A configuration of NVIDIA drivers was done along with the kernel to find one that satisfied the requirements of NVIDIA’s Video Search and Summarization.
- The Video Search and Summarization documentation was followed step-by-step and in detail to run it in helmet mode, but in this mode we realized that a much more powerful GPU than the one we have is needed, as well as much more RAM. Specifically, the following error occurred:
Detected NVIDIA GeForce RTX 5070 Ti GPU, which is not yet supported in this version of the container ERROR: No supported GPU(s) detected to run this container
It was specified that the compatible GPUs range from H200 up to A100.
- Seeing that helmet mode requires those configurations and that specific hardware, it was decided to opt for using Docker Compose to have a more customized configuration for our hardware. In this case, we used remote APIs like OpenAI for the LLMs and VLMs, and a Neo4j database which we managed to run correctly. More configurations are still needed in the Docker setup to run the VSS UI and be able to run it completely. I also think we will need an Azure OpenAI API key, which it seems to be using.
  ![image](https://github.com/user-attachments/assets/afe2abea-4e7e-4721-af06-316cf217efc6)

# Activity Report - 11/06/2025

**Email:** brandon@nuclea.solutions

## Main Updates
- Tests were conducted with Nvidia’s Video Search and Summarization (VSS) to try it using the resources of Zeus’s own computer. Lighter LLM and VLM models were used to allow analysis with our hardware, but due to library incompatibilities, the test could not be successfully completed.
- The VSS Docker on Zeus’s computer was reconfigured from scratch to allow remote use of the LLM and VLM models, avoiding the full resource load on the machine. The OpenAI API key was used, and testing with Azure OpenAI is still pending. All backend modules loaded correctly, but an error occurs when launching the frontend, which I haven’t yet figured out how to fix in order to analyze video and RTSP camera streams.

# Activity Report - 12/06/2025

**Email:** brandon@nuclea.solutions

## Main Updates
- With the corresponding API keys to use the LLM and VLM models from OpenAI, and after updating libraries, drivers, and repositories for the graphics card of the computer Zeus, we were able to successfully run the UI of NVIDIA's Video Search and Summarization technology. Within it, we managed to link some of our pre-recorded videos from Fimex's cameras for analysis and subsequently generate a summary from them.
- Unfortunately, even though the UI displays correctly and the backend is running properly, when making a query or asking something about the video, it gets stuck loading indefinitely and does not return any result, even though the console does not show any specific error.
  ![image](https://github.com/user-attachments/assets/ec018b20-d5c0-4ee2-88dc-9f0fbbb6f4cf)
- A new configuration will be attempted, using basic LLM and VLM models to be able to run everything locally and fully leverage the resources of the Zeus computer.

# Activity Report - 13/06/2025

**Email:** brandon@nuclea.solutions

## Main Updates
- Tests and library/model reconfigurations were carried out to better utilize NVIDIA’s Video Search and Summarization, since leaving all processing to be done remotely takes too long—even analyzing a simple 1-minute video segment becomes slow.
- So, a combination of local and remote processing was implemented to significantly reduce load times. Unfortunately, the following error occurred in the Guardrails module, and I have not yet been able to find a solution: 
  ``via-server-1  | 2025-06-14 02:50:19,117 ERROR Failed to load VIA stream handler - Guardrails failed
via-server-1  | Traceback (most recent call last):
via-server-1  |   File "/opt/nvidia/via/via-engine/via_server.py", line 1368, in run
via-server-1  |     self._stream_handler = ViaStreamHandler(self._args)
via-server-1  |   File "/opt/nvidia/via/via-engine/via_stream_handler.py", line 409, in __init__
via-server-1  |     self._create_llm_rails_pool()
via-server-1  |   File "/opt/nvidia/via/via-engine/via_stream_handler.py", line 516, in _create_llm_rails_pool
via-server-1  |     raise Exception("Guardrails failed")
via-server-1  | Exception: Guardrails failed
via-server-1  | 
via-server-1  | During handling of the above exception, another exception occurred:
via-server-1  | 
via-server-1  | Traceback (most recent call last):
via-server-1  |   File "/opt/nvidia/via/via-engine/via_server.py", line 2880, in <module>
via-server-1  |     server.run()
via-server-1  |   File "/opt/nvidia/via/via-engine/via_server.py", line 1370, in run
via-server-1  |     raise ViaException(f"Failed to load VIA stream handler - {str(ex)}")
via-server-1  | via_exception.ViaException: ViaException - code: InternalServerError message: Failed to load VIA stream handler - Guardrails failed
via-server-1  | Killed process with PID 68``

# Activity Report - 17/06/2025

**Email:** brandon@nuclea.solutions

## Main Updates
- A meeting was held with Lalo to better understand why the SSL error was occurring when running VSS locally on the Zeus computer. We couldn't find the exact cause of the error, but we came up with the idea of running tests using NVIDIA's notebooks.
- When testing on NVIDIA's notebooks, everything worked perfectly with the same configuration used on Zeus, so we continued analyzing other videos with summaries and questions in the chat.
- Finally, I decided to reconfigure the NVIDIA Video Search and Summarization setup from scratch on the Gaia computer, and interestingly, it worked perfectly there. I was able to analyze individual MP4 videos and even the live stream from Nuclea's office camera. Although the summaries were generated for the camera stream, the video itself wasn’t displayed — but in the end, the NVIDIA VSS service was successfully executed.
  ![image](https://github.com/user-attachments/assets/0c4d030f-b5e3-4219-904a-33a2f25ac715)
  
