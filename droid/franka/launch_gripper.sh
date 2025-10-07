source ~/miniconda3/bin/activate
conda activate polymetis-local
pkill -9 gripper
launch_gripper.py gripper=robotiq_2f gripper.comport=/dev/ttyUSB0 
