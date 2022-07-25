import pytest
import coverage
import sys
import numpy as np
import math

from KinematicsSolverApp import fk_solver


class TestFkSolver:

    def test_adding_two_numbers(self):
        the_sum = 2 + 2
        assert the_sum == 4

    def test_init(self, capsys):
        fk_solver.FkSolver(118, 150, 150, 54, 0)
        out, err = capsys.readouterr()
        assert out == "Links dimensions ok\n"

    def test_init_float(self, capsys):
        fk_solver.FkSolver(118.0, 150, 150, 54, 0)
        out, err = capsys.readouterr()
        assert out == "Links dimensions must be integers\n"

    def test_init_string(self, capsys):
        fk_solver.FkSolver(118, 150, 150, 54, 'aaa')
        out, err = capsys.readouterr()
        assert out == "Links dimensions must be integers\n"

    def test_init_minus(self, capsys):
        fk_solver.FkSolver(-100, 150, 150, 54, 0)
        out, err = capsys.readouterr()
        assert out == "Links dimensions must be equal or greater then 0\n"

    def test_dh(self):
        robot = fk_solver.FkSolver(118, 150, 150, 54, 0)
        result = robot.dh(0.0, 90.0, 0.0, 0.0)
        array_test = np.array([[0, 118, 0, 1.57079633],
                               [1.57079633, 0, 150, 0],
                               [0, 0, 150, 0],
                               [0, 0, 54, 0],
                               [-1.57079633, 0, 0, 0]])

        assert np.allclose(result[0], array_test)

    def test_solver(self):
        table_dh = np.array([[0, 118, 0, math.radians(90)],
                             [math.radians(90), 0, 150, 0],
                             [0, 0, 150, 0],
                             [0, 0, 54, 0],
                             [math.radians(-90), 0, 0, 0]])

        result = fk_solver.FkSolver.solver(table_dh)
        assert result == (90, [(0.0, 0.0, 268.0), (0.0, 0.0, 418.0), (0.0, 0.0, 472.0), (0.0, 0.0, 472.0)], 'Forward kinematics calculations ended successfully')

    def test_solver_zero_division(self):
        table_dh = np.array([[0, 118, 0, math.radians(90)],
                             [math.radians(90), 0, 150, 0],
                             [0, 0, 150, 0],
                             [0, 0, 0, 0],
                             [math.radians(-90), 0, 0, 0]])

        result = fk_solver.FkSolver.solver(table_dh)
        assert result == (0, [(0, 0, 0)], 'ZeroDivisionError: Table_dh[-2][-2] must be != 0')

    def test_hom_matrix(self):
        table_dh = np.array([[0, 118, 0, math.radians(90)],
                             [math.radians(90), 0, 150, 0],
                             [0, 0, 150, 0],
                             [0, 0, 54, 0],
                             [math.radians(-90), 0, 0, 0]])
        result = (fk_solver.FkSolver.hom_matrix(table_dh, 1))
        array_test = np.array([[6.12323400e-17, -1.00000000e+00, 0.00000000e+00, 9.18485099e-15],
                               [1.00000000e+00, 6.12323400e-17, -0.00000000e+00, 1.50000000e+02],
                               [0.00000000e+00, 0.00000000e+00, 1.00000000e+00, 0.00000000e+00],
                               [0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 1.00000000e+00]])

        assert np.allclose(result, array_test)

    def test_solve_auto(self):
        robot = fk_solver.FkSolver(118, 150, 150, 54, 0)
        result = robot.solve_auto(0.0, 90.0, 0.0, 0.0)
        assert result == (90, [(0.0, 0.0, 268.0), (0.0, 0.0, 418.0), (0.0, 0.0, 472.0), (0.0, 0.0, 472.0)],
                          'Forward kinematics calculations ended successfully')

    def test_solve_user(self):
        table_dh = np.array([[0, 118, 0, math.radians(90)],
                             [math.radians(90), 0, 150, 0],
                             [0, 0, 150, 0],
                             [0, 0, 54, 0],
                             [math.radians(-90), 0, 0, 0]])
        result = (fk_solver.FkSolver.solve_user(table_dh))
        assert result == (90, [(0.0, 0.0, 268.0), (0.0, 0.0, 418.0), (0.0, 0.0, 472.0), (0.0, 0.0, 472.0)],
                          'Forward kinematics calculations ended successfully')
