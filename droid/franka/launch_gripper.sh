source ~/anaconda3/etc/profile.d/conda.sh
conda activate polymetis
pkill -9 gripper
launch_gripper.py gripper=franka_hand
