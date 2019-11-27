import pygame
import random 
from snake_module import snake_class

class game_Manager:
	eaten = False
	total_grid= []
	fruit = []
	reward = 0

def init(self, height, width, grid_size):	
	# Init pygame
	pygame.init()
	#Init window variable
	# Remember: top left corner is (0,0) and down right corner is (grid_size, grid_size)
	# The reference is (horizontal, vertical)
	self.width = width
	self.height = height
	self.grid_size = grid_size
	self.win_size = (height * grid_size, width * grid_size)
	self.win = pygame.display.set_mode(self.win_size)

	pygame.display.set_caption("Pygame tutorial")


	# Initialize the grid
	self.total_grid= []
	for i in range(self.grid_size):
			for j in range(self.grid_size):
				pygame.draw.rect(self.win, (0, 0, 0), (i*self.width, j* self.height, self.width, self.height))
				self.total_grid.append((i,j))

	# Initialize the snake
	self.init_x = 4
	self.init_y = 4
	self.snake = snake_class(self.init_x, self.init_y, self.win, self.width, self.height)

	pygame.display.update()

	run = True
	direc = 0
	prev_dir = 0
	#Generate the first fruit
	current_free = list(set(total_grid) - set(snake.getBody()))
	fruit = current_free[random.randint(0, len(current_free))]
	pygame.draw.rect(win, (255, 255, 255), (fruit[0]*width, fruit[1]* height, width, height))
	move_res = True
	

def getState(self):
	return self.total_grid, self.snake.getBody(), self.fruit


def step(self, action):
	pygame.time.delay(100)
	#Generate a fruit
	if eaten: 
		current_free = list(set(total_grid) - set(snake.getBody()))
		fruit = current_free[random.randint(0, len(current_free )-1)]
		pygame.draw.rect(win, (255, 255, 255), (fruit[0]*width, fruit[1]* height, width, height))
	# Actions could be a list of 4 elements (up, down, right, left), all are 0s but the one taken which will be equal to one
	# If none of them is taken, then it means the snake keeps the prev direction
	
	eaten = snake.move(direc, grid_size, fruit)
	move_res = snake.update_Snake(win, width, height, eaten)
	if move_res == False:
		reward = -1
		run = False
	elif eaten == True:
		reward = 1
	else:
		reward = 0
	pygame.display.update()
	return getState(), reward


def quit():
	pygame.time.delay(100)
	pygame.quit()

