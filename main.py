from abc import ABC
import array from numpy


class Vector:
    @staticmethod
    def plus(a: Vector, b: Vector)->Vector:
class Movable(ABC):
    def get_location() -> Vector:

    def set_location(new_value: Vector):
    def get_velocity() -> Vector:

class Move:
    def __init__(self, _movable: Movable):
        _movable.set_location(Vector.plus(_movable.get_location(), _movable.get_velocity()))

