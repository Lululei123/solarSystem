import pygame
from pygame.locals import *
from time import sleep
import math
  

#todo:
#
#
#
#
#
#
#
#
#
#
#
#
#
#planet rotation circles


  
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
		(pygame.image.load("./img/neptune.png")),	#8
		(pygame.image.load("./img/moon.png"))		#9
		]


clock = pygame.time.Clock()

resolution = (2000,2000)
pygame.display.set_mode(resolution, pygame.FULLSCREEN)
pygame.display.set_caption('Solar System')


#variables for calculations
run = True
show_moon = True
moving = False
pause = False
real_distance = False
degree_preset = math.pi/180
circumnavigation = math.pi*2
speed_multiplier = 1
real_scale = False
scale_summand = 0


#position sun
sun_x = 900
sun_y = 470


# Create angle variables for each planet
angle_mercury = degree_preset * 180		# CONFIG angle: 300
angle_venus = degree_preset * 270		# CONFIG angle: 270
angle_earth = degree_preset * 105		# CONFIG angle: 105
angle_moon = degree_preset * 0			# CONFIG angle: 0
angle_mars = degree_preset * 345		# CONFIG angle: 345
angle_jupiter = degree_preset * 210		# CONFIG angle: 210
angle_saturn = degree_preset * 30		# CONFIG angle: 30
angle_uranus = degree_preset * 195		# CONFIG angle: 195
angle_neptune = degree_preset * 240 	# CONFIG angle: 240


#planet radius 
radius_mercury = 200
radius_venus = 250 
radius_earth = 300 
radius_moon = 50
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
scale_moon = 3.4 # Real diameter: 3'474 km
scale_mars = 6 # Real diameter: 6'792 km
scale_jupiter = 139 # Real diameter: 139'820 km
scale_saturn = 116 # Real diameter: 116'460 km
scale_uranus = 50 # Real diameter: 50'724 km
scale_neptune = 49 # Real diameter: 49'244 km



while run:
	clock.tick(120)
	# while not read:
		#create introduction screen explaining the controls
		# r = real size
		# alt + f4 = close
		# esc = close
		# space = pause
		# right arrow = speed up
		# left arrow = speed down
	
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
	x = radius_mercury
	y = radius_mercury
	mercury = pygame.transform.scale(planets[1], (scale_mercury + scale_summand , scale_mercury + scale_summand))
	x_center = sun_x + scale_sun/2 - scale_mercury/2
	y_center = sun_y + scale_sun/2 - scale_mercury/2
	x = (x * math.cos(angle_mercury) + x_center) #x/y: radius of orbit, +[value]: coordinates - center of orbit, angle_mercury: angle of rotation
	y = (y * math.sin(angle_mercury) + y_center) #x/y: radius of orbit, +[value]: coordinates - center of orbit, angle_mercury: angle of rotation
	window.fill((0, 0, 0))
	window.blit(mercury, (x - scale_mercury/2, y - scale_mercury/2))


	x = radius_venus
	y = radius_venus
	venus = pygame.transform.scale(planets[2], (scale_venus + scale_summand, scale_venus + scale_summand))
	x_center = sun_x + scale_sun/2 - scale_venus/2
	y_center = sun_y + scale_sun/2 - scale_venus/2
	x = (x * math.cos(angle_venus) + x_center) #x/y: radius of orbit, +[value]: coordinates - center of orbit, angle_venus: angle of rotation
	y = (y * math.sin(angle_venus) + y_center) #x/y: radius of orbit, +[value]: coordinates - center of orbit, angle_venus: angle of rotation
	window.blit(venus, (x - scale_venus/2, y - scale_venus/2))
 
 
	x = radius_earth
	y = radius_earth
	earth = pygame.transform.scale(planets[3], (scale_earth + scale_summand , scale_earth + scale_summand))
	x_center = sun_x + scale_sun/2 - scale_earth/2
	y_center = sun_y + scale_sun/2 - scale_earth/2
	x = (x * math.cos(angle_earth) + x_center) #x/y: radius of orbit, +[value]: coordinates - center of orbit, angle_earth: angle of rotation
	y = (y * math.sin(angle_earth) + y_center) #x/y: radius of orbit, +[value]: coordinates - center of orbit, angle_earth: angle of rotation
	window.blit(earth, (x - scale_earth/2, y - scale_earth/2))


	if show_moon:
		moon = pygame.transform.scale(planets[9], (scale_moon + scale_summand/1.5 , scale_moon + scale_summand/1.5))
		x = (radius_moon * math.cos(angle_moon) + x) #x/y: radius of orbit, +[value]: coordinates - center of orbit, angle_moon: angle of rotation
		y = (radius_moon * math.sin(angle_moon) + y) #x/y: radius of orbit, +[value]: coordinates - center of orbit, angle_moon: angle of rotation
		window.blit(moon, (x - scale_moon/2, y - scale_moon/2))


	x = radius_mars
	y = radius_mars
	mars = pygame.transform.scale(planets[4], (scale_mars + scale_summand , scale_mars + scale_summand))
	x_center = sun_x + scale_sun/2 - scale_mars/2
	y_center = sun_y + scale_sun/2 - scale_mars/2
	x = (x * math.cos(angle_mars) + x_center) #x/y: radius of orbit, +[value]: coordinates - center of orbit, angle_mars: angle of rotation
	y = (y * math.sin(angle_mars) + y_center) #x/y: radius of orbit, +[value]: coordinates - center of orbit, angle_mars: angle of rotation
	window.blit(mars, (x - scale_mars/2, y - scale_mars/2))


	x = radius_jupiter
	y = radius_jupiter
	jupiter = pygame.transform.scale(planets[5], (scale_jupiter + scale_summand , scale_jupiter + scale_summand))
	x_center = sun_x + scale_sun/2 - scale_jupiter/2
	y_center = sun_y + scale_sun/2 - scale_jupiter/2
	x = (x * math.cos(angle_jupiter) + x_center) #x/y: radius of orbit, +[value]: coordinates - center of orbit, angle_jupiter: angle of rotation
	y = (y * math.sin(angle_jupiter) + y_center) #x/y: radius of orbit, +[value]: coordinates - center of orbit, angle_jupiter: angle of rotation
	window.blit(jupiter, (x - scale_jupiter/2, y - scale_jupiter/2))


	x = radius_saturn
	y = radius_saturn
	saturn = pygame.transform.scale(planets[6], (scale_saturn + scale_summand , scale_saturn + scale_summand))
	x_center = sun_x + scale_sun/2 - scale_saturn/2
	y_center = sun_y + scale_sun/2 - scale_saturn/2
	x = (x * math.cos(angle_saturn) + x_center) #x/y: radius of orbit, +[value]: coordinates - center of orbit, angle_saturn: angle of rotation
	y = (y * math.sin(angle_saturn) + y_center) #x/y: radius of orbit, +[value]: coordinates - center of orbit, angle_saturn: angle of rotation
	window.blit(saturn, (x - scale_saturn/2, y - scale_saturn/2))


	x = radius_uranus
	y = radius_uranus
	uranus = pygame.transform.scale(planets[7], (scale_uranus + scale_summand , scale_uranus + scale_summand))
	x_center = sun_x + scale_sun/2 - scale_uranus/2
	y_center = sun_y + scale_sun/2 - scale_uranus/2
	x = (x * math.cos(angle_uranus) + x_center) #x/y: radius of orbit, +[value]: coordinates - center of orbit, angle_uranus: angle of rotation
	y = (y * math.sin(angle_uranus) + y_center) #x/y: radius of orbit, +[value]: coordinates - center of orbit, angle_uranus: angle of rotation
	window.blit(uranus, (x - scale_uranus/2, y - scale_uranus/2))


	x = radius_neptune
	y = radius_neptune
	neptune = pygame.transform.scale(planets[8], (scale_neptune + scale_summand , scale_neptune + scale_summand))
	x_center = sun_x + scale_sun/2 - scale_neptune/2
	y_center = sun_y + scale_sun/2 - scale_neptune/2
	x = (x * math.cos(angle_neptune) + x_center) #x/y: radius of orbit, +[value]: coordinates - center of orbit, angle_neptune: angle of rotation
	y = (y * math.sin(angle_neptune) + y_center) #x/y: radius of orbit, +[value]: coordinates - center of orbit, angle_neptune: angle of rotation
	window.blit(neptune, (x - scale_neptune/2, y - scale_neptune/2))
 
 
	x = sun_x
	y = sun_y
	sun = pygame.transform.scale(planets[0] , (scale_sun , scale_sun ))
	window.blit(sun, (x, y))
	
 
	#debug images 
 
	# sun = pygame.transform.scale(planets[0] , (2 , 1500))
	# window.blit(sun, (x + scale_sun/2, y + scale_sun/2))
	# sun = pygame.transform.scale(planets[0] , (1500 , 2))
	# window.blit(sun, (x + scale_sun/2, y + scale_sun/2))
	
	#...
 

	sleep(0.09)
 

		# Update the angle variables for each planet
	angle_mercury += circumnavigation /88 * speed_multiplier		#is the speed of a surrounding time of 88 days
	angle_venus += circumnavigation /225 * speed_multiplier	#is the speed of a surrounding time of 225 days
	angle_earth += circumnavigation /365 * speed_multiplier		#is the speed of a surrounding time of 365 days
	angle_moon += circumnavigation /27 * speed_multiplier		#is the speed of a surrounding time of 27 days
	angle_mars += circumnavigation /687 * speed_multiplier		#is the speed of a surrounding time of 687 days
	angle_jupiter += circumnavigation /4333 * speed_multiplier	#is the speed of a surrounding time of 4333 days
	angle_saturn += circumnavigation /10759 * speed_multiplier	#is the speed of a surrounding time of 10759 days
	angle_uranus += circumnavigation /30687 * speed_multiplier	#is the speed of a surrounding time of 30687 days
	angle_neptune += circumnavigation /60190 * speed_multiplier	#is the speed of a surrounding time of 60190 days

	# ...
 
	for event in pygame.event.get():
		#if r key is pressed make the planets in real size_scale
		if event.type == KEYDOWN:
			
			#speed up
			if event.key == K_RIGHT:
				speed_multiplier += 0.2
				if speed_multiplier > 10:
					speed_multiplier = 10

			#speed down
			elif event.key == K_LEFT:
				speed_multiplier -= 0.2
				if speed_multiplier < 0:
					speed_multiplier = 0
     
			#scale up
			elif event.key == K_UP and not real_scale:
				scale_summand += 2
	
 
			#scale down
			elif event.key == K_DOWN and not real_scale:
				scale_summand -= 2
				if scale_summand < 0:
					scale_summand = 0
    
    
			#reset all, except position
			elif event.key == K_r:
				speed_multiplier = 1
				scale_summand = 0
				scale_temp = 0
     
     
			elif KMOD_ALT and event.key == K_z:
				#up scaled
				if real_scale and not real_distance:
					scale_sun = 280
					scale_mercury = 4
					scale_venus = 12
					scale_earth = 12
					scale_moon = 3.4
					scale_mars = 6
					scale_jupiter = 139
					scale_saturn = 116
					scale_uranus = 50
					scale_neptune = 49
	
					radius_mercury = 200
					radius_venus = 250 
					radius_earth = 300 
					radius_moon = 50
					radius_mars = 350 
					radius_jupiter = 400 
					radius_saturn = 450 
					radius_uranus = 500 
					radius_neptune = 550 
     
					real_scale = False
					scale_summand = scale_temp
				#real size
				else:
					scale_sun = 1392000 / 4000
					scale_mercury = 4879 / 4000
					scale_venus = 12104 / 4000
					scale_earth = 12756 / 4000
					scale_moon = 3474 / 4000
					scale_mars = 6792 / 4000
					scale_jupiter = 139820 / 4000
					scale_saturn = 116460 / 4000
					scale_uranus = 50724 / 4000
					scale_neptune = 49244 / 4000
									
					real_scale = True
					scale_temp = scale_summand
					scale_summand = 0


			elif KMOD_ALT and event.key == K_d:
				if not real_distance and not real_scale:
					radius_mercury = 6.5
					radius_venus = 12
					radius_earth = 16.6
					radius_mars = 25.3
					radius_jupiter = 86.6
					radius_saturn = 159.6
					radius_uranus = 320.3
					radius_neptune = 500.83
     
					scale_sun = 10
					scale_mercury = 10
					scale_venus = 10
					scale_earth = 10
					scale_moon = 10
					scale_mars = 10
					scale_jupiter = 10
					scale_saturn = 10
					scale_uranus = 10
					scale_neptune = 10
     
					show_moon = False
					real_distance = True
				else:
					radius_mercury = 200
					radius_venus = 250 
					radius_earth = 300 
					radius_moon = 50
					radius_mars = 350 
					radius_jupiter = 400 
					radius_saturn = 450 
					radius_uranus = 500 
					radius_neptune = 550
     
					scale_sun = 1392000 / 4000
					scale_mercury = 4879 / 4000
					scale_venus = 12104 / 4000
					scale_earth = 12756 / 4000
					scale_moon = 3474 / 4000
					scale_mars = 6792 / 4000
					scale_jupiter = 139820 / 4000
					scale_saturn = 116460 / 4000
					scale_uranus = 50724 / 4000
					scale_neptune = 49244 / 4000
     
					show_moon = True
					real_distance = False
    
			
			#pause
			elif event.key == K_SPACE:
				if not pause:
					speed_temp = speed_multiplier
					speed_multiplier = 0
					pause = True
				elif pause:
					speed_multiplier = speed_temp
					pause = False
     
			#close
			elif event.key == K_ESCAPE:
				run = False
				pygame.quit()
				quit()
     
		if event.type == pygame.QUIT:
			run = False
			pygame.quit()
			quit()
	pygame.display.update()