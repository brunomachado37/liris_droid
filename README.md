# The DROID Robot Platform

This repository contains the code for setting up your DROID robot platform and using it to collect teleoperated demonstration data. This platform was used to collect the [DROID dataset](https://droid-dataset.github.io), a large, in-the-wild dataset of robot manipulations.

If you are interested in using the DROID dataset for training robot policies, please check out our [policy learning repo](https://github.com/droid-dataset/droid_policy_learning).
For more information about DROID, please see the following links: 

[**[Homepage]**](https://droid-dataset.github.io) &ensp; [**[Documentation]**](https://droid-dataset.github.io/droid) &ensp; [**[Paper]**](https://arxiv.org/abs/2403.12945) &ensp; [**[Dataset Visualizer]**](https://droid-dataset.github.io/dataset.html).

![](https://droid-dataset.github.io/droid/assets/index/droid_teaser.jpg)

---------
## Setup Guide

We assembled a step-by-step guide for setting up the DROID robot platform in our [developer documentation](https://droid-dataset.github.io/droid).
This guide has been used to set up 18 DROID robot platforms over the course of the DROID dataset collection. Please refer to the steps in this guide for setting up your own robot. Specifically, you can follow these key steps:

1. [Hardware Assembly and Setup](https://droid-dataset.github.io/droid/docs/hardware-setup)
2. [Software Installation and Setup](https://droid-dataset.github.io/droid/docs/software-setup)
3. [Example Workflows to collect data or calibrate cameras](https://droid-dataset.github.io/droid/docs/example-workflows)

If you encounter issues during setup, please raise them as issues in this github repo.

---------
## Single PC Software Setup

- The overall setup is quite similar to the original, so you can mostly follow the tutorial above for the software setup.

- You will need to run your Ubuntu with a real-time kernel. If that is not the case on your machine, follow the instructions for configuring it in the NUC setup.

- The network configuration is quite simple. You just need to setup your machine to have a static IP address in the same network as the Franka. (e.g. robot ip: 192.168.10.100, your IP 192.168.10.X)

- The oculus APK and setup, docker instalation, and x11 forwarding configuration should be performed just like in the laptop setup.

---------
## Running application

1. **Franka**

- Turn on the Franka. Once it is on, the base should be yellow, meaning the robot is locked. Open the desk UI in a browser, by typing the robot ip slash desk (e.g. 192.168.10.100/desk/).

- In the desk interface, unlock the robot joints. The lights on the robot's base should be blue.

- Also in the desk interface, activate FCI.

- *Troubleshooting:* If you can't access the desk, try it with a different browser and check ubuntu network settings to be sure you are connected to the same network as the robot with a static IP (e.g. 192.168.10.4). Note that the computer will usually have at least 2 network boards, one to connect to the robot and another to connect to the internet.

2. **Oculus Quest 2**

- Turn on the Oculus Quest 2 and make sure it is connected to the computer.

- Type `adb devices` on a terminal and check if the oculus is connected. It will appear as "no permissions". 

- Put on the oculus and check the notifications. Authorize USB debugging. Now on `adb devices` it should show as "device".

- *Troubleshooting:* If server is not working, open a terminal on the host machine and execute:
```
adb kill-server
adb start-server
```

3. **Zed Cameras**

- Check if both cameras are connected on **USB 3.0** ports. See if they both appear on cheese. 

- *Troubleshooting:* If cameras don't appear, execute on a terminal:
```
python -c "exec(\"import pyzed.sl as sl\nprint(sl.Camera.get_device_list())\")"
```

- If one of the cameras show as "NOT AVAILABLE", try to disconnect and re-connect them from the PC.

4. **Launch the application**

- To launch the main application use:
```
docker compose -f .docker/single_pc/docker-compose-single_pc.yaml up
```

- If you want to re-build the docker or is the first time running it:
```
docker compose -f .docker/single_pc/docker-compose-single_pc.yaml build
```

- You can also run a bash inside the container, to run different scripts or tests:
```
docker compose -f .docker/single_pc/docker-compose-single_pc.yaml run single_pc bash
```

