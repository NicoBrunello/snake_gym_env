import gym
from gym import error, spaces, utils
from gym.utils import seeding
# Imports for snake
import pygame
import random 
from Game_snake import game_Manager as gm


# Constants
HEIGHT = 25
WIDTH = 25
GRID_SIZE = 30
N_CHANNELS = 1
N_DISCRETE_ACTIONS = 5


class GymEnv(gym.Env):
	metadata = {'render.modes': ['human']}
	action_space = None
	observation_space = None

	def __init__(self):
	    super(CustomEnv, self).__init__()
	    gm.init(HEIGHT, WIDTH, GRID_SIZE)
	    # Define action and observation space
	    # They must be gym.spaces objects
	    # Actions are snake moviments:
	    self.action_space = spaces.Discrete(N_DISCRETE_ACTIONS)
	    # Observation is the grid state:
	    # TODO: make this a compatible box with grid + snake + fruit
	    self.observation_space = spaces.Box(shape=(GRID_SIZE, GRID_SIZE, N_CHANNELS), dtype=np.uint8)

	def step(self, action):
		return gm.step(action)


	def reset(self):
		gm.init(HEIGHT, WIDTH, GRID_SIZE)


	def render(self, mode='human', close=False):
		pass
