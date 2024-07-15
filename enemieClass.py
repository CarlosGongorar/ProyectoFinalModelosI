from abc import ABC, abstractmethod
import pygame

class Enemy(ABC):
    def __init__(self, image_path):
        self.image_path = pygame.image.load(image_path);
    def render(self):
        pass

class SpikeEnemyA(Enemy):
    def __init__(self, posX, posY, witdh, height):
        super().__init__("./images/enemies/spikemonsterA.png")
        self.posX = posX;
        self.posY = posY;
        self.width = witdh;
        self.height = height;
    
    def render(self):
        return pygame.Rect(self.posX, self.posY, self.width, self.height)

    def getImage(self):
        return self.image_path;

    def getPosition(self):
        return (self.posX, self.posY);

class SpikeEnemyB(Enemy):
    def __init__(self, posX, posY, witdh, height):
        super().__init__("./images/enemies/spikemonsterB.png")
        self.posX = posX;
        self.posY = posY;
        self.width = witdh;
        self.height = height;
    
    def render(self):
        return pygame.Rect(self.posX, self.posY, self.width, self.height)
    
    def getImage(self):
        return self.image_path;

    def getPosition(self):
        return (self.posX, self.posY);



class FactoryEnemySpike():
    @staticmethod
    def create(enemy_type, posX, posY, witdh, height):
        if enemy_type == "A":
            return SpikeEnemyA(posX, posY, witdh, height)
        elif enemy_type == "B":
            return SpikeEnemyB(posX, posY, witdh, height)
        else:
            raise ValueError("Invalid enemy type")