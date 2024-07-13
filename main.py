import pygame
from screenClass import GameScreen
from playerClass import Player

# Main

screen_manager = GameScreen(700, 500, (181, 226, 245), "G&G Game")
player = Player()

# Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    # Aquí iría el resto del código de tu juego, como dibujar en la pantalla (screen)
    screen_manager.getScreen().blit(player.getImage(), (100,100)) 
    screen_manager.updateDisplay()

pygame.quit()