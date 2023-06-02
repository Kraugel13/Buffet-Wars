
import pygame

#intialize
pygame.init()

#create screen
screen = pygame.display.set_mode((800, 600))

#Title and Icon
pygame.display.set_caption("Buffet Wars")

# game loop
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	