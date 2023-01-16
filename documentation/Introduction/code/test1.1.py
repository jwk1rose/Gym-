# test1.1

import gym

env = gym.make("CartPole-v0")
env.action_space.seed(42)

env.reset()

for _ in range(1000):
    observation, reward, terminated, truncated, info = env.step(env.action_space.sample())

if terminated or truncated:
    observation, info = env.reset()

env.close()

