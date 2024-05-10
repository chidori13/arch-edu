import unittest
from array import *
from math import sqrt
from math import fabs
from math import isnan
from numpy import nan

class EquationSolver:
    def __init__(self):
         pass
    def solve(self, a: float, b: float, c: float) -> array:

        eps = 1e-5

        if fabs(a) <= eps:
            raise ValueError(f"Уравнение не является квадратным")

        if isnan(a) or isnan(b) or isnan(c):
            raise ValueError(f"Значения коэффициентов не являются числами")

        D = b*b-4*a*c

        if D < -eps:
            return array('f', [])
        elif fabs(D) <= eps:
            return array('f', [-b/(2*a), -b/(2*a)])
        elif D > eps:
            return array('f', [-b+sqrt(D)/(2*a), -b-sqrt(D)/(2*a)])



class TestEquationSolve (unittest.TestCase):
    def setUp(self):
        self.equation = EquationSolver()

    def test_no_roots (self):
        self.assertEqual(self.equation.solve(1.0,0.0,1.0), array('f', []), msg='Нет корней')

    def test_two_roots(self):
        self.assertEqual(self.equation.solve(1.0,0.0, -1.0), array('f', [1.0, -1.0]), msg = 'Два различных корня')

    def test_one_root(self):
        self.assertEqual(self.equation.solve(1.0, 2.0, 1.0), array('f', [-1.0, -1.0]), msg = 'Два равных корня')

    def test_not_quadratic_equation(self):
        with self.assertRaises(ValueError):
            result = self.equation.solve(0.0, 1.0, 1.0)

    def test_coefficients_check(self):
        with self.assertRaises(ValueError):
            result = self.equation.solve(nan, 1.0, 1.0)


def main():
    test_solver = TestEquationSolve()
    test_solver.test_no_roots()
    test_solver.test_two_roots()
    test_solver.test_one_root()
    test_solver.test_not_quadratic_equation()
    test_solver.test_coefficients_check()