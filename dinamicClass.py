from abc import ABC
import pygame

#--------------------- Player Direction --------------------

class Direction(ABC):
    def action(self, context):
        pass

class Right(Direction):
    def action(self, context):
        return "right"

class Left(Direction):
    def action(self, context):
        return "left"

class PlayerDirection():
    def __init__(self):
        self.direction = None;

    def change_direction(self, direction):
        self.direction = direction

    def execute_action(self):
        return self.direction.action(self)
    
#------------------------ Player State ------------------------------

class PlayerState(ABC):
    def action(self, context):
        pass

class WalkingState(PlayerState):
    def action(self, context):
        return "walking"
    
class IdleState(PlayerState):
    def action(self, context):	
        return "idle"

class PlayerAction():
    def __init__(self):
        self.action = None;

    def change_action(self, action):
        self.action = action;

    def execute_action(self):
        return self.action.action(self)
    
#--------------------- Animator --------------------

class Animation():
    def __init__(self, imageList):
        self.imageList = imageList;
        self.imageIndex = 0;
        self.animationTimer = 0;
        self.animationSpeed = 6;

    def update(self):
        self.animationTimer += 1;
        if self.animationTimer >= self.animationSpeed:
            self.animationTimer = 0;
            self.imageIndex += 1;
            if self.imageIndex >= len(self.imageList) - 1:
                self.imageIndex = 0;

    def draw(self, screen, x, y, flipX, flipY):
        screen.blit(self.imageList[self.imageIndex],(x, y))
        screen.blit(pygame.transform.flip(self.imageList[self.imageIndex], flipX, False), (x, y))
