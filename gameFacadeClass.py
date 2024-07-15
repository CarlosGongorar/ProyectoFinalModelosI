import pygame

class Sound:
    def __init__(self):
        pygame.mixer.init();

    def play_music(self, music_file):
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play(-1)
    
    def play_jump_sound(self):
        jumpSound = pygame.mixer.Sound("./sounds/soundefects/jumpsound.mp3")
        jumpSound.play()
    
    def play_coin_sound(self):
        coinSound = pygame.mixer.Sound("./sounds/soundefects/coinsound.mp3")
        coinSound.play()
    
    def play_enemy_sound(self):
        enemySound = pygame.mixer.Sound("./sounds/soundefects/enemyhitsound.mp3")
        enemySound.play()

    def play_fall_sound(self):
        fallSound = pygame.mixer.Sound("./sounds/soundefects/fallsound.mp3")
        fallSound.play()

    def soundManager(self, sound):
        if sound == "coin":
            self.play_coin_sound()
        elif sound == "jump":
            self.play_jump_sound()
        elif sound == "enemy":
            self.play_enemy_sound()
        elif sound == "fall":
            self.play_fall_sound()

class GameFacade():
    def __init__(self):
        self.sound = Sound()
    
    def start_game(self):
        self.sound.play_music("./sounds/music/music.mp3")
        return "run"
    
    def sound_play(self, action):
        self.sound.soundManager(action);


