import pygame
from pygame.locals import *
from time import sleep
import math
    
pygame.init()

window = pygame.display.set_mode((2000, 2000))
planets = [
		(pygame.image.load("./img/sun.png")),
		(pygame.image.load("./img/mercury.png")),
		(pygame.image.load("./img/venus.png")),
		(pygame.image.load("./img/earth.png")),
		(pygame.image.load("./img/mars.png")),
		(pygame.image.load("./img/jupiter.png")),
		(pygame.image.load("./img/saturn.png")),
		(pygame.image.load("./img/uranus.png")),
		(pygame.image.load("./img/neptune.png"))
		]


clock = pygame.time.Clock()

resolution = (1500,1500)
pygame.display.set_mode(resolution, pygame.FULLSCREEN)


value = 0

run = True

moving = False

velocity = 12

x = 800
y = 150

#34*sin von Grad/365*x   34*cos von Grad/365*y
#formel für kreisbewegung

angle1 = 0
angle2 = 0


while run:
	clock.tick(120)

	#add sun
	
	"""
	explanation of coordinates:
	- x/y: radius of orbit aound sun
	- +[value]: coordinates - center of orbit
		=> coordintes of top left corner of the image
		=> center of the image is at (x + x-scale| y + y-scale)
		=> center of the orbit is at (750 + (sun)x-scale/2 | 450 + (sun)y-scale/2)
		=> to aling image in the orbit and let it spin around the sun: (sun-coordinates + radius of orbit - image-scale/2)
	- angle1: angle of rotation
	
	"""

	#move mercury around sun
	x = 100 
	y = 100
	x = int(x*math.cos(angle1)+835) #x/y: radius of orbit, +[value]: coordinates - center of orbit, angle1: angle of rotation
	y = int(y*math.sin(angle1)+535) #x/y: radius of orbit, +[value]: coordinates - center of orbit, angle1: angle of rotation
	mercury = pygame.transform.scale(planets[1], (30, 30))
	window.fill((0, 0, 0))
	window.blit(mercury, (x, y))
	y = 100
	x = int(x*math.cos(angle1)+300)
	y = int(y*math.sin(angle1)+300)
	print(x, y)
	image = pygame.transform.scale(image, (180, 180))
	window.blit(image, (x, y))
	pygame.display.update()
	window.fill((0, 0, 0))
	sleep(0.1)
	
	
 
	angle1 += 0.1
	# for i in range(100, 0, -8):
	# 	x -= 8
	# 	y += 8
	# 	sleep(0.1)
	# 	image = pygame.transform.scale(image, (180, 180))
	# 	window.blit(image, (x, y))
	# 	pygame.display.update()
	# 	window.fill((0, 0, 0))

	# for i in range(100, 0, -8):
	# 	x += 8
	# 	y += 8
	# 	sleep(0.1)
	# 	image = pygame.transform.scale(image, (180, 180))
	# 	window.blit(image, (x, y))
	# 	pygame.display.update()
	# 	window.fill((0, 0, 0))
  
	# for i in range(100, 0, -8):
	# 	x += 8
	# 	y -= 8
	# 	sleep(0.1)
	# 	image = pygame.transform.scale(image, (180, 180))
	# 	window.blit(image, (x, y))
	# 	pygame.display.update()
	# 	window.fill((0, 0, 0))

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			run = False
			pygame.quit()
			quit()

		if event.type == pygame.KEYUP:

			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				moving = False
				value = 0
	key_pressed_is = pygame.key.get_pressed()



	# window.blit(image, (x, y))

	pygame.display.update()

	# window.fill((0, 0, 0))