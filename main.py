import pygame
from screenClass import GameScreen
from playerClass import Player

# Main

screen_manager = GameScreen(700, 500, (181, 226, 245), "G&G Game"); # Game
clock = pygame.time.Clock()
player = Player();

# DELETE THAT 
player_x = 300
player_y = 0
player_speed = 0
player_acceleration = 0.2
player_width = 45
player_height = 51

# Platform Delete--------------------------------------------
platforms = [
    pygame.Rect(100, 300, 400, 50), # Platform
    pygame.Rect(100, 250, 50, 50), # Platform
    pygame.Rect(450, 250, 50, 50), # Platform

]

# Loop
running = True
while running:
    # Check for quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Player imput ----------------------------------------------------------------delete--------------------------------

    new_player_x = player_x
    new_player_y = player_y


    keys = pygame.key.get_pressed();
    if keys[pygame.K_a]:
        new_player_x -= 2
    if keys[pygame.K_d]:
        new_player_x += 2
    if keys[pygame.K_w] and player_on_ground:
        player_speed = -6

    # Horiazontal movement

    new_player_rect = pygame.Rect(new_player_x, player_y, player_width, player_height)
    x_collision = False

    #Check colitions
    for p in platforms:
        if p.colliderect(new_player_rect):
            x_collision = True
            break
    if x_collision == False:
        player_x = new_player_x

    # Vertical movement

    player_speed += player_acceleration
    new_player_y += player_speed

    new_player_rect = pygame.Rect(player_x, new_player_y, player_width, player_height)
    y_collision = False
    player_on_ground = False    

    #Check colitions
    for p in platforms:
        if p.colliderect(new_player_rect):
            y_collision = True
            player_speed = 0
            if p[1] > new_player_y:
                player_y = p[1] - player_height
                player_on_ground = True
            break

    if y_collision == False:
        player_y = new_player_y


    screen_manager.getScreen().fill((181, 226, 245)) # Limpia el fondo

    # Aquí iría el resto del código de tu juego, como dibujar en la pantalla (screen)

    # Platforms
    for p in platforms:
        pygame.draw.rect(screen_manager.getScreen(), (209, 206, 50), p)


    screen_manager.getScreen().blit(player.getImage(), (player_x,player_y)) # Player
    screen_manager.updateDisplay() # Update display

    clock.tick(60);

pygame.quit()