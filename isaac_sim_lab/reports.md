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

# Activity Report - 04/01/2025

**Email:** brandon@nuclea.solutions

## Main Updates
- Watched all Multi-Camera Tracking tutorials from Nvidia: [Nvidia On-Demand](https://www.nvidia.com/en-us/on-demand/playlist/playList-62b777fa-766f-4773-8ae4-a70e564d7848/)
- Reinstalled Ubuntu 22.04, Isaac Sim, libraries, and drivers to prevent compatibility issues and ensure a clean work environment
- Encountered issues during initial tracking tests in Isaac Sim, which led me to decide to reinstall everything.
