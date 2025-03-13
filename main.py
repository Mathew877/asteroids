import sys
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()

	# create groups for our objects
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	# add classes to their appropriate containers
	Asteroid.containers = (asteroids, updatable, drawable)
	Shot.containers = (shots, updatable, drawable)
	AsteroidField.containers = updatable
	asteroid_field = AsteroidField()
	# add player to drawable and updatable groups
	Player.containers = (updatable, drawable) 
	# spawn player in center of screen
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	dt = 0

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			
		updatable.update(dt)

		# check for asteroid collisions
		for asteroid in asteroids:
			if player.has_collided(asteroid):
				print("Game over!")
				sys.exit()

			for shot in shots:
				if shot.has_collided(asteroid):
					asteroid.split()


		screen.fill("black")

		for d in drawable:
			d.draw(screen)

		pygame.display.flip()

		dt = clock.tick(60) / 1000



if __name__ == "__main__":
	main()
