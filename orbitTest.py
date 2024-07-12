import pygame
from pygame.locals import *
from time import sleep
import math
    
pygame.init()

window = pygame.display.set_mode((600, 600))

image1 = pygame.image.load("./sun.png")				
image2 = pygame.image.load("./merkur.png")
image = image1
image = pygame.transform.scale(image, (180, 180))


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

	clock.tick(180)
	x = 100
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