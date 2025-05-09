# 27/03/2025
- Installed and configured Ubuntu 20.04 on local laptop with another ssd (dual boot, dual drive)
- Got most of the requirements for Isaac Sim ( lacking VRAM (6.4 -> 8) and RAM (14.4 -> 32 ))
- Installed Isaac Sim
## Todo: 
- Start testing and exploring program

# 28/03/2025
- Installed Isaac Lab
- Made first tests
- Quick start with robotic arm and solid cube
- Got performance issues:
- "Isaac Sim is not responding" multiple times
- High RAM usage (300 Mb left)
- OS frozen multiple times
## Todo: 
- Check if there's a way to increase performance
- Keep testing

# 31/03/2025
- Installed Nvidia SDK Manager & Docker
- Tests of tutorials in Isaac Sim
- Worked well in GUI
- Problems in interaction with python scripts
- Message appearing when trying hot reload in vs code python script: 
```
2025-04-01 03:13:59 [361,373ms] [Error] [asyncio] Task exception was never retrieved
future: <Task finished name='Task-1922' coro=<BaseSampleUITemplate._on_load_world.<locals>._on_load_world_async() done, defined at /home/vicman/isaacsim/exts/isaacsim.examples.interactive/isaacsim/examples/interactive/base_sample/base_sample_extension.py:107> exception=NameError("name 'np' is not defined")>
Traceback (most recent call last):
  File "/home/vicman/isaacsim/exts/isaacsim.examples.interactive/isaacsim/examples/interactive/base_sample/base_sample_extension.py", line 108, in _on_load_world_async
    await self._sample.load_world_async()
  File "/home/vicman/isaacsim/exts/isaacsim.examples.interactive/isaacsim/examples/interactive/base_sample/base_sample.py", line 43, in load_world_async
    self.setup_scene()
  File "/home/vicman/isaacsim/exts/isaacsim.examples.interactive/isaacsim/examples/interactive/hello_world/hello_world.py", line 33, in setup_scene
    position=np.array([0, 0, 1.0]), # Using the current stage units which is in meters by default.
NameError: name 'np' is not defined

```
- Last logs when trying to run ```sudo ./python.sh standalone_examples/api/isaacsim.simulation_app/hello_world.py```

```
2025-04-01 03:12:09 [9,676ms] [Warning] [rtx.scenedb.plugin] SceneDbContext : TLAS limit buffer size 8448000128
2025-04-01 03:12:09 [9,676ms] [Warning] [rtx.scenedb.plugin] SceneDbContext : TLAS limit : valid false, within: false
2025-04-01 03:12:09 [9,676ms] [Warning] [rtx.scenedb.plugin] SceneDbContext : TLAS limit : decrement: 167690, decrement size: 8363520384
2025-04-01 03:12:09 [9,676ms] [Warning] [rtx.scenedb.plugin] SceneDbContext : New limit 8508328 (slope: 503, intercept: 13181056)
2025-04-01 03:12:09 [9,676ms] [Warning] [rtx.scenedb.plugin] SceneDbContext : TLAS limit buffer size 4286378240
2025-04-01 03:12:09 [9,676ms] [Warning] [rtx.scenedb.plugin] SceneDbContext : TLAS limit : valid true, within: true
2025-04-01 03:12:09 [9,855ms] [Warning] [omni.usd-abi.plugin] No setting was found for '/rtx-defaults-transient/meshlights/forceDisable'
2025-04-01 03:12:09 [9,911ms] [Warning] [omni.usd-abi.plugin] No setting was found for '/rtx-defaults/post/dlss/execMode'
./python.sh: line 41: 55718 Killed                  $python_exe "$@" $args
There was an error running python
```
- Not obvious reason atm

# 1/04/2025
- Solved errors from yesterday
- There was no clear reason at all
- Most likely something went wrong during Isaac Lab instalation
- Solution was to reinstall
- Made other tutorials in nvidia page
- Got performance errors in some of them
- Likely cause: Limited VRAM memory in GPU

# Activity Report - 01/04/2025

**Email:** brandon@nuclea.solutions

## Main Updates
- Watched all Multi-Camera Tracking tutorials from Nvidia: [Nvidia On-Demand](https://www.nvidia.com/en-us/on-demand/playlist/playList-62b777fa-766f-4773-8ae4-a70e564d7848/)
- Reinstalled Ubuntu 22.04, Isaac Sim, libraries, and drivers to prevent compatibility issues and ensure a clean work environment
- Encountered issues during initial tracking tests in Isaac Sim, which led me to decide to reinstall everything.

  # Activity Report - 02/04/2025

**Email:** brandon@nuclea.solutions

## Main Updates
- An attempt was made to create a virtual machine in Google Cloud Console using Compute Engine, but the following service errors occurred:
  ```
  A n1-standard-4 VM instance with 1 nvidia-tesla-t4 accelerator(s) is currently unavailable in the us-central1-f zone. Alternatively, you can try your request again with a different VM hardware configuration or at a later time. For more information, see the troubleshooting documentation.
  ```
- An attempt was made to resolve the error by selecting different hosting zones and various server characteristics, but unfortunately, none were successful.
  ![image](https://github.com/user-attachments/assets/51068fb5-9b9e-46fe-98f7-35c5f1bb7a78)

- Another test will be attempted with AWS to see if it works there.

# 2/04/2025
@VicmanGT
- Tested different included examples and tutorials in isaacsim packate
- Got import errors in examples that tried to use clases defined in other folders
- Exmaples that didnt' do that worked correctly
- Got initialization error while trying to launch isaac-sim:
```
[Error] [carb.cudainterop.plugin] CUDA error 999: cudaErrorUnknown - unknown error)
[Error] [carb.cudainterop.plugin] Failed to query CUDA device count.
[Error] [carb.cudainterop.plugin] Could not query CUDA device.
```
- Got temporarly solved by rebooting Ubuntu
- Not apparent cause yet.
- Error seen in Nvidia Forum:
- https://forums.developer.nvidia.com/t/cuda-error-999-failed-to-query-cuda-device-count-cuda-deviceordinal-is-invalid/274493

  # Activity Report - 03/04/2025

**Email:** brandon@nuclea.solutions

## Main Updates
- Successfully launch and configure a virtual machine on AWS without encountering server issues or GPU availability limitations by region.
- The NVIDIA drivers with CUDA and other libraries were installed to configure Metropolitan NVIDIA.
- An attempt was made to configure Metropolitan NVIDIA using Docker, but the following authorization error occurred:
  ```
   sudo docker login nvcr.io
  Username: $oauthtoken
  Password:
  WARNING! Your password will be stored unencrypted in /root/.docker/config.json.
  Configure a credential helper to remove this warning. See
  https://docs.docker.com/engine/reference/commandline/login/#credentials-store
  
  Login Succeeded
  ubuntu@ip-172-31-5-186:~$ sudo docker pull nvcr.io/nvidia/metropolis/metropolis:v1.0
  Error response from daemon: Head "https://nvcr.io/v2/nvidia/metropolis/metropolis/manifests/v1.0": denied: {"errors": [{"code": "DENIED", "message": "Access Denied"}]}
  ubuntu@ip-172-31-5-186:~$ sudo docker pull nvcr.io/nvidia/metropolis/metropolis:v1.0
  Error response from daemon: Head "https://nvcr.io/v2/nvidia/metropolis/metropolis/manifests/v1.0": denied: {"errors": [{"code": "DENIED", "message": "Access Denied"}]}
  ```
- I used DeepStream SDK as an alternative to Docker to perform intelligent video analysis.
- I will look for a way to install it tomorrow using a Docker container for only the VTS service.

# 03/04/2025
@VicmanGT
- Check tutorials and examples from Nvidia Isaac Sim docs page
- Started reviewing examples from cameras in the simulation
- Printed frames into console and generated images from frames with opencv
- Combined examples from a robot (car and arm ) simulation and a camera implementation, worked nicely

## Todo: 
- Get video from simulation using camera 
- Check how to put multiple cameras and get data from them
- Implement in other examples

  # Activity Report - 04/04/2025

**Email:** brandon@nuclea.solutions

## Main Updates
- It was successfully installed and configured DeepStream on the server.
- A configuration file was created for DeepStream so that it could run a video through VST.
- The video ran correctly, but I have the problem of not being able to visualize it since I'm connected via SSH.
  ```
  ubuntu@ip-172-31-5-186:/opt/nvidia/deepstream/deepstream-7.1/samples/configs/deepstream-app$ deepstream-app -c config_file.txt
  ** WARN: <parse_source:675>: Unknown key 'width' for group [source0]
  ** WARN: <parse_source:675>: Unknown key 'height' for group [source0]
  
  Runtime commands:
          h: Print this help
          q: Quit
  
          p: Pause
          r: Resume
  
  ** INFO: <bus_callback:291>: Pipeline ready
  
  Failed to query video capabilities: Invalid argument
  ** INFO: <bus_callback:277>: Pipeline running
  
  nvstreammux: Successfully handled EOS for source_id=0
  ** INFO: <bus_callback:334>: Received EOS. Exiting ...
  
  Quitting
  App run successful
  ```
- Find a way to display the VST UI.

# 04/04/2025
@VicmanGT
- Checked humanoids example
- Added multiple cameras to simulation in different positions and orientations
- Got frames from all of them each a certain amount of time
- Converted frames into iamges and store them in file system
- Camera 1 first frame
![1_camera1_opencv](https://github.com/user-attachments/assets/37a655b8-9a6f-457b-8918-6f55e2169369)
- Camera 2 first frame
![1_camera2_opencv](https://github.com/user-attachments/assets/c830fc73-fcd9-4da5-9d71-31189e2571df)
- Camera 3 first frame
![1_camera3_opencv](https://github.com/user-attachments/assets/b8ab076d-149b-45d7-a03e-695e8c27d0c5)
- Camera 1 second frame
![2_camera1_opencv](https://github.com/user-attachments/assets/3d6fab01-d803-4fa3-b8d0-ef112d9e459a)
- Camera 2 second frame
![2_camera2_opencv](https://github.com/user-attachments/assets/0c2bcca4-58dd-45c6-a429-9aea0cde91e1)
- Camera 13 second frame
![2_camera3_opencv](https://github.com/user-attachments/assets/bd2c523e-719f-428e-9a55-be0f5a101ebf)

## Todo: 
- Modify humanoid movement to they don't fall that quick

 # Activity Report - 07/04/2025

**Email:** brandon@nuclea.solutions

## Main Updates
- The DeepStream configuration for running MP4 videos has been completed. It runs smoothly, although the interface has not yet been viewed.

- The setup for running videos via the RTSP protocol in DeepStream has begun, but it is not yet ready due to the lack of a graphics engine with NVIDIA's TensorRT library, which is used for optimizing and running neural networks on GPUs.
![image](https://github.com/user-attachments/assets/b3f1e0b5-b0fb-49e4-a1fc-dfcb1bb0f78a)

- The plan is to follow the quick start guide for multi-camera simulation with AWS, from: [Multi_Camera_Sim2Deploy_AWS](https://docs.nvidia.com/mms/text/Multi_Camera_Sim2Deploy_AWS.html)

# 07/04/2025
@VicmanGT
- Implemented 3 cameras in different position in humanoid simulation
- Got 1 fps from all of them and were saved in different folders
- Used numeric keyboard to move the humanoids throughout the space ( now modified to warehouse environment )
- Simulation Results (5x vel):

https://github.com/user-attachments/assets/857a68e0-6a97-43a5-8a4b-a65aecdfccd5

- Cameras frames:

https://github.com/user-attachments/assets/37780be7-548c-43ed-ba8e-8d2b6116535b

https://github.com/user-attachments/assets/055b8177-7941-450b-abac-d18915dcbd03

https://github.com/user-attachments/assets/f38c2686-e087-4d51-bd08-f0ae348baad8

- Got some issues with slowness of the simulation and response time from the keyboard input, posible cause the frame capture
- Neither RAM or VRAM seem an cause

# 08/04/2025
@VicmanGT
- Implemented RF-DETR algorithm on code to make predicions on the detected frames for each camera
- GitHub Repo: https://github.com/roboflow/rf-detr
- Save the images with surrounding boxes with predictions
- Got errors while trying this:
```
  Error] [omni.ext._impl.custom_importer] Failed to import python module omni.kit.widget.options_menu. Error: No module named 'omni.kit.widget'
```
- This after making a ```./python.sh -m pip install rfdetr``` to install the library to use the model
- The error message was showed in console for almost every ```omni``` dependent package
- Ran ```./post_install.sh``` after rebooting system
- New error was this:
  ```
  [Error] [carb.scripting-python.plugin] FileNotFoundError: [Errno 2] No such file or directory: '/home/vicman/isaacsim/exts/omni.pip.compute/pip_prebundle/cv2'
  At:
    /home/vicman/isaacsim/kit/kernel/py/omni/ext/_impl/fast_importer.py(261): _fast_walk
  ```
- Neither the application of any of the examples from isaac sim worked due to the same error
- Couldn't yet find a quick solution in the web

# Todo: 
- Reinstall Isaac Sim from scratch
- Check installed python libraries with  ```./python.sh -m pip list``` before and after trying to install the ```rfdeter```

 # Activity Report - 09/04/2025

**Email:** brandon@nuclea.solutions

## Main Updates
- Early access was requested from NVIDIA through an official application to use their new AI models and camera tracking technologies, such as NVIDIA Metropolis. I am currently waiting for approval.
![image](https://github.com/user-attachments/assets/22eba68c-ff38-463e-80f9-f64dbd7196c0)

- Two work plans were developed to extract video footage from HikVision cameras. The first plan involves downloading videos locally via RTSP using the FFmpeg library. A Python script was created to manage all registered cameras listed in a CSV file. The recording duration is customizable, and using cron jobs and system services, we can schedule the script to run at specific times of the day.
![image](https://github.com/user-attachments/assets/26ba5144-9e2c-4c90-9b22-75390956852b)

- The second plan builds on the first but differs in that instead of storing the videos locally, the footage is uploaded directly to a cloud storage solution such as an AWS S3 bucket.

- Tomorrow, we will begin testing with the actual Fimex cameras and evaluate the strategy of also using an SFTP server to store all videos, which will later be processed using NVIDIA Metropolis.

# 09/04/2025
@VicmanGT
- Reinstalled Isaac Sim and the problem from yesterdy solved, even after installiing de library for the RF-DETR
- Correctly implemented RF-DETR algorithm
- Correctly saved frames with bounding boxes of predicitons
- Improved performance of simulation by lowering the resolution of the cameras (full hd -> hd)
- Moved camera positions to get them to capture a wider space
- Implemented an option to choose between automated simulation of manual control with the numpad
- Started coding the algorithm to detect movement
- Results of simulation:

https://github.com/user-attachments/assets/2f4ab757-2c00-4ba6-847a-94ed0731e8e0

- Result frames with predicitons

https://github.com/user-attachments/assets/0ff68486-a04d-4fbf-9df4-60e08fe3807f

https://github.com/user-attachments/assets/85516f4c-dab2-4da7-a751-920e4efccdc5

## Todo: 
- The RF-DETR algorithm had problems to identify the humanoids, labeling them as other objects when they were even detected
- This could be mainly due to the not human like texture they have, so try to find if there's another texture to cover them
- Check another object detection algorithm such as YOLO to compare performance and scores
- Implement the move alert function
- Figure out how to mantain some form of consistency during the frames passed

## Notes: 
- Got this error message some times while trying to run the python script
```
Inconsistency detected by ld.so: ../elf/dl-tls.c: 517: _dl_allocate_tls_init: Assertion `listp != NULL' failed!
There was an error running python
```
- The problem solved trying 2 or 1 more time, no obvious reason atm

# Activity Report - 10/04/2025

**Email:** brandon@nuclea.solutions
@VicmanGT

## Main Updates
- Today, I visited the Fimex factory and worked with Víctor on configuring and extracting video footage from the production cameras, then streaming it via RTSP to the AWS EC2.
- Checked the stream via VLC, however this was only possible in Brandon's personal computer most likely because some specific configuration on the Local Fimex computer.
- It did work one time on the Local Fimex computer but after changing the camera in the python script, the connection was unable to be setted again, the reason behind this it's still not clear.
- We also left the local Fimex computer connected to TeamViewer, so we can access it remotely in the future for further configuration.

# Activity Report - 11/04/2025

**Email:** brandon@nuclea.solutions

## Main Updates
- A basic GUI was downloaded and configured for the AWS EC2 server, and a successful connection was made from a Windows client machine using VNC.
  ![image](https://github.com/user-attachments/assets/ba528233-23b5-4b30-acd5-e41a2f78b674)

- A daemon service was created so that, upon starting or restarting the server, the mediamtx service would automatically start and run, enabling the reception of video from the RTSP cameras.
- A VPN called Kerio was downloaded and configured on the virtual machine to establish a connection between the server and the local Fimex computer.
![image](https://github.com/user-attachments/assets/6ef47ec7-2bf9-4525-92ac-a7fdfbbb711b)

- A visit was made to Cumbres to perform a drone flight test.

# 11/04/2025
@VicmanGT
- Went to Cumbres school to help install and configure a sensor to better measure the distance from the ground
- Helped performed basic flight operation

# Activity Report - 14/04/2025

**Email:** brandon@nuclea.solutions

## Main Updates
- Once the VPN was correctly installed and configured on the EC2 server, a service was also created to enable it and connect automatically to the Fimex server every time the server starts.

- A service was created so that VNC would start automatically when Linux boots, allowing us to access the graphical interface without having to activate it manually.

- It was possible to ping the IP address 172.16.3.122, and the camera stream could already be viewed using the ffplay command.
  ![image](https://github.com/user-attachments/assets/941a9674-cd8a-4e63-ac20-b4f2331a6edf)
  ![image](https://github.com/user-attachments/assets/2c27eb72-acce-4f45-878b-b426bd0766b9)
- It will be investigated how to save short video locally to process it on the EC2 server.

# 14/04/2025
@VicmanGT
- Coded a movement alert function that prints to the console when the centroid of a box prediction moves more that a certain threshold
- Included logging info to know when the new object are detected, not longer detected or the classs of the prediction changed
- Also when there are no predictions for the image
- All this for each camera
  
https://github.com/user-attachments/assets/be6eac17-51a7-4254-bc91-5e1aee0add30


- Implemented YOLOv11 model to make predictions on frames

## Todo: 
- Check how to process the outputs of YOLOv11 to draw the rectangles on the image
- Adapt function to process the output of YOLOv11

  # Activity Report - 15/04/2025

**Email:** brandon@nuclea.solutions

## Main Updates
- Some issues were fixed during the VPN initialization that were preventing it from properly connecting to the Fimex server.
- After successfully configuring the VPN to access all camera streams from Fimex, a Python script was developed to extract specific segments of the live feed and save them locally on the computer.
  ![image](https://github.com/user-attachments/assets/ba3c9a23-3abf-4aaf-b5ee-c2ea8084ce72)
  ![image](https://github.com/user-attachments/assets/a07dd569-bb52-4832-a51d-3b16e876fb69)

- The script will be improved to analyze each of the extracted videos for camera tracking. A more local solution will be implemented, without using NVIDIA Metropolis, since access to the platform has not yet been granted.

# 15/04/2025
@VicmanGT
- Created repo to have version control in isaac sim code
- Completely implemented YOLOv11 algorithm to make predictions for the isaac sim simulation
- Assigned camera 2 to this
- Tests results:
- The YOLO algorithm performed worse than the RFDE, since in most of the frames none of the humanoids were detected
- Therefore no moment whatsoever

https://github.com/user-attachments/assets/e668101a-0287-4461-b6dc-8672fbc261bc

- Tested movement alert function in local webcam to check with "real person movement" worked nicely

https://github.com/user-attachments/assets/419b049d-e30c-460f-8943-aa1d6a6a3602

## Todo: 
- Apply filter for person class and counting

# 16/04/2025
@VicmanGT
- Divided humanoid simulation file into modules for more comfortable development
- Added named paratemer to script to select the model to use (rf-dert or yolo)
- IsaacSim code stop working in local computer
- Got same error as in the 8/04/2025 but the procedure didn't work now
- Not custom humanoids simulation app or any of the examples are running:
- Last logs before shooting down app:
```
2025-04-17 01:31:37 [10,558ms] [Warning] [rtx.scenedb.plugin] SceneDbContext : TLAS limit buffer size 8448000128
2025-04-17 01:31:37 [10,558ms] [Warning] [rtx.scenedb.plugin] SceneDbContext : TLAS limit : valid false, within: false
2025-04-17 01:31:37 [10,558ms] [Warning] [rtx.scenedb.plugin] SceneDbContext : TLAS limit : decrement: 167690, decrement size: 8363520384
2025-04-17 01:31:37 [10,558ms] [Warning] [rtx.scenedb.plugin] SceneDbContext : New limit 8508328 (slope: 503, intercept: 13181056)
2025-04-17 01:31:37 [10,558ms] [Warning] [rtx.scenedb.plugin] SceneDbContext : TLAS limit buffer size 4286378240
2025-04-17 01:31:37 [10,558ms] [Warning] [rtx.scenedb.plugin] SceneDbContext : TLAS limit : valid true, within: true
2025-04-17 01:31:38 [10,757ms] [Warning] [omni.usd-abi.plugin] No setting was found for '/rtx-defaults-transient/meshlights/forceDisable'
2025-04-17 01:31:38 [10,854ms] [Warning] [omni.usd-abi.plugin] No setting was found for '/rtx-defaults/post/dlss/execMode'
./python.sh: line 41: 16648 Killed                  $python_exe "$@" $args
There was an error running python
```
- Get frozen while trying to run then suddenly stops
- IsaacSim App selector works ok

## Todo: 
- Check RAM and VRAM usage while trying to run a script
- Check other versions

  # Activity Report - 21/04/2025

**Email:** brandon@nuclea.solutions

## Main Updates
- Tests were conducted with the cameras to extract videos from Fimex.
- A new VNC service was enabled to allow faster and more efficient access to the server.
- A service was created to retry the VPN connection to prevent potential data leaks and to improve video retrieval from the cameras.
- A solution will be explored to extract all videos from all cameras via streaming and store them in a bucket with a UI to view the streams simultaneously.

  # Activity Report - 22/04/2025

**Email:** brandon@nuclea.solutions

## Main Updates
- A Python script was created to display the streaming of the 20 cameras connected in Fimex through a simple UI.
  ![image](https://github.com/user-attachments/assets/dc7d7e4b-338e-4c9c-b1ba-a1b8c1bbded0)

- Another script was developed to continuously save the camera streams to an AWS S3 bucket. Whether the recording day ends or the script is interrupted due to an error, the recorded footage up to that point is saved automatically.
- A Linux service was configured to ensure the script runs automatically at all times, without the need for manual startup.
- The setup of a local computer with a 5070 graphics card will begin, aiming to eliminate the need for using AWS EC2 instances.

# 22/04/2025
@VicmanGT
- Tested custom models with the people counting function and the movement alert:
- best.pt

https://github.com/user-attachments/assets/8ae3f7ba-64e9-4b74-9b0e-67b2b45cc418

- NucleaDrone-v14-2Class.pt

https://github.com/user-attachments/assets/32f82b47-f2f7-4d12-9719-09a25f5dac72

- Both models got similar results
- Only minor difference is that best.pt is faster and therefore better and keeping track of people when do fast movements

# 23/04/2025
@VicmanGT
- Cloned metropolis-dev repository into ec2 server to access compute there 
- Made predictions in videos of Fimex with rfde-tf, custom models best.pt and NucleaDrone-v14-2Class.pt
- The rf-detr permormed well both at counting and the interaction with the movement_alert

https://github.com/user-attachments/assets/e4544a9c-d994-498d-8d65-57ae532acdf7

- The tests made with both best.pt and NucleaDrone-v14-2Class.pt seemed to have less accuracy when detecting people, and only outputed one person in each frame
## Todo: 
- Check what is happening there

# Activity Report - 24/04/2025

**Email:** brandon@nuclea.solutions

## Main Updates
- The local Nuclea computer with an Nvidia 5070 graphics card was configured to access the Fimex cameras.
- VPN and VNC services were created to enable access to the FSTP video from the cameras.
- A script was created to run automatically and locally save the video stream from 20 cameras on the computer.

# 24/04/2025
@VicmanGT 
- Corrected script to get better predictions from custom models best.pt and NucleaDrone-v14-2Class.pt
- Tested with videos saved from Fimex cameras
- best.pt

 https://github.com/user-attachments/assets/4187d91b-af04-4b4d-a9da-73f096d703f7

- NucleaDrone-v14-2Class.pt

https://github.com/user-attachments/assets/15da1964-4ead-43fd-9658-97365a215acb

- Between the two custom models, best.pt got the better results being faster and more accurate
- When comparing best.pt with the rf-dert model, both provide good results with the main difference that best.pt sometimes detect more people in the frame however rf-dert got more consistent and stable predictions.

# Activity Report - 25/04/2025

**Email:** brandon@nuclea.solutions

## Main Updates
- The advanced configuration was completed for the Zeus computer to enable remote access to its operating system's UI via VNC.
  ![image](https://github.com/user-attachments/assets/becc8c76-f4d1-4bb8-97b2-6b0b34647f48)
- The Python script was improved to more efficiently detect recordings or streamings from the cameras simultaneously and correctly save the video output.
- The configuration of the Gaia computer is planned to be completed next, with the goal of enabling remote UI access and beginning the installation of software such as Isaac Sim and Isaac Lab.

# 25/04/2025
@VicmanGT
- Reestructured scripts in metropolis-dev repo into folders
- isaac_sim_lab, models ( custom models ), utils ( movement alert and function to annotate yolo detections), and video_analysis
- In video_analysis added separate scripts to test models in webcam and with a folder with videos

# Activity Report - 28/04/2025

**Email:** brandon@nuclea.solutions

## Main Updates
- The new 14TB hard drive was configured and partitioned for the Zeus computer, and a shortcut was created for this drive in the file explorer.
- The script for recording FIMEX cameras was modified to save all videos on the new hard drive.
- All the initial configurations for the Gaia computer were completed to enable access to the operating system's GUI via a VNC service. Additionally, basic programs such as Visual Studio Code, VLC, Google Chrome, and others were installed.
  ![image](https://github.com/user-attachments/assets/22bfd274-0db1-42f8-911b-17eccd385235)

# 28/04/2025
@VicmanGT
- Cloned local repository from metropolis-dev and adapted code in the Zeus computer for testing the movement alert in the recordings from Fimex
- Got following errors:
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
- Seemed like there isn't yet any Pytorch version that supports the installed GPU ```NVIDIA GeForce RTX 5070 Ti``` and therefore no models can be used
- This happens for both custom models and rf-detr
- Relevant links of same problem but using ComfyUI:
1. https://github.com/comfyanonymous/ComfyUI/issues/7127
2. https://github.com/comfyanonymous/ComfyUI/discussions/6643
- Solved by installing another pytorch version:
```
  pip install --pre torch torchvision --index-url https://download.pytorch.org/whl/nightly/cu128
```
Results: 
- Very similar to the ones made in the EC2 instance, however there were many videos that had a lot of noise that made the detections inaccurate and inconsistent
- Example:

https://github.com/user-attachments/assets/5ffefcec-4474-4f50-bb0e-d34da1fe724d

- But it seems like it's more of a problem of the cameras themselves.

# Activity Report - 29/04/2025

**Email:** brandon@nuclea.solutions

## Main Updates
- Isaac Sim and Isaac Lab from NVIDIA were downloaded and configured on the Gaia computer.
  ![image](https://github.com/user-attachments/assets/c7ef6658-3858-47db-8f47-4ec3409a4132)
- The first test of using the VST container on the Zeus computer for elk tracking with the office webcam was conducted.
- The VST Docker container runs correctly, but there is an issue where the UI does not display, even though no specific error is thrown. Further investigation is needed to find a way to launch it properly.
  ![image](https://github.com/user-attachments/assets/6693eeed-04f8-4efe-9389-94fe007eb558)


# 29/04/2025
@VicmanGT
- Started programming code for the Zeus server surveillance using webcam
- Face detection algorithms with a Cascade Classifier might be useful
- There are different types of configurations for the models managed in .xml files
- There were issues when the camera pointed to the side of the face instead of in the front, and in this case there was no prediction
- Relevant links:
- https://www.geeksforgeeks.org/face-detection-using-cascade-classifier-using-opencv-python/
- https://chatgpt.com/share/6811b087-52e0-800c-8bbc-b46e9086b737
- https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html

## Todo: 
- Find configuration file that can detect a face completely from the side
- Check another way to detect when some is using the computer server
- Pose Estimation, Fase Mesh, Eye tracking
- Test

# Activity Report - 30/04/2025

**Email:** brandon@nuclea.solutions

## Main Updates
- The Zeus computer was successfully configured to use NVIDIA NGC with access to all containers provided by NVIDIA Metropolis.
- The first Docker container for NVIDIA VST was downloaded and used.
- The UI was successfully displayed, although I still haven't found a way to connect the VST service to the local computer's webcam.
- It is necessary to investigate how to run the webcam over RTSP and connect it directly to the Docker container so it can detect it, and also check if it would work with access to the camera recordings from Fimex.

# 30/04/2025
@VicmanGT
- Found repository that already had implemented a face detection algorithm and was able to detect face from the profile
- Had some bugs but they're fixed now
- Modifications:
- Limit face detection to only the one that is closer to the camera by comparing the size of the bounding box
- Added threshold to see if the face was close enough, simulating it's using the computer server
- Filter by 'Right Profile' according to the accomodation of the webcam in the computer server so when it's detected, the code saved the frames and makes a video out of them
- Relevant links:
- https://github.com/nawafalageel/Side-Profile-Detection
- https://www.geeksforgeeks.org/python-opencv-capture-video-from-camera/

## Todo: 
- Check how to make multiple videos out of a single stream without the need to rerun the code

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

