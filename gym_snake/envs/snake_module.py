# Snake object class
import pygame


class snake_class(object):
	body = [(0,0)]
	head_x = 0 # variable that constantly represents the value of the x of the head
	head_y = 0 # variable that constantly represents the value of the y of the head
	newx = 0 # x of the head after the move
	newy = 0 # y of the head after the move
	direction = 0 # Direction of the snake: 0 = down, 1= up, 2 = left, 3 =  right
	#windows parameters
	width = 0
	height = 0

	def __init__(self, head_x, head_y, win, width, height):
		# Init the snake with the haed and one piece of body
		self.head_x = head_x
		self.head_y = head_y
		self.newx = head_x
		self.newy = head_y
		self.body[0] = (head_x, head_y)
		self.body.append((head_x , head_y-1))
		self.width = width
		self.height = height
		pygame.draw.rect(win, (235, 110, 52), (head_x*width, head_y* height, width, height))
		pygame.draw.rect(win, (235, 110, 52), (self.body[1][0]*width, self.body[1][1]* height, width, height))


	def move(self, direction, grid_size, fruit):
		# Change direction
		self.direction = direction
		if self.direction == 0:
			self.newy = self.head_y + 1
			if self.newy >= grid_size:
				self.newy = 0
		if self.direction == 1:
			self.newy = self.head_y - 1
			if self.newy < 0:
				self.newy = grid_size - 1
		if self.direction == 2:
			self.newx = self.head_x - 1
			if self.newx < 0:
				self.newx = grid_size - 1
		if self.direction == 3:
			self.newx = self.head_x + 1
			if self.newx >= grid_size:
				self.newx = 0
		#check fruit eaten
		if self.head_x == fruit[0] and self.head_y == fruit[1]:
			return True
		return False
	
	def update_Snake(self, win, width, height, eaten):
		# After have done a move, this function update the graphic of the snake and return true 
		# if the move is valid, false otherwise
		prev_x= self.newx
		prev_y = self.newy
		self.head_x = prev_x
		self.head_y = prev_y
		h = (self.head_x, self.head_y)
		#check collisions with body
		if (h in list(self.body)):
			return False
		else: 
			pygame.draw.rect(win, (255, 110, 52), (self.newx*width, self.newy* height, width, height))
			
			for i, cell in enumerate(self.body):
				pygame.draw.rect(win, (235, 110+ i , 42+ i ), (prev_x*width, prev_y* height, width, height))
				dummyx = cell[0]
				dummyy = cell[1]
				self.body[i] = (prev_x, prev_y)
				prev_x = dummyx
				prev_y = dummyy
			if not eaten : 
				pygame.draw.rect(win, (0, 0, 0), (prev_x*width, prev_y* height, width, height))
			else:
				self.body.append((prev_x, prev_y))
			return True
	
	def getBody(self):
		return self.body

	def getHead_x(self):
		return self.head_x

	def getHead_y(self):
		return self.head_y