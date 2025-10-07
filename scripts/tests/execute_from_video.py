import hydra

from droid.robot_env import RobotEnv
from droid.trajectory_utils.misc import execute_policy_with_dataset_images


@hydra.main(config_path="/app/config/eval", config_name="exec")
def main(config):
    # Make the robot env
    env = RobotEnv(action_space=config.algo.action_space,
                   gripper_action_space=config.algo.gripper_action_space)

    # Load policy #
    model = hydra.utils.instantiate(config.algo.model).to("cuda:0")
    transform = hydra.utils.instantiate(config.algo.transform)
    policy = hydra.utils.instantiate(config.algo.policy, model=model, transform=transform)

    # Replay Trajectory #
    h5_filepath = config.trajectory_folderpath + "/trajectory.h5"
    recording_folderpath = config.trajectory_folderpath + "/recordings/MP4"
    execute_policy_with_dataset_images(env, policy, filepath=h5_filepath, recording_folderpath=recording_folderpath)


if __name__ == "__main__":
    main()