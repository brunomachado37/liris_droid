import os
from cv2 import aruco

# Robot Params #
nuc_ip = None
robot_ip = "192.168.10.100"
laptop_ip = "192.168.10.4"
sudo_password = "panda"
robot_type = "panda"  # 'panda' or 'fr3'
gripper_type = "franka" # 'franka' or 'robotiq'
robot_serial_number = "295341-1325717"

# Camera ID's #
hand_camera_id = "15483906"
varied_camera_1_id = "21555878"

# Charuco Board Params #
CHARUCOBOARD_ROWCOUNT = 9
CHARUCOBOARD_COLCOUNT = 14
CHARUCOBOARD_CHECKER_SIZE = 0.015
CHARUCOBOARD_MARKER_SIZE = 0.011
ARUCO_DICT = aruco.Dictionary_get(aruco.DICT_5X5_100)

# Ubuntu Pro Token (RT PATCH) #
ubuntu_pro_token = ""

# Code Version [DONT CHANGE] #
droid_version = "1.3"

