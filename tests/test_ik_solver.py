import pytest
import coverage
import sys

from KinematicsSolverApp import ik_solver


class TestIkSolver:

    def test_adding_two_numbers(self):
        the_sum = 2 + 2
        assert the_sum == 4

    def test_check_input_param_ok(self, capsys):
        links_test = {"link1": [118, -80, 80],
                      "link2": [150, 5, 175],
                      "link3": [150, - 115, 55],
                      "link4": [54, -85, 85],
                      "link5": [0, 0, 0]}
        ik_solver.IkSolver(links_test)
        out, err = capsys.readouterr()
        assert out == "Links dimensions ok\n"

    def test_check_input_param_str(self, capsys):
        links_test = {"link1": ["a", -80, 80],
                      "link2": [150, 5, 175],
                      "link3": [150, - 115, 55],
                      "link4": [54, -85, 85],
                      "link5": [0, 0, 0]}
        ik_solver.IkSolver(links_test)
        out, err = capsys.readouterr()
        assert out == "Links dimensions must be integers\n"

    def test_check_input_param_min_length(self, capsys):
        links_test = {"link1": [-100, -80, 80],
                      "link2": [150, 5, 175],
                      "link3": [150, - 115, 55],
                      "link4": [54, -85, 85],
                      "link5": [0, 0, 0]}
        ik_solver.IkSolver(links_test)
        out, err = capsys.readouterr()
        assert out == "Links dimensions must be equal or greater then 0\n"

    def test_solver_ok(self):
        links_test = {"link1": [118, -80, 80],
                      "link2": [150, 5, 175],
                      "link3": [150, - 115, 55],
                      "link4": [54, -85, 85],
                      "link5": [0, 0, 0]}
        robot = ik_solver.IkSolver(links_test)
        result = robot.ik_solver(0, 0, 472, 90)
        assert result == 'Calculations ended successfully'

    def test_solver_str(self):
        links_test = {"link1": [118, -80, 80],
                      "link2": [150, 5, 175],
                      "link3": [150, - 115, 55],
                      "link4": [54, -85, 85],
                      "link5": [0, 0, 0]}
        robot = ik_solver.IkSolver(links_test)
        result = robot.ik_solver("a", 0, 472, 90)
        assert result == "Error: The entered data is incorrect"

    def test_solver_minus(self):
        links_test = {"link1": [118, -80, 80],
                      "link2": [150, 5, 175],
                      "link3": [150, - 115, 55],
                      "link4": [54, -85, 85],
                      "link5": [0, 0, 0]}
        robot = ik_solver.IkSolver(links_test)
        result = robot.ik_solver(-100, 0, 472, 90)
        assert result == "Error: Something went wrong"
