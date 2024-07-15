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
pygame.display.set_mode(resolution, pygame.FULLSCREEN)
pygame.display.set_caption('Solar System')

value = 0

run = True

moving = False


degree_preset = math.pi/180
dist_around_sun = math.pi*2
speed_multiplier = 1

# Create angle variables for each planet
angle_mercury = degree_preset * 180		# CONFIG angle: 300
angle_venus = degree_preset * 270		# CONFIG angle: 270
angle_earth = degree_preset * 105		# CONFIG angle: 105
angle_mars = degree_preset * 345		# CONFIG angle: 345
angle_jupiter = degree_preset * 210		# CONFIG angle: 210
angle_saturn = degree_preset * 30		# CONFIG angle: 30
angle_uranus = degree_preset * 195		# CONFIG angle: 195
angle_neptune = degree_preset * 240 	# CONFIG angle: 240


#position sun
sun_x = 900
sun_y = 470


#planet radius 
radius_mercury = 200
radius_venus = 250 
radius_earth = 300 
radius_mars = 350 
radius_jupiter = 400 
radius_saturn = 450 
radius_uranus = 500 
radius_neptune = 550 

#planes scale
scale_sun = 280 # Real diameter: 1'392'000 km
scale_mercury = 4 # Real diameter: 4'879 km
scale_venus = 12 # Real diameter: 12'104 km
scale_earth = 12 # Real diameter: 12'756 km
scale_mars = 6 # Real diameter: 6'792 km
scale_jupiter = 139 # Real diameter: 139'820 km
scale_saturn = 116 # Real diameter: 116'460 km
scale_uranus = 50 # Real diameter: 50'724 km
scale_neptune = 49 # Real diameter: 49'244 km



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
	angle_mercury += dist_around_sun /88 * speed_multiplier		#is the speed of a surrounding time of 88 days
	angle_venus += dist_around_sun /225 * speed_multiplier	#is the speed of a surrounding time of 225 days
	angle_earth += dist_around_sun /365 * speed_multiplier		#is the speed of a surrounding time of 365 days
	angle_mars += dist_around_sun /687 * speed_multiplier		#is the speed of a surrounding time of 687 days
	angle_jupiter += dist_around_sun /4333 * speed_multiplier	#is the speed of a surrounding time of 4333 days
	angle_saturn += dist_around_sun /10759 * speed_multiplier	#is the speed of a surrounding time of 10759 days
	angle_uranus += dist_around_sun /30687 * speed_multiplier	#is the speed of a surrounding time of 30687 days
	angle_neptune += dist_around_sun /60190 * speed_multiplier	#is the speed of a surrounding time of 60190 days

	# ...
 
	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			run = False
			pygame.quit()
			quit()
	pygame.display.update()