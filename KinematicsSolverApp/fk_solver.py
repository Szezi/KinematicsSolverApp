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
        try:
            if not isinstance(link1, int) or not isinstance(link2, int) or not isinstance(link3, int) or not isinstance(
                    link4, int) or not isinstance(link5, int):
                status = "Links dimensions must be integers"
                print(status)
                self.link1 = None
                self.link2 = None
                self.link3 = None
                self.link4 = None
                self.link5 = None
            else:
                if link1 < 0 or link2 < 0 or link3 < 0 or link4 < 0 or link5 < 0:
                    status = "Links dimensions must be equal or greater then 0"
                    print(status)
                    self.link1 = None
                    self.link2 = None
                    self.link3 = None
                    self.link4 = None
                    self.link5 = None
                else:
                    status = "Links dimensions ok"
                    print(status)
                    self.link1 = link1
                    self.link2 = link2
                    self.link3 = link3
                    self.link4 = link4
                    self.link5 = link5
        except TypeError as error:
            print(str(error))

    def dh(self, theta1: float, theta2: float, theta3: float, theta4: float) -> Tuple[np.array, str]:
        """
        Method creates dh table with the given parameters.\n
        :param theta1: Base rotation angle
        :param theta2: 1st link rotation angle
        :param theta3: 2nd link rotation angle
        :param theta4: 3rd link rotation angle
        :return: dh_table, status
        """
        try:
            if not isinstance(theta1, float) or not isinstance(theta2, float) or not isinstance(theta3,
                                                                                                float) or not isinstance(
                    theta4, float):
                raise TypeError("Thetas values must be float")
            else:
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
                if None in table_dh:
                    raise TypeError("Robot configurations not defined correctly")
                else:
                    status = "DH table generated correctly"
                    return table_dh, status

        except TypeError as status:
            return_error = np.array([[0, 0, 0, 0],
                                     [0, 0, 0, 0],
                                     [0, 0, 0, 0],
                                     [0, 0, 0, 0],
                                     [0, 0, 0, 0]])
            return return_error, str(status)

    @staticmethod
    def hom_matrix(dh_table: np.array, i: int) -> np.array:
        """
        Generation of homogenous transformation matrices Ti. \n
        :param dh_table: Denavit–Hartenbergs table
        :param i: Number of transformations
        :return: t_dh - Homogenous trans. matrix Ti
        """

        t_dh = np.array([
            [math.cos(dh_table[i, 0]), (-1 * math.sin(dh_table[i, 0]) * math.cos(dh_table[i, 3])),
             (math.sin(dh_table[i, 0]) * math.sin(dh_table[i, 3])),
             dh_table[i, 2] * math.cos(dh_table[i, 0])],
            [math.sin(dh_table[i, 0]), (math.cos(dh_table[i, 0]) * math.cos(dh_table[i, 3])),
             (-1 * math.cos(dh_table[i, 0]) * math.sin(dh_table[i, 3])),
             dh_table[i, 2] * math.sin(dh_table[i, 0])],
            [0, math.sin(dh_table[i, 3]), math.cos(dh_table[i, 3]), dh_table[i, 1]],
            [0, 0, 0, 1]])
        return t_dh

    @staticmethod
    def solver(dh_table) -> Tuple[int, List[Tuple[float, float, float]], str]:
        """
        Forward kinematics end effector xyz pos. solver. \n
        :param dh_table: Denavit–Hartenbergs table
        :return: alpha; xyz_pos_link; status: Orientation and list of xyz positions of each link end
        """

        matrix_t = FkSolver.hom_matrix(dh_table, 0)
        xyz_pos1 = []

        # Determination of the homogenous transformation matrices
        for number in range(1, len(dh_table)):
            matrix_t = matrix_t @ FkSolver.hom_matrix(dh_table, number)
            xyz_pos = float(round(matrix_t[0, 3])), float(round(matrix_t[1, 3])), float(round(matrix_t[2, 3]))
            xyz_pos1.append(xyz_pos)
        # End effector orientation
        try:
            if round(round(dh_table[-2][-2])) == 0:
                raise ZeroDivisionError
            else:
                # z-ef - "z" dimension between last links "z" dim and end effector "z" dim.
                z_ef = round(matrix_t[2, 3]) - round(xyz_pos1[-3][-1])
                # alpha - z_ef / links4_length
                alpha = math.degrees(math.asin(z_ef / round(dh_table[-2][-2])))
                status = "Forward kinematics calculations ended successfully"
                return round(alpha), xyz_pos1, status

        except RuntimeError as error:
            status = str(error)
            return 0, [(0, 0, 0)], status
        except ZeroDivisionError:
            status = "ZeroDivisionError: Table_dh[-2][-2] must be != 0"
            return 0, [(0, 0, 0)], status
        except:
            status = "Sth went wrong"
            return 0, [(0, 0, 0)], status

    def solve_auto(self, theta1: float, theta2: float, theta3: float, theta4: float) -> Tuple[
                    int, List[Tuple[float, float, float]], str]:
        """
        Calculate end effectors xyz pos. with given rotations of initialized robotic model.\n
        :param theta1: Base rotation angle
        :param theta2: 1st link rotation angle
        :param theta3: 2nd link rotation angle
        :param theta4: 3rd link rotation angle
        :return: alpha; xyz_pos_link; status: Orientation and list of xyz positions of each link end
        """
        try:
            if not isinstance(theta1, float) or not isinstance(theta2, float) or not isinstance(theta3,
                                                                                                float) or not isinstance(
                    theta4, float):
                raise TypeError("Thetas values must be float")
            else:
                table_dh = FkSolver.dh(self, theta1, theta2, theta3, theta4)
                return FkSolver.solver(table_dh[0])

        except TypeError as error:
            status = str(error)
            return_error = (0, [(0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0)],
                            status)
            return return_error

    @staticmethod
    def solve_user(dh_table) -> Tuple[int, List[Tuple[float, float, float]], str]:
        """
        Calculate end effectors xyz pos. with given dh table.\n
        :param dh_table: Denavit–Hartenbergs table
        :return: alpha; xyz_pos_link; status: Orientation and list of xyz positions of each link end
        """
        return FkSolver.solver(dh_table)
