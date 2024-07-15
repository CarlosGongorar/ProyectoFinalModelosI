from abc import ABC, abstractmethod
import pygame

class Enemy(ABC):
    def __init__(self, image_path):
        self.image_path = pygame.image.load(image_path);
        
    def render(self):
        pass

class SpikeEnemyA(Enemy):
    def __init__(self, posX, posY, witdh, height, enemy_strategy):
        super().__init__("./images/enemies/spikemonsterA.png")
        self.posX = posX;
        self.posY = posY;
        self.width = witdh;
        self.height = height;
        self.enemy_strategy = enemy_strategy;
    
    def render(self):
        return pygame.Rect(self.posX, self.posY, self.width, self.height)
    
    def move(self):
        self.enemy_strategy.move(self)

    def setMovementStrategy(self, enemy_strategy):
        self.enemy_strategy = enemy_strategy

    def getImage(self):
        return self.image_path;

    def getPosition(self):
        return (self.posX, self.posY);

    def setPosition(self, posX, posY):
        self.posX = posX;
        self.posY = posY;

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

    def move(self):
        pass

class FactoryEnemySpike():
    @staticmethod
    def create(enemy_type, posX, posY, witdh, height, movement_strategy):
        if enemy_type == "A":
            return SpikeEnemyA(posX, posY, witdh, height, movement_strategy)
        elif enemy_type == "B":
            return SpikeEnemyB(posX, posY, witdh, height)
        else:
            raise ValueError("Invalid enemy type")
        
class MovementsStrategy(ABC):
    @abstractmethod
    def move(self, enemy):
        pass

class MoveLeftStrategy(MovementsStrategy):
    def move(self, enemy):
        x, y = enemy.getPosition()
        x -= 1
        enemy.setPosition(x, y)
        if x == 150:
            enemy.setMovementStrategy(MoveRightStrategy())

class MoveRightStrategy(MovementsStrategy):
    def move(self, enemy):
            x, y = enemy.getPosition()
            x += 1
            enemy.setPosition(x, y)
            if x == 400:
                enemy.setMovementStrategy(MoveLeftStrategy())
