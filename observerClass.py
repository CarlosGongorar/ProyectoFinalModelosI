from abc import ABC, abstractmethod


class Panel(ABC):
    @abstractmethod
    def showStatus(self):
        pass
    
    @abstractmethod
    def update(self):
        pass

class CoinPanel(Panel):
    def __init__(self, player):
        self.player = player
        self.player.add_observer_score(self)
        self.score = 0

    def update(self, coins):
        self.score = coins
        #self.showStatus()
    
    def showStatus(self):
        #print(f"Total coins: {self.score}")
        return self.score

class LivesPanel(Panel):
    def __init__(self, player):
        self.player = player
        self.player.add_observer_lives(self)
        self.lives = 3

    def update(self, lives):
        self.lives = lives
        #self.showStatus()
    
    def showStatus(self):
        #print(f"Lives: {self.lives}")
        return self.lives