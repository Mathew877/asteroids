# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0
	# create 2 groups for our objects
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	# add player to both groups
	Player.containers = (updatable, drawable) 
	# spawn player in center of screen
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			
		screen.fill("black")
		updatable.update(dt)
		for d in drawable:
			d.draw(screen)
		pygame.display.flip()

		dt = clock.tick(60) / 1000



if __name__ == "__main__":
	main()
