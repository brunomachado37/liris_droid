import hydra

from droid.robot_env import RobotEnv
from droid.trajectory_utils.misc import execute_policy_with_camera_images


@hydra.main(config_path="/app/config/eval", config_name="exec")
def main(config):
    # Make the robot env
    env = RobotEnv(action_space=config.algo.action_space,
                   gripper_action_space=config.algo.gripper_action_space)

    env.control_hz = 3

    # Load policy #
    model = hydra.utils.instantiate(config.algo.model).to("cuda:0")
    transform = hydra.utils.instantiate(config.algo.transform)
    policy = hydra.utils.instantiate(config.algo.policy, model=model, transform=transform)

    execute_policy_with_camera_images(env, policy, limit_horizon=500, randomize_initial_position=False)


if __name__ == "__main__":
    main()