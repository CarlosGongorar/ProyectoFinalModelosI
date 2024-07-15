from abc import ABC

class Direction(ABC):
    def action(self, context):
        pass

class Right(Direction):
    def action(self, context):
        return "right"

class Left(Direction):
    def action(self, context):
        return "left"

class PlayerDirection(Direction):
    def __init__(self):
        self.direction = None;

    def change_direction(self, direction):
        self.direction = direction

    def execute_action(self):
        return self.direction.action(self)
