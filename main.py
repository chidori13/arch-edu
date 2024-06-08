from abc import ABC
from unittest.mock import Mock


class Vector:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    @staticmethod
    def __operate(f, a, b):
        return Vector(*f(a, b))
    def plus(self, other):
        return Vector.__operate(lambda a, b: (a.x + b.x, a.y + b.y), self, other)

class Movable(ABC):
    def __init__(self):
        pass
    def get_location(self)->Vector:
        pass
    def get_velocity(self) -> Vector:
        pass
    def set_location(self, new_value: Vector):
        pass


class Move:
    def __init__(self, movable: Movable):
        self.movable = movable

    def execute(self):
        self.movable.set_location(Vector.plus(self.movable.get_location(), self.movable.get_velocity()))


def main():
    movable_mock = Mock(spec=Movable)
    movable_mock.get_location.return_value = Vector(12, 5)
    movable_mock.get_velocity.return_value = Vector(-7, 3)
    move_command = Move(movable_mock)
    move_command.execute()
    movable_mock.set_location.assert_called_with(Vector(5,8))
