from abc import ABC, abstractmethod
import pygame

class Coin(ABC):
    def __init__(self, image_path):
        self.image_path = pygame.image.load(image_path);

    @abstractmethod
    def render(self):
        pass

class GoldCoin(Coin):
    def __init__(self, posX, posY, width, height):
        super().__init__("./images/coin/coin_0.png")

        self.coin_animation = [
            pygame.image.load("./images/coin/coin_0.png"),
            pygame.image.load("./images/coin/coin_1.png"),
            pygame.image.load("./images/coin/coin_2.png"),
            pygame.image.load("./images/coin/coin_3.png"),
            pygame.image.load("./images/coin/coin_4.png"),
            pygame.image.load("./images/coin/coin_5.png")
                            ]
        self.posX = posX;
        self.posY = posY;
        self.width = width;
        self.height = height;

    def render(self):
        return pygame.Rect(self.posX, self.posY, self.width, self.height)
    
    def getImage(self):
        return self.image_path;

    def getPosition(self):
        return (self.posX, self.posY);

    def getAnimation(self):
        return self.coin_animation;


class CoinFactory():
    @staticmethod
    def create(coin_type, posX, posY, width, height):
        if coin_type == "gold":
            return GoldCoin(posX, posY, width, height)
        else:
            raise ValueError("Invalid coin type")