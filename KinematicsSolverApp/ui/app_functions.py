""" Module contains class AppFunctions that contains created functions to control application"""
from KinematicsSolverApp.main import *
from KinematicsSolverApp.main import MainWindow
from KinematicsSolverApp.ui.ui_functions import *


class AppFunctions(MainWindow):
    """ Class contains functions to control application depending on users actions """

    def __init__(self):
        super().__init__()

    def page_fk_init(self):
        """
        Page - Forward kinematics calculations of robotic arm.\n
        Initialize robotics arm model with given parameters. \n

        :return: robotic_arm_fk
        """
        pass

    def page_fk_solve(self):
        """
        Page - Forward kinematics calculations of robotic arm.\n
        Calculate xyz position of end effector of robotic arm. \n

        :return: [Px, Py, Pz]
        """
        pass

    def page_fk_solve_user(self):
        """
        Page - Forward kinematics calculations of robotic arm.\n
        Calculate xyz position of end effector of robotic arm with dh table inserted by user. \n

        :return: Forward kinematics
        """
        pass

    def page_ik_init(self):
        """
        Page - Inverse kinematics calculations of robotic arm\n
        Initialize robotics arm model with given parameters. \n
        :return: Inverse kinematics
        """
        pass

    def page_ik_solve(self):
        """
        Page - Inverse kinematics calculations of robotic arm\n
        Calculate joints values of robotic arm with given xyz position. \n
        :return: [theta1, theta2, theta3, theta4]
        """
        pass
