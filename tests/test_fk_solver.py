import pytest
import coverage
import sys
import numpy as np
import math

from KinematicsSolverApp.modules import fk_solver


class TestFkSolver:

    def test_adding_two_numbers(self):
        the_sum = 2 + 2
        assert the_sum == 4

    def test_check_input_param_ok(self, capsys):
        links_test = {"link1": [118, -80, 80],
                      "link2": [150, 5, 175],
                      "link3": [150, - 115, 55],
                      "link4": [54, -85, 85],
                      "link5": [0, 0, 0]}
        fk_solver.FkSolver(links_test)
        out, err = capsys.readouterr()
        assert out == "Links dimensions ok\n"

    def test_check_input_param_str(self, capsys):
        links_test = {"link1": ["a", -80, 80],
                      "link2": [150, 5, 175],
                      "link3": [150, - 115, 55],
                      "link4": [54, -85, 85],
                      "link5": [0, 0, 0]}
        fk_solver.FkSolver(links_test)
        out, err = capsys.readouterr()
        assert out == "Links dimensions must be integers\n"

    def test_check_input_param_min_length(self, capsys):
        links_test = {"link1": [-100, -80, 80],
                      "link2": [150, 5, 175],
                      "link3": [150, - 115, 55],
                      "link4": [54, -85, 85],
                      "link5": [0, 0, 0]}
        fk_solver.FkSolver(links_test)
        out, err = capsys.readouterr()
        assert out == "Links dimensions must be equal or greater then 0\n"

    def test_dh(self):
        links_test = {"link1": [118, -80, 80],
                      "link2": [150, 5, 175],
                      "link3": [150, - 115, 55],
                      "link4": [54, -85, 85],
                      "link5": [0, 0, 0]}
        robot = fk_solver.FkSolver(links_test)
        result = robot.fk_dh(0.0, 90.0, 0.0, 0.0)
        array_test = np.array([[0, 118, 0, 1.57079633],
                               [1.57079633, 0, 150, 0],
                               [0, 0, 150, 0],
                               [0, 0, 54, 0],
                               [-1.57079633, 0, 0, 0]])

        assert np.allclose(result[0], array_test)

    def test_dh_int_not_float(self):
        links_test = {"link1": [118, -80, 80],
                      "link2": [150, 5, 175],
                      "link3": [150, - 115, 55],
                      "link4": [54, -85, 85],
                      "link5": [0, 0, 0]}
        robot = fk_solver.FkSolver(links_test)
        result = robot.fk_dh(0, 90.0, 0.0, 0.0)
        assert result[1] == "Thetas values must be float"

    def test_dh_string_not_float(self):
        links_test = {"link1": [118, -80, 80],
                      "link2": [150, 5, 175],
                      "link3": [150, - 115, 55],
                      "link4": [54, -85, 85],
                      "link5": [0, 0, 0]}
        robot = fk_solver.FkSolver(links_test)
        result = robot.fk_dh("a", 90.0, 0.0, 0.0)
        assert result[1] == "Thetas values must be float"

    def test_solver(self):
        table_dh = np.array([[0, 118, 0, math.radians(90)],
                             [math.radians(90), 0, 150, 0],
                             [0, 0, 150, 0],
                             [0, 0, 54, 0],
                             [math.radians(-90), 0, 0, 0]])

        result = fk_solver.FkSolver.fk_solver(table_dh)
        assert result == (90, [(0.0, 0.0, 268.0), (0.0, 0.0, 418.0), (0.0, 0.0, 472.0), (0.0, 0.0, 472.0)], 'Forward kinematics calculations ended successfully')

    def test_solver_zero_division(self):
        table_dh = np.array([[0, 118, 0, math.radians(90)],
                             [math.radians(90), 0, 150, 0],
                             [0, 0, 150, 0],
                             [0, 0, 0, 0],
                             [math.radians(-90), 0, 0, 0]])

        result = fk_solver.FkSolver.fk_solver(table_dh)
        assert result == (0, [(0, 0, 0)], 'ZeroDivisionError: Table_dh[-2][-2] must be != 0')

    def test_hom_matrix(self):
        table_dh = np.array([[0, 118, 0, math.radians(90)],
                             [math.radians(90), 0, 150, 0],
                             [0, 0, 150, 0],
                             [0, 0, 54, 0],
                             [math.radians(-90), 0, 0, 0]])
        result = (fk_solver.FkSolver.fk_hom_matrix(table_dh, 1))
        array_test = np.array([[6.12323400e-17, -1.00000000e+00, 0.00000000e+00, 9.18485099e-15],
                               [1.00000000e+00, 6.12323400e-17, -0.00000000e+00, 1.50000000e+02],
                               [0.00000000e+00, 0.00000000e+00, 1.00000000e+00, 0.00000000e+00],
                               [0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 1.00000000e+00]])

        assert np.allclose(result, array_test)

    def test_solve_auto(self):
        links_test = {"link1": [118, -80, 80],
                      "link2": [150, 5, 175],
                      "link3": [150, - 115, 55],
                      "link4": [54, -85, 85],
                      "link5": [0, 0, 0]}
        robot = fk_solver.FkSolver(links_test)
        result = robot.fk_solve_auto(0.0, 90.0, 0.0, 0.0)
        assert result == (90, [(0.0, 0.0, 268.0), (0.0, 0.0, 418.0), (0.0, 0.0, 472.0), (0.0, 0.0, 472.0)],
                          'Forward kinematics calculations ended successfully')

    def test_solve_auto_int_not_float(self):
        links_test = {"link1": [118, -80, 80],
                      "link2": [150, 5, 175],
                      "link3": [150, - 115, 55],
                      "link4": [54, -85, 85],
                      "link5": [0, 0, 0]}
        robot = fk_solver.FkSolver(links_test)
        result = robot.fk_solve_auto(0, 90.0, 0.0, 0.0)
        assert result == (0, [(0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0)], 'Thetas values must be float')

    def test_solve_auto_string_not_float(self):
        links_test = {"link1": [118, -80, 80],
                      "link2": [150, 5, 175],
                      "link3": [150, - 115, 55],
                      "link4": [54, -85, 85],
                      "link5": [0, 0, 0]}
        robot = fk_solver.FkSolver(links_test)
        result = robot.fk_solve_auto("a", 90.0, 0.0, 0.0)
        assert result == (0, [(0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0)], 'Thetas values must be float')

    def test_solve_user(self):
        table_dh = np.array([[0, 118, 0, math.radians(90)],
                             [math.radians(90), 0, 150, 0],
                             [0, 0, 150, 0],
                             [0, 0, 54, 0],
                             [math.radians(-90), 0, 0, 0]])
        result = (fk_solver.FkSolver.fk_solve_user(table_dh))
        assert result == (90, [(0.0, 0.0, 268.0), (0.0, 0.0, 418.0), (0.0, 0.0, 472.0), (0.0, 0.0, 472.0)],
                          'Forward kinematics calculations ended successfully')

    def test_solve_user_zero_division(self):
        table_dh = np.array([[0, 118, 0, math.radians(90)],
                             [math.radians(90), 0, 150, 0],
                             [0, 0, 150, 0],
                             [0, 0, 0, 0],
                             [math.radians(-90), 0, 0, 0]])
        result = (fk_solver.FkSolver.fk_solve_user(table_dh))
        assert result == (0, [(0, 0, 0)], 'ZeroDivisionError: Table_dh[-2][-2] must be != 0')