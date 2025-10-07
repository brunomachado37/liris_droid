import torch
from PIL import Image

from droid.misc.parameters import language_command, unnorm_key


class PolicyWrapperOpenVLA:
    def __init__(self, model, transform):
        print(type(model), type(transform))
        self.policy = model
        self.policy.to("cuda:0")
        self.transform = transform
        self.instruction = language_command
        self.unnorm_key = unnorm_key

    def forward(self, observation):
        # input_image = observation["observation"]["camera"]["image"]["varied_camera"][0]
        # input_image = observation["image"]["21555878_left"][:, :, :3]
        input_image = observation["image"]["21555878_left"][:, :, [2, 1, 0]]
        input_image = Image.fromarray(input_image)
        input_image.save("test.png")
        # input_image = input_image.resize((640, 360), resample=Image.BICUBIC)
        prompt = f"In: What action should the robot take to {self.instruction.lower()}?\nOut:"
            
        inputs = self.transform(prompt, input_image).to("cuda:0", dtype=torch.bfloat16)
        action = self.policy.predict_action(**inputs, unnorm_key=self.unnorm_key, do_sample=False)

        # Reverse Gripper Action #
        action[-1] = 1 - action[-1]

        return action

    def __call__(self, observation):
        return self.forward(observation)
    
    def reset(self):
        pass