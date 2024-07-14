import pygame
from screenClass import GameScreen
from playerClass import Player
from controlsClass import InputHandler, CommandJumpMove, CommandLeftMove, CommandRightMove
from observerClass import CoinPanel
# Main

screen_manager = GameScreen(700, 500, (181, 226, 245), "G&G Game"); # Game
clock = pygame.time.Clock()
player = Player();
coinpanel = CoinPanel(player)


# KEY BIND
input_handler = InputHandler();
input_handler.assignCommand(pygame.K_w, CommandJumpMove(player))
input_handler.assignCommand(pygame.K_a, CommandLeftMove(player))
input_handler.assignCommand(pygame.K_d, CommandRightMove(player))

player_x = player.getPlayerX()
player_y = player.getPlayerY()
player_speed = player.getPlayerSpeed()
player_acceleration = player.getPlayerAcceleration()
player_width = player.getPlayerWidth()
player_height = player.getPlayerHeight()

score = 0
# Platform Delete--------------------------------------------
platforms = [
    pygame.Rect(100, 300, 400, 50), # Platform
    pygame.Rect(100, 250, 50, 50), # Platform
    pygame.Rect(450, 250, 50, 50), # Platform

]

# Coins ---------------------------------------------------------------- Put in class
coin_image = pygame.image.load("./images/coin/coin_0.png")
coins = [
        pygame.Rect(100, 200, 23, 23),
        pygame.Rect(300, 200, 23, 23),
        pygame.Rect(500, 200, 23, 23),
        pygame.Rect(200, 100, 23, 23),
        pygame.Rect(400, 100, 23, 23)
    ]

# Loop
running = True
while running:
    # Check for quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    new_player_x = player_x
    new_player_y = player_y

    #Controls

    keys = pygame.key.get_pressed();

    if keys[pygame.K_a]:
        new_player_x -= 2
        input_handler.handleInput(pygame.K_a)
    if keys[pygame.K_d]:
        new_player_x += 2
        input_handler.handleInput(pygame.K_d)
    if keys[pygame.K_w] and player_on_ground:
        player_speed = -6
        input_handler.handleInput(pygame.K_w)

    # Horiazontal movement
    new_player_rect = pygame.Rect(new_player_x, player_y, player_width, player_height)
    x_collision = False

    #Check X colitions
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

    #Check Y colitions
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

    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    
    for c in coins:
        if c.colliderect(player_rect):
            coins.remove(c)
            player.colectCoin()

    screen_manager.getScreen().fill((181, 226, 245)) # Limpia el fondo

    # Platforms
    for p in platforms:
        pygame.draw.rect(screen_manager.getScreen(), (209, 206, 50), p)

    for c in coins:
        screen_manager.getScreen().blit(coin_image,(c[0],c[1]))

    screen_manager.getScreen().blit(player.getImage(), (player_x, player_y)) # Player
    screen_manager.updateDisplay() # Update display

    clock.tick(60);

pygame.quit()