import pygame

class Player:

    # Singleton Creation
    _instance = None;

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls);
        return cls._instance
    
    def __init__(self):

        # Para que solo ocurra una vez por instancia
        if hasattr(self, '_initialized'):
            return
        self._initialized = True

        self.image_path = "./images/dinosprites/dinovita/vita_00.png" # Ruta de la imagen
        self.load_image() #Atributo imagen
        self.player_x = 300
        self.player_y = 0
        self.player_speed = 0
        self.player_acceleration = 0.2
        self.player_width = 45
        self.player_height = 51
        self.observers = [];
        self.score = 0;
        self.player_on_ground = False;

    def load_image(self): # Cargado de imagen
        try:
            self.image = pygame.image.load(self.image_path);
        except pygame.error as e:
            print("Error 01: Cargado de imagen de jugador");
            self.image = None;
    
    def moveRight(self):
        self.player_x += 2;
    
    def moveLeft(self):
        self.player_x -= 2;
    
    def jump(self):
        if self.player_on_ground:
            self.player_speed = -6;
    
    def colectCoin(self):
        self.score += 1;
        self.notify_observers();
    
    def add_observer(self, observer):
        self.observers.append(observer);
    
    def remove_observer(self, observer):
        self.observers.remove(observer);
    
    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.score);

    # Retorna atributo imagen
    def getImage(self):
        return self.image;

    def getPlayerX(self):
        return self.player_x;

    def getPlayerY(self):
        return self.player_y;

    def getPlayerSpeed(self):
        return self.player_speed;

    def getPlayerAcceleration(self):
        return self.player_acceleration;

    def getPlayerWidth(self):
        return self.player_width;

    def getPlayerHeight(self):
        return self.player_height;

    def getPlayerOnGround(self):
        return self.player_on_ground;

    def setPlayerX(self, x):
        self.player_x = x;

    def setPlayerY(self, y):
        self.player_y = y;

    def setPlayerSpeed(self, speed):
        self.player_speed = speed;

    def setPlayerAcceleration(self, acceleration):
        self.player_acceleration = acceleration;

    def setPlayerWidth(self, width):
        self.player_width = width;

    def setPlayerHeight(self, height):
        self.player_height = height;

    def setPlayerOnGround(self, on_ground):
        self.player_on_ground = on_ground;

