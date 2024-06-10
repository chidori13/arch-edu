import unittest
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


class TestMove():
    def test_usual_move(self):
        movable_mock = Mock(spec=Movable)
        movable_mock.get_location.return_value = Vector(12, 5)
        movable_mock.get_velocity.return_value = Vector(-7, 3)
        move_command = Move(movable_mock)
        move_command.execute()
        assert(movable_mock.get_location, Vector(5,8))

    def test_impossible_get_location(self):
        movable_mock = Mock(spec=Movable)
        attrs = {'get_velocity.return_value': Vector(1,1), 'get_location.side_effect': ValueError}
        movable_mock.configure_mock(**attrs)
        move_command = Move(movable_mock)
        try:
            move_command.execute()
        except ValueError:
            print(f'Невозможно сдвинуть объект без первоначального положения')

    def test_impossible_get_velocity(self):
        movable_mock = Mock(spec=Movable)
        attrs = {'get_location.return_value': Vector(1,1), 'get_velocity.side_effect': ValueError}
        movable_mock.configure_mock(**attrs)
        move_command = Move(movable_mock)
        try:
            move_command.execute()
        except ValueError:
            print(f'Невозможно сдвинуть объект, не зная его скорости')

    def test_impossible_set_location(self):
        movable_mock = Mock(spec=Movable)
        attrs = {'get_location.return_value': Vector(1, 1), 'get_velocity.return_value': Vector(1, 1),'set_location.side_effect': Exception}
        movable_mock.configure_mock(**attrs)
        move_command = Move(movable_mock)
        try:
            move_command.execute()
        except Exception:
            print(f'Невозможно изменить положение объекта в пространстве')


class Angle:
    def __init__(self, direction: int, n: int):
        self.n = n
        self.direction = direction

    def __operate(f, a, b):
        return Angle(*f(a, b))


class Rotable(ABC):
    def get_angle()->Angle:
    pass
    def set_angle(new_value: Angle):
    pass
    def get_angular_velocity()->Angle:
    pass

class Rotate:
    def __init__(self, rotable: Rotable):
        self.rotable = rotable

    def execute(self):
        self.rotable.set_angle(Angle.plus(self._rotable.get_angle(), self._rotable.get_angular_velocity()))