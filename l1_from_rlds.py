import hydra
import torch
import tensorflow_datasets as tfds

from PIL import Image


@hydra.main(config_path="/app/config/eval", config_name="exec")
def main(config):
    # Load policy #
    model = hydra.utils.instantiate(config.algo.model).to("cuda:0")
    transform = hydra.utils.instantiate(config.algo.transform)

    # Replay Trajectory #
    dataset = tfds.builder_from_directory('/app/checkpoints/liris_pnp_cube/1.0.0').as_dataset(split='all')
    for episode in dataset:
        for step in episode["steps"]:
            image = step["observation"]["exterior_image_1_left"].numpy()
            language_instruction = step["language_instruction"].numpy().decode('utf-8')
            action_dict = step["action_dict"]

            input_image = Image.fromarray(image)
            prompt = f"In: What action should the robot take to {language_instruction.lower()}?\nOut:"
            inputs = transform(prompt, input_image).to("cuda:0", dtype=torch.bfloat16)
            action = model.predict_action(**inputs, unnorm_key="liris_pnp_cube", do_sample=False)
            action[-1] = 1 - action[-1]

            print(f"L1 cartesian velocity: {sum(abs(action[:6] - action_dict['cartesian_velocity'].numpy()))}")
            print(f"L1 gripper cartesian position: {sum(abs(action[6:] - action_dict['gripper_position'].numpy()))}")
        break


if __name__ == "__main__":
    main()