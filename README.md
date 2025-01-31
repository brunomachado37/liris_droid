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
## Dataset creation
###  a) Data collection / teleoperation

TODO : explain the process of data collection

###  b) Dataset conversion HDF5 to RLDS format

Once the data is collected, it should be recorder in the volume `/app/data` indicated in the file `.docker/single_computer/docker-compose.yaml`. The folder contains success and failure recording of all the tasks sorted by dates of collection :
```
<data_dir>
├─ success
|   ├─ <YYYY>-<MM>-<DD> # Day of trajectory selection
|   |   ├─ <Day>_<Mon>_<DD>_<HH>:<MM>:<SS>_<YYYY> # Individual trajectory directory
|   |   |   ├─ trajectory.h5 # HDF5 file containing states, actions, camera data
|   |   |   └── recordings
|   |   |       └── SVO
|   |   |           ├─ <camera_1_id>.svo
|   |   |           └── <camera_2_id>.svo
|   |   ├─ ...
|   ├─ ...
└── failure
    ├─...

```
In order to adapt the dataset from HDF5 format to the RLDS format used in [Open-X dataset](https://robotics-transformer-x.github.io/) (for example), you need to do the following steps:
- Convert video of trajectories from `.svo` to `.mp4` by calling the script `svo_to_mp4.py`
- Use the conversion script `scripts/postprocess_rlds.py` to process all the converted data to create a RLDS dataset. Note: under the hood it uses the [DROID dataset builder repo](https://github.com/alexcbb/droid_dataset_builder) that is added as a submodule to this repo. 


### c) Dataset visualization
TODO : create a visualization tool as in HF LeRobot. 


