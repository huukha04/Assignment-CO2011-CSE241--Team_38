import gym_cutting_stock
import gymnasium as gym
from policy import GreedyPolicy, RandomPolicy
from student_submissions.s2210xxx.policy2211412 import Policy2211412
import imageio
# Create the environment
env = gym.make(
    "gym_cutting_stock/CuttingStock-v0",
    render_mode="human",  # Comment this line to disable rendering
)

# Số khung hình tối đa
max_frames = 500

# Tạo một danh sách để lưu các khung hình
frames = []


NUM_EPISODES = 1

if __name__ == "__main__":
    observation, info = env.reset(seed=8)
    
    Policy2211412 = Policy2211412(policy_id=2)
    ep = 0
    while ep < NUM_EPISODES:
        action = Policy2211412.get_action(observation, info)
        observation, reward, terminated, truncated, info = env.step(action)
       

        if terminated or truncated:
            print("seed = ", ep)
            print(info)
            observation, info = import gym_cutting_stock
import gymnasium as gym
from policy import GreedyPolicy, RandomPolicy
from student_submissions.s2210xxx.policy2210xxx import Policy2210xxx

# Create the environment
env = gym.make(
    "gym_cutting_stock/CuttingStock-v0",
    render_mode="human",  # Comment this line to disable rendering
)
NUM_EPISODES = 100

if __name__ == "__main__":
    # Reset the environment
    observation, info = env.reset(seed=42)

    # Test GreedyPolicy
    gd_policy = GreedyPolicy()
    ep = 0
    while ep < NUM_EPISODES:
        action = gd_policy.get_action(observation, info)
        observation, reward, terminated, truncated, info = env.step(action)

        if terminated or truncated:
            print(info)
            observation, info = env.reset(seed=ep)
            ep += 1

    # Reset the environment
    observation, info = env.reset(seed=42)

    # Test RandomPolicy
    rd_policy = RandomPolicy()
    ep = 0
    while ep < NUM_EPISODES:
        action = rd_policy.get_action(observation, info)
        observation, reward, terminated, truncated, info = env.step(action)

        if terminated or truncated:
            print(info)
            observation, info = env.reset(seed=ep)
            ep += 1
            
    # Reset the environment
    observation, info = env.reset(seed=42)

    # Test
    G_2211412 = 2211412()
    ep = 0
    while ep < NUM_EPISODES:
        action = G_2211412.get_action(observation, info)
        observation, reward, terminated, truncated, info = env.step(action)

        if terminated or truncated:
            print(info)
            observation, info = env.reset(seed=ep)
            ep += 1

    # Uncomment the following code to test your policy
    # # Reset the environment
    # observation, info = env.reset(seed=42)
    # print(info)

    # policy2210xxx = Policy2211412(policy_id=1)
    # for _ in range(200):
    #     action = policy2210xxx.get_action(observation, info)
    #     observation, reward, terminated, truncated, info = env.step(action)
    #     print(info)

    #     if terminated or truncated:
    #         observation, info = env.reset()

env.close()env.reset(seed=ep)
            ep += 8

gif_path = "cutting_stock_simulation.gif"
imageio.mimsave(gif_path, frames, duration=0.1)  # duration điều chỉnh tốc độ khung hình

env.close()
