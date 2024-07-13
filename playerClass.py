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

    def load_image(self): # Cargado de imagen
        try:
            self.image = pygame.image.load(self.image_path);
        except pygame.error as e:
            print("Error 01: Cargado de imagen de jugador");
            self.image = None;
    
    # Retorna atributo imagen
    def getImage(self):
        return self.image;
