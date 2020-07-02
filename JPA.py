import time
import numpy as np
import random
import math
import csv
import msvcrt
from graphics import *

win = GraphWin("Game", 800,600)
win.setCoords(0,0,800,600)
enemies = []

class CreateEnemy:
	
	def __init__(self,cords,health,size,color):
		self.c = cords
		self.h = health
		self.s = size
		self.clr = color

	def draw_enemy(self):
		self.n = Circle(Point(self.c[0],self.c[1]), self.s)
		self.n.setFill(self.clr)
		self.n.draw(win)
	
	def enemy_hit(self,cords):
		if(self.c[0] + self.s >= cords[0] >= self.c[0] - self.s and self.c[1] + self.s >= cords[1] >= self.c[1] - self.s):
			print(self.n)
			self.n.undraw()

	def enemy_move(self,player_cords):

		if (player_cords[0] > self.c[0]):
			dx = random.randrange(1,10)
		else:
			dx = random.randrange(-10,-1)

		if (player_cords[1] > self.c[1]):
			dy = random.randrange(1,10)
		else:
			dy = random.randrange(-10,-1)

		self.c[0]+=dx/10
		self.c[1]+=dy/10

		self.n.move(dx/10,dy/10)

class Attack:

	def __init__(self,attrange):
		self.r = attrange


	def range_multiplier(self,pos_cords,click_cords):
		new_cords = [0,0]
		cords = [(click_cords[0]-pos_cords[0]),(click_cords[1]-pos_cords[1])]
		angle = math.atan(cords[1]/cords[0])
		if cords[0] > 0:
			new_cords[0] = self.r * math.cos(angle) + pos_cords[0]
			new_cords[1] = self.r * math.sin(angle) + pos_cords[1]
		else:
			new_cords[0] = self.r * math.cos(angle+math.pi) + pos_cords[0]
			new_cords[1] = self.r * math.sin(angle+math.pi) + pos_cords[1]
	
		return new_cords





dx, dy = 10, 0
key = 0


head = Circle(Point(400,500), 25) # set center and radius
head.setFill("yellow")
head.draw(win)
mcx, mcy = 400,500
player_cords = [mcx,mcy]
p = None
line = None
count_1 = 0
cords = []


i = 0		
while i < 10:		
	cords = [0,0]	
	cords[0] = random.randrange(1,799)
	cords[1] = random.randrange(1,599)
	size = random.randrange(10,50)
	enemies.append(CreateEnemy(cords,20,size,"red"))
	enemies[i].draw_enemy()
	i+=1



while 1:
	k = win.checkKey()


	if k == 'a':
		head.move(-dx, dy)
		mcx -= dx
		player_cords = [mcx,mcy]
	
	
	elif k == 'd':
		head.move(dx, dy)
		mcx += dx
		player_cords = [mcx,mcy]
		

	elif k == 'w':
		head.move(dy,dx)
		mcy += dx
		player_cords = [mcx,mcy]
		
	elif k == 's':
		head.move(dy,-dx)
		mcy -= dx
		player_cords = [mcx,mcy]

	

	p = win.checkMouse()

	if(p != None):
		if (line):
			line.undraw()
		x = p.x
		y = p.y
		user_attack = Attack(100)
		cords = user_attack.range_multiplier([mcx,mcy],[x,y])
		line = Line(Point(mcx,mcy), Point(cords[0],cords[1]))
		line.draw(win)
		for enemy in enemies:			
			enemy.enemy_hit(cords)
	

	for enemy in enemies:		
		enemy.enemy_move(player_cords)

	time.sleep(.01)


	







