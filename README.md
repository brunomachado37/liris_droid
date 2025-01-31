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
###  A) Data collection / teleoperation

TODO : explain the process of data collection

###  B) Dataset conversion HDF5 to RLDS format

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
In order to adapt the dataset from HDF5 format to the RLDS format used in [Open-X dataset](https://robotics-transformer-x.github.io/) (for example), you need to perform the following steps:
#### a. Convert videos from .svo to .mp4
/!\ Ensure you have installed a version of ZED SDK between `>=3.8 & <4.1` in order to perform the following.
For the dataset directory, it is recommanded to create a `data` folder in the top-level of the repo where you either store directly the `success/failure` folders or just symlink them to perform the conversion.

All the videos of the dataset are recorded as `SVO` files, which is a format from ZED cameras. It is required to convert the video of each trajectory from `.svo` to `.mp4`. You'll have to call the following script in order to do so:
```
python scripts/convert/svo_to_mp4.py \
    --lab="<Your_lab_name>" \
    --data_dir="<Path to the success/failure data folder>" \
    --lab_agnostic=False  \
    --do_index=True \
    --do_process=True \
    --process_failures=False \
    --extract_MP4_data=True \
    --extract_depth_data=False \
    --start_date="2025-01-30" \
    --end_date="2025-01-31" \
    --num_cameras=2 \
    --fps=25
```
Check the parameters for your own use inside of the `svo_to_mp4.py` script.

#### b. Convert dataset to TFDS
A tfds dataset builder is already created under `scripts/droid_dataset_builder/droid` inside a modified fork. You can modify it to your own needs.
For example, the `scripts/droid_dataset_builder/droid/droid.py` file needs to be changed by updating the `DATA_DIR` value to the path to your dataset.
Two other important parameters needs to be set to adapt to your machine : `N_WORKERS` and `MAX_PATHS_IN_MEMORY` inside of the `Droid` class 

Then, when everything is correct, execute the following:
```
cd scripts/droid_dataset_builder/droid &
tfds build --overwrite
```
/!\ The dataset will be stored in `~/tensorflow_datasets/droid` folder, ensure no dataset was already present in order to not overwrite it. Otherwise, copy-past it somewhere else. 

If you encounter a `CUDA error: Failed call to cuDeviceGet: CUDA_ERROR_NOT_INITIALIZED: initialization error` error, launch the following command to pass the processing into the CPU : `CUDA_VISIBLE_DEVICES="" tfds build --overwrite`

Your dataset is now ready, let's visalize it to verify the content.

### C) Dataset visualization
TODO : create a visualization tool as in HF LeRobot. 


