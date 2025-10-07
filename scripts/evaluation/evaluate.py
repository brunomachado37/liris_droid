from droid.evaluation.eval_launcher_liris import eval_launcher
import matplotlib.pyplot as plt
import os
import argparse
import cv2
import hydra

@hydra.main(version_base=None, config_path="config/eval", config_name="eval")
def main(config):   
    print("Evaluating Policy")
    eval_launcher(config)


if __name__ == "__main__":
    main()