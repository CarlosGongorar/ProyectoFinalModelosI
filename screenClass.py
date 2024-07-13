import pygame

class GameScreen():
    
    # Singleton Creation
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, width, height, color= (0, 0, 0), name=""):
        
        # Para que solo ocurra una vez por instancia
        if hasattr(self, '_initialized'):
            return
        self._initialized = True

        self.width = width; # Ancho
        self.height = height; # Altura
        self.color = color; # Color
        self.name = name; # Nombre de pestaña

        # Creacion de la ventana
        # init
        pygame.init();
        self.screen = pygame.display.set_mode((self.width, self.height));
        pygame.display.set_caption(self.name);
        self.screen.fill(self.color);
    
    def getScreen(self):
        return self.screen;

    def getSize(self):
        return self.width, self.height;
    
    # Actualiza elementos dibujados en pantalla

    def updateDisplay(self):
        pygame.display.flip(); 
