from abc import ABC, abstractmethod
import pygame
class CommandControl(ABC):
    @abstractmethod
    def execute_command(self):
        pass

class CommandRightMove(CommandControl):
    def __init__(self, player):
        self.player = player

    def execute_command(self):
        self.player.moveRight()

class CommandLeftMove(CommandControl):
    def __init__(self, player):
        self.player = player
    
    def execute_command(self):
        self.player.moveLeft()

class CommandJumpMove(CommandControl):
    def __init__(self, player):
        self.player = player
    
    def execute_command(self):
        self.player.jump()

class InputHandler():
    def __init__(self):
        self.commands = {}

    def assignCommand(self, key, command):
        self.commands[key] = command

    def handleInput(self, key):
        if key in self.commands:
            self.commands[key].execute_command()
        else:
            print("Tecla no asignada")