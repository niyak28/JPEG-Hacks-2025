import pygame
from random import randint
from os.path import join

pygame.init()


# initialize window
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
running = True
pygame.display.set_caption("space shooter template")


# surface
surf = pygame.Surface((100, 200))
surf.fill("blue")
x = 100

# import surface
player_surf = pygame.image.load(join("space shooter", "images", "player.png")).convert_alpha()
player_rect = player_surf.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
player_direction = 1

star_surf = pygame.image.load(join("space shooter", "images", "star.png")).convert_alpha()
star_positions = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for i in range(20)]

meteor_surf = pygame.image.load(join("space shooter", "images", "meteor.png")).convert_alpha()
meteor_rect = meteor_surf.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

laser_surf = pygame.image.load(join("space shooter", "images", "laser.png")).convert_alpha()
laser_rect = laser_surf.get_rect(bottomleft = (20, WINDOW_HEIGHT - 20))


# rect


while True:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # draw game
    display_surface.fill("darkgray")
    for pos in star_positions:
        display_surface.blit(star_surf, pos)
    
    display_surface.blit(meteor_surf, meteor_rect)
    display_surface.blit(laser_surf, laser_rect)
    
    # move spaceship
    player_rect.x += player_direction * 2
    if player_rect.right > WINDOW_WIDTH or player_rect.left < 0:    
        player_direction *= -1
    display_surface.blit(player_surf, player_rect) # show the passed surface and where to place it


    pygame.display.update() # .flip() does the same thing but for part of the window


# un-initializes game and makes sure it closes properly
pygame.quit