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
