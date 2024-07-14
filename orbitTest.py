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
angle_mercury = 0
angle_venus = 1
angle_earth = 1.55
angle_mars = 3
angle_jupiter = 4
angle_saturn = 5
angle_uranus = 6
angle_neptune = 7


#position sun
sun_x = 750
sun_y = 450


#planet radius 
radius_mercury = 100
radius_venus = 150
radius_earth = 200
radius_mars = 250
radius_jupiter = 300
radius_saturn = 350
radius_uranus = 400
radius_neptune = 450


#planes scale
scale_sun = 100
scale_mercury = 30
scale_venus = 30
scale_earth = 30
scale_mars = 30
scale_jupiter = 30
scale_saturn = 30
scale_uranus = 30
scale_neptune = 30



while run:
	clock.tick(120)

	#add sun
	
	"""
	explanation of coordinates:
	- x/y: radius of orbit aound sun
	- +[value]: coordinates - center of orbit
		=> coordintes of top left corner of the image
		=> center of the image is at (x + x-scale| y + y-scale)
		=> centerOfOrbit = (sun[coord] + (sun)x-scale/2 | 450 + (sun)y-scale/2)
		=> to aling image in the orbit and let it spin around the sun: (centerOfOrbit - image-scale/2)
	- angle1: angle of rotation
	
	"""
	#move mercury around sun
	x = radius_mercury
	y = radius_mercury
	mercury = pygame.transform.scale(planets[1], (scale_mercury , scale_mercury))
	x_center = sun_x + scale_sun/2 - scale_mercury/2
	y_center = sun_y + scale_sun/2 - scale_mercury/2
	x = (x * math.cos(angle_mercury) + x_center) #x/y: radius of orbit, +[value]: coordinates - center of orbit, angle_mercury: angle of rotation
	y = (y * math.sin(angle_mercury) + y_center) #x/y: radius of orbit, +[value]: coordinates - center of orbit, angle_mercury: angle of rotation
	window.fill((0, 0, 0))
	window.blit(mercury, (x, y))
 
	x = radius_venus
	y = radius_venus
	venus = pygame.transform.scale(planets[2], (scale_venus , scale_venus))
	x_center = sun_x + scale_sun/2 - scale_venus/2
	y_center = sun_y + scale_sun/2 - scale_venus/2
	x = (x * math.cos(angle_venus) + x_center) #x/y: radius of orbit, +[value]: coordinates - center of orbit, angle_venus: angle of rotation
	y = (y * math.sin(angle_venus) + y_center) #x/y: radius of orbit, +[value]: coordinates - center of orbit, angle_venus: angle of rotation
	window.blit(venus, (x, y))

	x = radius_earth
	y = radius_earth
	earth = pygame.transform.scale(planets[3], (scale_earth , scale_earth))
	x_center = sun_x + scale_sun/2 - scale_earth/2
	y_center = sun_y + scale_sun/2 - scale_earth/2
	x = (x * math.cos(angle_earth) + x_center) #x/y: radius of orbit, +[value]: coordinates - center of orbit, angle_earth: angle of rotation
	y = (y * math.sin(angle_earth) + y_center) #x/y: radius of orbit, +[value]: coordinates - center of orbit, angle_earth: angle of rotation
	window.blit(earth, (x, y))

	x = radius_mars
	y = radius_mars
	mars = pygame.transform.scale(planets[4], (scale_mars , scale_mars))
	x_center = sun_x + scale_sun/2 - scale_mars/2
	y_center = sun_y + scale_sun/2 - scale_mars/2
	x = (x * math.cos(angle_mars) + x_center) #x/y: radius of orbit, +[value]: coordinates - center of orbit, angle_mars: angle of rotation
	y = (y * math.sin(angle_mars) + y_center) #x/y: radius of orbit, +[value]: coordinates - center of orbit, angle_mars: angle of rotation
	window.blit(mars, (x, y))

	x = radius_jupiter
	y = radius_jupiter
	jupiter = pygame.transform.scale(planets[5], (scale_jupiter , scale_jupiter))
	x_center = sun_x + scale_sun/2 - scale_jupiter/2
	y_center = sun_y + scale_sun/2 - scale_jupiter/2
	x = (x * math.cos(angle_jupiter) + x_center) #x/y: radius of orbit, +[value]: coordinates - center of orbit, angle_jupiter: angle of rotation
	y = (y * math.sin(angle_jupiter) + y_center) #x/y: radius of orbit, +[value]: coordinates - center of orbit, angle_jupiter: angle of rotation
	window.blit(jupiter, (x, y))

	x = radius_saturn
	y = radius_saturn
	saturn = pygame.transform.scale(planets[6], (scale_saturn , scale_saturn))
	x_center = sun_x + scale_sun/2 - scale_saturn/2
	y_center = sun_y + scale_sun/2 - scale_saturn/2
	x = (x * math.cos(angle_saturn) + x_center) #x/y: radius of orbit, +[value]: coordinates - center of orbit, angle_saturn: angle of rotation
	y = (y * math.sin(angle_saturn) + y_center) #x/y: radius of orbit, +[value]: coordinates - center of orbit, angle_saturn: angle of rotation
	window.blit(saturn, (x, y))

	x = radius_uranus
	y = radius_uranus
	uranus = pygame.transform.scale(planets[7], (scale_uranus , scale_uranus))
	x_center = sun_x + scale_sun/2 - scale_uranus/2
	y_center = sun_y + scale_sun/2 - scale_uranus/2
	x = (x * math.cos(angle_uranus) + x_center) #x/y: radius of orbit, +[value]: coordinates - center of orbit, angle_uranus: angle of rotation
	y = (y * math.sin(angle_uranus) + y_center) #x/y: radius of orbit, +[value]: coordinates - center of orbit, angle_uranus: angle of rotation
	window.blit(uranus, (x, y))

	x = radius_neptune
	y = radius_neptune
	neptune = pygame.transform.scale(planets[8], (scale_neptune , scale_neptune))
	x_center = sun_x + scale_sun/2 - scale_neptune/2
	y_center = sun_y + scale_sun/2 - scale_neptune/2
	x = (x * math.cos(angle_neptune) + x_center) #x/y: radius of orbit, +[value]: coordinates - center of orbit, angle_neptune: angle of rotation
	y = (y * math.sin(angle_neptune) + y_center) #x/y: radius of orbit, +[value]: coordinates - center of orbit, angle_neptune: angle of rotation
	window.blit(neptune, (x, y))
 
	x = sun_x
	y = sun_y
	sun = pygame.transform.scale(planets[0] , (scale_sun , scale_sun))
	window.blit(sun, (x, y))
	
	sun = pygame.transform.scale(planets[0] , (2 , 1500))
	window.blit(sun, (x + scale_sun/2, y + scale_sun/2))
	sun = pygame.transform.scale(planets[0] , (2 , 1500))
	window.blit(sun, (x + scale_sun/2, y + scale_sun/2))
	
 
	sleep(0.1)
 

		# Update the angle variables for each planet
	# angle_mercury += 0.1
	# angle_venus += 0.1
	# angle_earth += 0.1
	# angle_mars += 0.1
	# angle_jupiter += 0.1
	# angle_saturn += 0.1
	# angle_uranus += 0.1
	# angle_neptune += 0.1

	# ...
 
	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			run = False
			pygame.quit()
			quit()
	pygame.display.update()