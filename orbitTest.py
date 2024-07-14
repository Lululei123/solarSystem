import pygame
from pygame.locals import *
from time import sleep
import math
    
pygame.init()

window = pygame.display.set_mode((2000, 2000))
planets = [
		(pygame.image.load("./img/sun.png")),		#0
		(pygame.image.load("./img/mercury.png")),	#1
		(pygame.image.load("./img/venus.png")),		#2
		(pygame.image.load("./img/earth.png")),		#3
		(pygame.image.load("./img/mars.png")),		#4
		(pygame.image.load("./img/jupiter.png")),	#5
		(pygame.image.load("./img/saturn.png")),	#6
		(pygame.image.load("./img/uranus.png")),	#7
		(pygame.image.load("./img/neptune.png"))	#8
		]


clock = pygame.time.Clock()

resolution = (2000,2000)
# pygame.display.set_mode(resolution, pygame.RESIZABLE)
# pygame.display.set_mode(resolution, pygame.FULLSCREEN)
pygame.display.set_caption('Solar System')

value = 0

run = True

moving = False

# Create angle variables for each planet
angle_mercury = 3
angle_venus = 7
angle_earth = 0
angle_mars = 0
angle_jupiter = 0
angle_saturn = 0
angle_uranus = 0
angle_neptune = 0

# ...



#declare position of the sun
sun_x = 750
sun_y = 450

#declare center position for planets


#planet radius 



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
	x = 150 
	y = 150
	mercury = pygame.transform.scale(planets[1], (30, 30))
	x = int(x*math.cos(angle_mercury)+835) #x/y: radius of orbit, +[value]: coordinates - center of orbit, angle_mercury: angle of rotation
	y = int(y*math.sin(angle_mercury)+535) #x/y: radius of orbit, +[value]: coordinates - center of orbit, angle_mercury: angle of rotation
	window.fill((0, 0, 0))
	window.blit(mercury, (x, y))
 
	x = 150 
	y = 150
	venus = pygame.transform.scale(planets[2], (30, 30))
	x = int(x*math.cos(angle_venus)+835) #x/y: radius of orbit, +[value]: coordinates - center of orbit, angle_venus: angle of rotation
	y = int(y*math.sin(angle_venus)+535) #x/y: radius of orbit, +[value]: coordinates - center of orbit, angle_venus: angle of rotation
	window.blit(venus, (x, y))
	x=750
	x = 200 
	y = 200
	earth = pygame.transform.scale(planets[3], (30, 30))
	x = int(x*math.cos(angle_earth)+835) #x/y: radius of orbit, +[value]: coordinates - center of orbit, angle_earth: angle of rotation
	y = int(y*math.sin(angle_earth)+535) #x/y: radius of orbit, +[value]: coordinates - center of orbit, angle_earth: angle of rotation
	window.blit(earth, (x, y))

	x = 250 
	y = 250
	mars = pygame.transform.scale(planets[4], (30, 30))
	x = int(x*math.cos(angle_mars)+835) #x/y: radius of orbit, +[value]: coordinates - center of orbit, angle_mars: angle of rotation
	y = int(y*math.sin(angle_mars)+535) #x/y: radius of orbit, +[value]: coordinates - center of orbit, angle_mars: angle of rotation
	window.blit(mars, (x, y))

	x = 300 
	y = 300
	jupiter = pygame.transform.scale(planets[5], (30, 30))
	x = int(x*math.cos(angle_jupiter)+835) #x/y: radius of orbit, +[value]: coordinates - center of orbit, angle_jupiter: angle of rotation
	y = int(y*math.sin(angle_jupiter)+535) #x/y: radius of orbit, +[value]: coordinates - center of orbit, angle_jupiter: angle of rotation
	window.blit(jupiter, (x, y))

	x = 350 
	y = 350
	saturn = pygame.transform.scale(planets[6], (30, 30))
	x = int(x*math.cos(angle_saturn)+835) #x/y: radius of orbit, +[value]: coordinates - center of orbit, angle_saturn: angle of rotation
	y = int(y*math.sin(angle_saturn)+535) #x/y: radius of orbit, +[value]: coordinates - center of orbit, angle_saturn: angle of rotation
	window.blit(saturn, (x, y))

	x = 400 
	y = 400
	uranus = pygame.transform.scale(planets[7], (30, 30))
	x = int(x*math.cos(angle_uranus)+835) #x/y: radius of orbit, +[value]: coordinates - center of orbit, angle_uranus: angle of rotation
	y = int(y*math.sin(angle_uranus)+535) #x/y: radius of orbit, +[value]: coordinates - center of orbit, angle_uranus: angle of rotation
	window.blit(uranus, (x, y))

	x = 450 
	y = 450
	neptune = pygame.transform.scale(planets[8], (30, 30))
	x = int(x*math.cos(angle_neptune)+835) #x/y: radius of orbit, +[value]: coordinates - center of orbit, angle_neptune: angle of rotation
	y = int(y*math.sin(angle_neptune)+535) #x/y: radius of orbit, +[value]: coordinates - center of orbit, angle_neptune: angle of rotation
	window.blit(neptune, (x, y))
 
	x = sun_x
	y = sun_y
	sun = pygame.transform.scale(planets[0] , (200, 200))
	window.blit(sun, (x, y))
	sleep(0.1)

		# Update the angle variables for each planet
	angle_mercury += 0.1
	angle_venus += 0.1
	angle_earth += 0.1
	angle_mars += 0.1
	angle_jupiter += 0.1
	angle_saturn += 0.1
	angle_uranus += 0.1
	angle_neptune += 0.1

	# ...
 
	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			run = False
			pygame.quit()
			quit()

	pygame.display.update()