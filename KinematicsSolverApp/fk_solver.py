import numpy as np
import math


class FkSolver:
    # TODO Create class discretion
    def __init__(self, link1, link2, link3, link4, link5):
        self.link1 = link1
        self.link2 = link2
        self.link3 = link3
        self.link4 = link4
        self.link5 = link5

    def dh(self, theta1, theta2, theta3, theta4):
        # TODO Create method discretion
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
    def hom_Matrix(table_dh, i):
        # TODO Create method discretion
        # Generation of homogenous transformation matrices Ti
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
    def solver(table_dh):
        # TODO Create method discretion
        matrix_t = FkSolver.hom_Matrix(table_dh, 0)
        xyz_pos1 = []

        # Determination of the homogenous transformation matrices
        for number in range(1, len(table_dh)):
            matrix_t = matrix_t @ FkSolver.hom_Matrix(table_dh, number)
            xyz_pos = float(round(matrix_t[0, 3])), float(round(matrix_t[1, 3])), float(round(matrix_t[2, 3]))
            xyz_pos1.append(xyz_pos)

        # End effector orientation
        try:
            z_ef = round(matrix_t[2, 3]) - round(xyz_pos1[-3][-1])
            alpha = math.degrees(math.asin(z_ef / round(table_dh[-2][-2])))
            status = "Forward kinematics calculations ended successfully"
            return round(alpha), xyz_pos1, status

        except RuntimeError as error:
            status = error
            return 0, [], status

        except:
            status = "Sth went wrong"
            return 0, [], status

    def solve_auto(self, theta1, theta2, theta3, theta4):
        # TODO Create method discretion
        table_dh = FkSolver.dh(self, theta1, theta2, theta3, theta4)
        return FkSolver.solver(table_dh)

    @staticmethod
    def solve_user(table_dh):
        # TODO Create method discretion
        return FkSolver.solver(table_dh)

# TODO Create error exceptions

# test
Robot = FkSolver(118, 150, 0, 54, 0)
print(Robot.solve_auto(0, 90, 0, 0))
table_dh3 = np.array([[0, 118, 0, math.radians(90)],
                      [math.radians(90), 0, 150, 0],
                      [0, 0, 150, 0],
                      [0, 0, 54, 0],
                      [math.radians(-90), 0, 0, 0]])
print((Robot.solve_user(table_dh3)))
