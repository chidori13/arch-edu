import unittest
from array import *
from math import sqrt

class EquationSolver:
    def __init__(self):
         pass
    def solve(self, a: float, b: float, c: float) ->  array:

        eps = 1e-5
        D = b*b-4*a*c

        if D < -eps:
            return array('f', [])
        elif D <= eps:
            return array('f', [-b/(2*a), -b/(2*a)])
        elif D > eps:
            return array('f', [-b+sqrt(D)/(2*a), -b-sqrt(D)/(2*a)])



class TestEquationSolve (unittest.TestCase):
    def setUp(self):
        self.equation = EquationSolver()

    def test_no_roots (self):
        self.assertEqual(self.equation.solve(1.0,0.0,1.0), array('f', []))

    def test_two_roots(self):
        self.assertEqual(self.equation.solve(1.0,0.0, -1.0), array('f', [1.0, -1.0]))

    def test_one_root(self):
        self.assertEqual(self.equation.solve(1.0, 2.0, 1.0), array('f', [-1.0, -1.0]))

