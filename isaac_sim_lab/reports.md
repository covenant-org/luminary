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
