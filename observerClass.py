class CoinPanel:
    def __init__(self, player):
        self.player = player
        self.player.add_observer(self)
        self.score = 0

    def update(self, coins):
        self.score = coins
        self.showStatus()
    
    def showStatus(self):
        print(f"Total coins: {self.score}")