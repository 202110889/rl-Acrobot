import gym

# import gymnasium as gym
# import ale_py
# gym.register_envs(ale_py)
import time


# import matplotlib.pyplot as plt

env = gym.make("ALE/Breakout-v5", render_mode="human")  # remove render_mode in training
obs, info = env.reset()

episode_over = False
while not episode_over:
    time.sleep(0.1)
    action = env.action_space.sample()
    obs, reward, terminated, truncated, info = env.step(action)
    episode_over = terminated or truncated
env.close()
