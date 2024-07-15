from abc import ABC


class GameState(ABC):
    def action(self, context):
        pass

class PlayState(GameState):
    def action(self, context):
        return "run"

class LoseState(GameState):
    def action(self, context):
        return "lose"

class WinState(GameState):
    def action(self, context):
        return "win"

class Game():
    def __init__(self):
        self.state = None;

    def change_state(self, state):
        self.state = state
    
    def execute_action(self):
        return self.state.action(self)
