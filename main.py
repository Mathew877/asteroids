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
	dt = 0

	# create 2 groups for our objects
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()

	# add player to drawable and updatable groups
	Player.containers = (updatable, drawable) 
	# spawn player in center of screen
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	# group for the asteroids
	asteroids = pygame.sprite.Group()
	Asteroid.containers = (asteroids, updatable, drawable)

	AsteroidField.containers = updatable
	asteroid_field = AsteroidField()

	shots = pygame.sprite.Group()
	Shot.containers = (updatable, drawable)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			
		screen.fill("black")
		updatable.update(dt)

		# check for asteroid collisions
		for asteroid in asteroids:
			if player.has_collided(asteroid):
				print("Game over!")
				exit()

		for d in drawable:
			d.draw(screen)
		pygame.display.flip()

		dt = clock.tick(60) / 1000



if __name__ == "__main__":
	main()
