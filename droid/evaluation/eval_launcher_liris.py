import json
import os
import numpy as np
import torch
import cv2
import hydra

from droid.controllers.oculus_controller import VRPolicy
from droid.robot_env import RobotEnv
from droid.user_interface.data_collector import DataCollecter
from droid.user_interface.gui import RobotGUI


def eval_launcher(config):
    # Prepare Log Directory #
    dir_path = os.path.dirname(os.path.realpath(__file__))
    log_dir = os.path.join(dir_path, "../../evaluation_logs", config.exp_name)

    # Set Random Seeds #
    torch.manual_seed(config.seed)
    np.random.seed(config.seed)

    policy = hydra.utils.instantiate(config.algo.policy)

    camera_kwargs = dict(
        hand_camera=dict(image=True, concatenate_images=False),
        varied_camera=dict(image=True, concatenate_images=False),
    )
    
    policy_camera_kwargs = {}
    policy_camera_kwargs.update(camera_kwargs)

    env = RobotEnv(
        action_space=config.algo.action_space,
        gripper_action_space=config.algo.gripper_action_space,
        camera_kwargs=policy_camera_kwargs
    )
    controller = VRPolicy()

    # Launch GUI #
    data_collector = DataCollecter(
        env=env,
        controller=controller,
        policy=policy,
        save_traj_dir=log_dir,
        save_data=config.save_data,
    )
    RobotGUI(robot=data_collector)
