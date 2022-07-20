""" Module allows forward kinematics to be calculated"""
from typing import Tuple, List

import numpy as np
import math


class FkSolver:
    """ Class allows to calculate forward kinematics of the robotic arm with given parameters and specified length of robotic arm links.
    Forward kinematics is being calculated using Denavit–Hartenberg notation.\n """

    def __init__(self, link1: int, link2: int, link3: int, link4: int, link5: int) -> None:
        """
        Initials parameters and dimensions of robotic arm. \n
        :param link1: base height
        :param link2: 1st links length
        :param link3: 2nd links length
        :param link4: "L" effector dimension
        :param link5: "H" effector dimension
        """

        self.link1 = link1
        self.link2 = link2
        self.link3 = link3
        self.link4 = link4
        self.link5 = link5

    def dh(self, theta1: float, theta2: float, theta3: float, theta4: float) -> np.array:
        """
        Method creates dh table with the given parameters.\n
        :param theta1: Base rotation angle
        :param theta2: 1st link rotation angle
        :param theta3: 2nd link rotation angle
        :param theta4: 3rd link rotation angle
        :return: dh_table
        """

        # Convert angels in degrees to radians
        theta1 = math.radians(theta1)
        theta2 = math.radians(theta2)
        theta3 = math.radians(theta3)
        theta4 = math.radians(theta4)

        # DH table with input parameters
        table_dh = np.array([[theta1, self.link1, 0, math.radians(90)],
                             [theta2, 0, self.link2, 0],
                             [theta3, 0, self.link3, 0],
                             [theta4, 0, self.link4, 0],
                             [math.radians(-90), 0, self.link5, 0]])
        return table_dh

    @staticmethod
    def hom_Matrix(table_dh, i: int) -> np.array:
        """
        Generation of homogenous transformation matrices Ti. \n
        :param table_dh: Denavit–Hartenbergs table
        :param i: Number of transformations
        :return: t_dh - Homogenous trans. matrix Ti
        """

        t_dh = np.array([
            [math.cos(table_dh[i, 0]), (-1 * math.sin(table_dh[i, 0]) * math.cos(table_dh[i, 3])),
             (math.sin(table_dh[i, 0]) * math.sin(table_dh[i, 3])),
             table_dh[i, 2] * math.cos(table_dh[i, 0])],
            [math.sin(table_dh[i, 0]), (math.cos(table_dh[i, 0]) * math.cos(table_dh[i, 3])),
             (-1 * math.cos(table_dh[i, 0]) * math.sin(table_dh[i, 3])),
             table_dh[i, 2] * math.sin(table_dh[i, 0])],
            [0, math.sin(table_dh[i, 3]), math.cos(table_dh[i, 3]), table_dh[i, 1]],
            [0, 0, 0, 1]])
        return t_dh

    @staticmethod
    def solver(table_dh) -> Tuple[int, List[Tuple[float, float, float]], str]:
        """
        Forward kinematics end effector xyz pos. solver. \n
        :param table_dh: Denavit–Hartenbergs table
        :return: alpha; xyz_pos_link; status: Orientation and list of xyz positions of each link end
        """
        matrix_t = FkSolver.hom_Matrix(table_dh, 0)
        xyz_pos1 = []

        # Determination of the homogenous transformation matrices
        for number in range(1, len(table_dh)):
            matrix_t = matrix_t @ FkSolver.hom_Matrix(table_dh, number)
            xyz_pos = float(round(matrix_t[0, 3])), float(round(matrix_t[1, 3])), float(round(matrix_t[2, 3]))
            xyz_pos1.append(xyz_pos)

        # End effector orientation
        try:
            if round(xyz_pos1[-3][-1]) == 0:
                raise ZeroDivisionError
            else:
                # z-ef - "z" dimension between last links "z" dim and end effector "z" dim.
                z_ef = round(matrix_t[2, 3]) - round(xyz_pos1[-3][-1])
                # alpha - z_ef / links4_length
                alpha = math.degrees(math.asin(z_ef / round(table_dh[-2][-2])))
                status = "Forward kinematics calculations ended successfully"
                return round(alpha), xyz_pos1, status

        except RuntimeError as error:
            status = str(error)
            return 0, [(0, 0, 0)], status
        except ZeroDivisionError as error:
            status = str(error)
            return 0, [(0, 0, 0)], status
        except:
            status = "Sth went wrong"
            return 0, [(0, 0, 0)], status

    def solve_auto(self, theta1: float, theta2: float, theta3: float, theta4: float) -> Tuple[int, List[Tuple[float, float, float]], str]:
        """
        Calculate end effectors xyz pos. with given rotations of initialized robotic model.\n
        :param theta1: Base rotation angle
        :param theta2: 1st link rotation angle
        :param theta3: 2nd link rotation angle
        :param theta4: 3rd link rotation angle
        :return: alpha; xyz_pos_link; status: Orientation and list of xyz positions of each link end
        """
        table_dh = FkSolver.dh(self, theta1, theta2, theta3, theta4)
        return FkSolver.solver(table_dh)

    @staticmethod
    def solve_user(table_dh) -> Tuple[int, List[Tuple[float, float, float]], str]:
        """
        Calculate end effectors xyz pos. with given dh table.\n
        :param table_dh: Denavit–Hartenbergs table
        :return: alpha; xyz_pos_link; status: Orientation and list of xyz positions of each link end
        """
        return FkSolver.solver(table_dh)


# test
Robot = FkSolver(118, 150, 0, 54, 0)
print(Robot.solve_auto(0, 90, 0, 0))
table_dh3 = np.array([[0, 118, 0, math.radians(90)],
                      [math.radians(90), 0, 150, 0],
                      [0, 0, 150, 0],
                      [0, 0, 54, 0],
                      [math.radians(-90), 0, 0, 0]])
print((Robot.solve_user(table_dh3)))
