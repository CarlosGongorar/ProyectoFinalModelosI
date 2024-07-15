import pygame
import time
from screenClass import GameScreen
from playerClass import Player
from controlsClass import InputHandler, CommandJumpMove, CommandLeftMove, CommandRightMove
from observerClass import CoinPanel, LivesPanel
from enemieClass import FactoryEnemySpike, MoveRightStrategy, MoveLeftStrategy
from gameStateClass import Game, PlayState, LoseState, WinState
from dinamicClass import PlayerDirection, Left, Right, PlayerAction, IdleState, WalkingState, Animation
from coinClass import CoinFactory
from gameFacadeClass import GameFacade
# Main

game = Game();
gameLose = LoseState();
gamePlaying = PlayState();
gameWin = WinState();
gameFacade = GameFacade();

screen_manager = GameScreen(700, 500, (181, 226, 245), "G&G Game"); # Game
clock = pygame.time.Clock()

player = Player();
playerdirection = PlayerDirection();
playeraction = PlayerAction();
playerWalking = WalkingState();
playerIdle = IdleState();
playerLeft = Left();
playerRight = Right();

playerdirection.change_direction(playerRight);
playeraction.change_action(playerIdle);

coinpanel = CoinPanel(player);
livespanel = LivesPanel(player);

spikeEnemyFactory = FactoryEnemySpike();
coinFactory = CoinFactory();
font = pygame.font.Font(pygame.font.get_default_font(), 24);


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

# Platform Delete--------------------------------------------
platforms = [
    pygame.Rect(100, 300, 400, 20), # Main Platform
    pygame.Rect(100, 250, 50, 50), # Platform
    pygame.Rect(450, 250, 50, 50), # Platform
    pygame.Rect(100, 460, 400, 50), # Bottom Platform
    ]

# Coins ------------------------------------------------------------------------
coin1 = coinFactory.create("gold", 100, 200, 23, 23);
coin2 = coinFactory.create("gold", 300, 200, 23, 23);
coin3 = coinFactory.create("gold", 500, 200, 23, 23);
coin4 = coinFactory.create("gold", 200, 100, 23, 23);
coin5 = coinFactory.create("gold", 400, 100, 23, 23);
coin6 = coinFactory.create("gold", 300, 350, 23, 23);

coins = [
    coin1, 
    coin2, 
    coin3,
    coin4, 
    coin5,
    coin6
    ]

coin_animator = Animation(coin1.getAnimation());
player_walkinganimator = Animation(player.getWalkingAnimation());
player_idleanimator = Animation(player.getIdleAnimation());

# ----------------------------- Lives ------------------------------------------
lives_image = pygame.image.load("./images/lives/heart.png")
lives = livespanel.showStatus()
# ------------------------------------ Enemies List ----------------------------


enemyA = spikeEnemyFactory.create("A", 150, 274, 50, 26, MoveRightStrategy());
enemy2A = spikeEnemyFactory.create("A", 400, 434, 50, 26, MoveLeftStrategy());
enemy3A = spikeEnemyFactory.create("A", 150, 434, 50, 26, MoveRightStrategy());
enemyB = spikeEnemyFactory.create("B", 400, 274, 50, 26, None);
enemy2B = spikeEnemyFactory.create("B", 150, 274, 50, 26, None);
enemies = [
    enemyA,
    enemy2A,
    enemy3A,
    enemyB,
    enemy2B
]
# Fall Barrier --------------------------------

falling_barrier = [pygame.Rect(0, 560, 700, 50)]
# Loop

game.change_state(gamePlaying)
gameState = gameFacade.start_game()

while gameState is game.execute_action():

    # Check for quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameState = False
    new_player_x = player_x
    new_player_y = player_y

    #-------------------------- Updaters -------------------------
    coin_animator.update()
    player_idleanimator.update()
    player_walkinganimator.update()
    screen_manager.updateDisplay()

    #----------------------- Controls------------------------

    keys = pygame.key.get_pressed();

    if keys[pygame.K_a]:
        playerdirection.change_direction(playerLeft)
        playeraction.change_action(playerWalking)
        new_player_x -= 2
        input_handler.handleInput(pygame.K_a)
        

    if keys[pygame.K_d]:
        playerdirection.change_direction(playerRight)
        playeraction.change_action(playerWalking)
        new_player_x += 2
        input_handler.handleInput(pygame.K_d)

    if not keys[pygame.K_a] and not keys[pygame.K_d]:
        playeraction.change_action(playerIdle)

    if keys[pygame.K_w] and player_on_ground:
        gameFacade.sound_play("jump")
        player_speed = -6
        input_handler.handleInput(pygame.K_w)

    playeraction.execute_action();

    # Horiazontal movement
    new_player_rect = pygame.Rect(new_player_x, player_y, player_width, player_height)
    x_collision = False

    

    # Vertical movement

    player_speed += player_acceleration
    new_player_y += player_speed

    new_player_rect = pygame.Rect(player_x, new_player_y, player_width, player_height)
    y_collision = False
    player_on_ground = False    

    #---------------------------------------------------------
    #------------------------Colitions------------------------
    #---------------------------------------------------------

    #Check X colitions
    for p in platforms:
        if p.colliderect(new_player_rect):
            x_collision = True
            break
    if x_collision == False:
        player_x = new_player_x
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

    # Coins Colition
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    for c in coins:
        coinColition = c.render();
        if coinColition.colliderect(player_rect):
            gameFacade.sound_play("coin")
            coins.remove(c)
            player.colectCoin()
            if coinpanel.showStatus() == 6:
                game.change_state(gameWin)
                print("################# Ganaste! #################")
    
    # Enemy Colition

    for e in enemies:
        enemyColition = e.render()
        if enemyColition.colliderect(player_rect):
            gameFacade.sound_play("enemy")
            player.loseLives()
            player_x = 300
            player_y = 0
            player_speed = 0
            if livespanel.showStatus() <= 0:
                game.change_state(gameLose) 
                print("################# Perdiste :( #################")
    
    for f in falling_barrier:
        if f.colliderect(new_player_rect):
            gameFacade.sound_play("fall")
            player.loseLives()
            pygame.time.delay(1500)
            player_x = 300
            player_y = 0
            player_speed = 0
            if livespanel.showStatus() <= 0:
                game.change_state(gameLose)
                print("################# Perdiste :( #################")
    #----------------------------------------------------------------
    #----------------------------DRAWS-------------------------------
    #----------------------------------------------------------------
    screen_manager.getScreen().fill((181, 226, 245)) # Limpia el fondo

    # Platforms
    for p in platforms:
        pygame.draw.rect(screen_manager.getScreen(), (209, 206, 50), p)

    # Coins

    for c in coins:
        x, y = c.getPosition()
        coinImage = c.getImage()
        coin_animator.draw(screen_manager.getScreen(), x, y, False, False)
    
    # Enemies

    for e in enemies:
        x, y = e.getPosition()
        enemyImage = e.getImage()
        e.move();

        screen_manager.getScreen().blit(enemyImage,(x, y))

    for f in falling_barrier:
        pygame.draw.rect(screen_manager.getScreen(), (255, 0, 0), f)

    
    

    # --------------------- HUD --------------------------------
    # Score
    score_text = font.render("Score: " + str(coinpanel.showStatus()), True, (255, 255, 255),(181, 226, 245))
    score_text_rect = score_text.get_rect()
    screen_manager.getScreen().blit(score_text, score_text_rect)
    
    
    # Lives
    for l in range((livespanel.showStatus())):
        screen_manager.getScreen().blit(lives_image,(200 + (l*50), 10))


    #----------------------------Player Render------------------------------
    
    if playeraction.execute_action() == "idle" and playerdirection.execute_action() == "right":
        player_idleanimator.draw(screen_manager.getScreen(), player_x, player_y, False, False)

    elif playeraction.execute_action() == "idle" and playerdirection.execute_action() == "left":
        player_idleanimator.draw(screen_manager.getScreen(), player_x, player_y, True, False)

    elif playerdirection.execute_action() == "right" and playeraction.execute_action() == "walking":
        player_walkinganimator.draw(screen_manager.getScreen(), player_x, player_y, False, False)
    
    elif playerdirection.execute_action() == "left" and playeraction.execute_action() == "walking":
        player_walkinganimator.draw(screen_manager.getScreen(), player_x, player_y, True, False)

    clock.tick(60);



pygame.quit()