""" Module contains class AppFunctions that contains created functions to control application"""
from KinematicsSolverApp.main import *
from KinematicsSolverApp.main import MainWindow
from KinematicsSolverApp.ui.ui_functions import *

from KinematicsSolverApp.modules.robotic_arm import RoboticArm


class AppFunctions(MainWindow):
    """ Class contains functions to control application depending on users actions """

    def __init__(self):
        super().__init__()
        self.robotic_arm_ik = None
        self.robotic_arm_fk = None

    def page_fk_init(self):
        """
        Page - Forward kinematics calculations of robotic arm.\n
        Initialize robotics arm model with given parameters. \n

        :return: robotic_arm_fk
        """

        robotic_parm = UIFunctions.robotic_init_from_qtable_to_dict(self, self.ui.tableWidget_fk_input)

        for key in robotic_parm:
            for value in range(0, 3):
                try:
                    robotic_parm[key][value] = int(robotic_parm[key][value])
                except ValueError:
                    status = "Error: Values must be int"
                    UIFunctions.log_list(self, status)

        self.robotic_arm_fk = RoboticArm(robotic_parm)
        UIFunctions.log_list(self, self.robotic_arm_fk.fk_check_input_param())
        UIFunctions.write_to_dh_table(self)

    def page_fk_solve(self):
        """
        Page - Forward kinematics calculations of robotic arm.\n
        Calculate xyz position of end effector of robotic arm. \n

        :return: [Px, Py, Pz]
        """
        # Clear before calculations
        UIFunctions.clear_matrix_to_table(self, self.ui.tableWidget_fk_T12, 2)
        UIFunctions.clear_matrix_to_table(self, self.ui.tableWidget_fk_T13, 3)
        UIFunctions.clear_matrix_to_table(self, self.ui.tableWidget_fk_T14, 4)
        UIFunctions.clear_matrix_to_table(self, self.ui.tableWidget_fk_T15, 5)

        # Read input parameters
        thetas = UIFunctions.robotic_input_fk(self)

        try:
            thetas = tuple(float(item) for item in thetas)
        except ValueError:
            status = "Error: Values must be float"
            UIFunctions.log_list(self, status)
        else:
            self.robotic_arm_fk.fk_solve_auto(thetas[0], thetas[1], thetas[2], thetas[3])
            result = self.robotic_arm_fk.fk_solve_auto(thetas[0], thetas[1], thetas[2], thetas[3])

            UIFunctions.write_matrix_to_table(self, self.ui.tableWidget_fk_T12, 2)
            UIFunctions.write_matrix_to_table(self, self.ui.tableWidget_fk_T13, 3)
            UIFunctions.write_matrix_to_table(self, self.ui.tableWidget_fk_T14, 4)
            UIFunctions.write_matrix_to_table(self, self.ui.tableWidget_fk_T15, 5)

            # Display status log
            UIFunctions.log_list(self, result[2])

    def page_fk_solve_user(self):
        """
        Page - Forward kinematics calculations of robotic arm.\n
        Calculate xyz position of end effector of robotic arm with dh table inserted by user. \n

        :return: Forward kinematics
        """
        try:
            user_dh = UIFunctions.read_user_dh(self).astype(float)
        except ValueError:
            status = "Error: Values must be float"
            UIFunctions.log_list(self, status)
        else:
            fk_user_result = RoboticArm.fk_solve_user(user_dh)

            # Display status log
            UIFunctions.log_list(self, fk_user_result[2])

            user_px = fk_user_result[1][3][0]
            user_py = fk_user_result[1][3][1]
            user_pz = fk_user_result[1][3][2]

            # Display on LCD
            self.ui.lcdNumber_fk_px.display(user_px)
            self.ui.lcdNumber_fk_py.display(user_py)
            self.ui.lcdNumber_fk_pz.display(user_pz)

    def page_ik_init(self):
        """
        Page - Inverse kinematics calculations of robotic arm\n
        Initialize robotics arm model with given parameters. \n
        :return: Inverse kinematics
        """
        robotic_parm = UIFunctions.robotic_init_from_qtable_to_dict(self, self.ui.tableWidget_ik_input)
        for key in robotic_parm:
            for value in range(0, 3):
                try:
                    robotic_parm[key][value] = int(robotic_parm[key][value])
                except ValueError:
                    status = "Error: Values must be int"
                    UIFunctions.log_list(self, status)

        self.robotic_arm_ik = RoboticArm(robotic_parm)
        UIFunctions.log_list(self, self.robotic_arm_ik.fk_check_input_param())

    def page_ik_solve(self):
        """
        Page - Inverse kinematics calculations of robotic arm\n
        Calculate joints values of robotic arm with given xyz position. \n
        :return: [theta1, theta2, theta3, theta4]
        """
        # Clear lcd
        UIFunctions.display_ik_results(self, [[0.0, 0.0, 0.0, 0.0], "clear"], [[0.0, 0.0, 0.0, 0.0], "clear"])

        xyz = UIFunctions.robotic_input_ik(self)
        try:
            xyz = tuple(int(item) for item in xyz)
        except ValueError:
            status = "Error: Values must be int"
            UIFunctions.log_list(self, status)
        else:
            self.robotic_arm_ik.ik_solver(xyz[0], xyz[1], xyz[2], xyz[3])
            config_1 = self.robotic_arm_ik.ik_get_config1()
            config_2 = self.robotic_arm_ik.ik_get_config2()

            # Display results
            UIFunctions.display_ik_results(self, config_1, config_2)

            # Display status log
            UIFunctions.log_list(self, config_1[1])
            UIFunctions.log_list(self, config_2[1])
