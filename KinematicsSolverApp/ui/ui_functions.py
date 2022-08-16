""" Module contains class UIFunctions that contains created functions to control application"""

import os
import datetime as dt
import numpy
import numpy as np

from KinematicsSolverApp.main import MainWindow
from KinematicsSolverApp.main import *

GLOBAL_STATE = 0


class UIFunctions(MainWindow):
    """ Class contains functions to control application GUI depending on users actions """

    # ==> TOGGLE MENU
    def __init__(self):
        super().__init__()
        self.sizegrip = None
        self.shadow = None
        self.animation = None

    def toggleMenu(self, max_width, enable):
        """Left toggle menu properties"""

        if enable:

            # GET WIDTH
            width = self.ui.frame_menu.width()
            max_extend = max_width
            standard = 70

            # SET MAX WIDTH
            if width == 70:
                width_extended = max_extend
            else:
                width_extended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.frame_menu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(width_extended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    # ==> SELECT
    def select_menu(getStyle):
        """
        Select menu page

        :return: menu_select
        """

        menu_select = getStyle + "QPushButton { border-right: 5px solid rgb(40, 112, 148); }"
        return menu_select

    # ==> DESELECT
    def deselect_menu(getStyle):
        """
        Deselect menu page

        :return: menu_deselect
        """

        menu_deselect = getStyle.replace("QPushButton { border-right: 5px solid rgb(40, 112, 148); }", "")
        return menu_deselect

    # ==> START/RESET SELECTION
    def select_standard_menu(self, widget):
        """Start/reset menu page selection"""

        for menu in self.ui.frame_menu.findChildren(QPushButton):
            if menu.objectName() != widget:
                menu.setStyleSheet(UIFunctions.deselect_menu(menu.styleSheet()))
            if menu.objectName() == widget:
                menu.setStyleSheet(UIFunctions.select_menu(menu.styleSheet()))

    # ==> CHANGE PAGE LABEL TEXT
    def label_page(self, text):
        """ Change page label text"""

        new_text = '| ' + text.upper()
        self.ui.label_top_info_2.setText(new_text)

    # ==> MAXIMIZE RESTORE FUNCTION
    def maximize_restore(self):
        """ Maximize and restore app window"""

        global GLOBAL_STATE
        status = GLOBAL_STATE

        # IF NOT MAXIMIZED
        if status == 0:
            self.showMaximized()

            # SET GLOBAL TO 1
            GLOBAL_STATE = 1

            # IF MAXIMIZED REMOVE MARGINS AND BORDER RADIUS
            self.ui.frame_top.setContentsMargins(0, 0, 0, 0)
            self.ui.btn_max.setToolTip("Restore")
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width() + 1, self.height() + 1)
            self.ui.frame_top.setContentsMargins(0, 0, 0, 0)
            self.ui.btn_max.setToolTip("Maximize")

    # ==> CLOSE APP
    @staticmethod
    def close_app():
        """Close app and end communication"""
        sys.exit()

    # ==> UI DEFINITIONS
    def uiDefinitions(self):
        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # SET DROP SHADOW WINDOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))

        # APPLY DROP SHADOW TO FRAME
        self.ui.frame_top.setGraphicsEffect(self.shadow)

        # MAXIMIZE / RESTORE
        self.ui.btn_max.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        # MINIMIZE
        self.ui.btn_min.clicked.connect(lambda: self.showMinimized())

        # CLOSE
        self.ui.btn_close.clicked.connect(lambda: UIFunctions.close_app())
        self.ui.btn_close.clicked.connect(lambda: self.close())

        # ==> RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.frame_grip)
        self.sizegrip.setStyleSheet("background: transparent;")

    # RETURN STATUS IF WINDOWS IS MAXIMIZE OR RESTORED
    @staticmethod
    def returnStatus():
        return GLOBAL_STATE

    # == > QTABLEWIDGET AUTO MODE
    # ADD / DELETE ROW
    def AddRow(self):
        """ Create empty row """

        self.ui.tableWidget_8.insertRow(self.ui.tableWidget.currentRow() + 1)

    def RemoveRow(self):
        """ Remove selected row """

        if self.ui.tableWidget_8.rowCount() > 0:
            self.ui.tableWidget_8.removeRow(self.ui.tableWidget.currentRow())

    # STATUS DISPLAY
    def log_list(self, log):
        """ Print given string in log"""

        log_time = dt.datetime.now().strftime("%H:%M:%S")
        new_text = log_time + " | " + log.upper()
        self.ui.Log.append(new_text)

        # write status to logs file
        if 'Error' in log:
            self.logger.error(log)
        elif 'Warning' in log:
            self.logger.warning(log)
        else:
            self.logger.info(log)

    def robotic_init_from_qtable_to_dict(self, qtable):

        l1 = qtable.item(0, 0).text()
        l2 = qtable.item(1, 0).text()
        l3 = qtable.item(2, 0).text()
        l4 = qtable.item(3, 0).text()
        l5 = qtable.item(4, 0).text()

        r1_min = qtable.item(0, 1).text()
        r2_min = qtable.item(1, 1).text()
        r3_min = qtable.item(2, 1).text()
        r4_min = qtable.item(3, 1).text()
        r5_min = qtable.item(4, 1).text()

        r1_max = qtable.item(0, 2).text()
        r2_max = qtable.item(1, 2).text()
        r3_max = qtable.item(2, 2).text()
        r4_max = qtable.item(3, 2).text()
        r5_max = qtable.item(4, 2).text()

        init_dict = {"link1": [l1, r1_min, r1_max],
                     "link2": [l2, r2_min, r2_max],
                     "link3": [l3, r3_min, r3_max],
                     "link4": [l4, r4_min, r4_max],
                     "link5": [l5, r5_min, r5_max]}

        return init_dict

    def read_user_dh(self):
        qtable = self.ui.tableWidget_8

        user_dh = np.array([[qtable.item(0, 0).text(), qtable.item(0, 1).text(), qtable.item(0, 2).text(), qtable.item(0, 3).text()],
                           [qtable.item(1, 0).text(), qtable.item(1, 1).text(), qtable.item(1, 2).text(), qtable.item(1, 3).text()],
                           [qtable.item(2, 0).text(), qtable.item(2, 1).text(), qtable.item(2, 2).text(), qtable.item(2, 3).text()],
                           [qtable.item(3, 0).text(), qtable.item(3, 1).text(), qtable.item(3, 2).text(), qtable.item(3, 3).text()],
                           [qtable.item(4, 0).text(), qtable.item(4, 1).text(), qtable.item(4, 2).text(), qtable.item(4, 3).text()]])
        return user_dh

    def robotic_input_fk(self):

        qtable = self.ui.tableWidget_fk_theta

        theta1 = qtable.item(0, 0).text()
        theta2 = qtable.item(0, 1).text()
        theta3 = qtable.item(0, 2).text()
        theta4 = qtable.item(0, 3).text()

        return theta1, theta2, theta3, theta4

    def robotic_input_ik(self):

        qtable = self.ui.tableWidget_ik_xyz

        px = qtable.item(0, 0).text()
        py = qtable.item(0, 1).text()
        pz = qtable.item(0, 2).text()
        # alfa = float(qtable.item(0, 3).text())
        alfa = 90
        return px, py, pz, alfa

    def write_to_dh_table(self):
        thetas = UIFunctions.robotic_input_fk(self)
        try:
            thetas = tuple(float(item) for item in thetas)
        except ValueError:
            status = "Error: Values must be float"
            UIFunctions.log_list(self, status)
        else:
            fk_dh = self.robotic_arm_fk.fk_dh(thetas[0], thetas[1], thetas[2], thetas[3])
            # Display status log
            UIFunctions.log_list(self, fk_dh[1])
            table_ui = self.ui.tableWidget_fk_dh

            # Add items to table
            row = 0
            for j in range(0, 5):
                values = [fk_dh[0][j][0],
                          fk_dh[0][j][1],
                          fk_dh[0][j][2],
                          fk_dh[0][j][3]]

                for i in range(0, table_ui.columnCount()):
                    table_ui.setItem(row, i, QTableWidgetItem(str(values[i])))
                row += 1

    def write_matrix_to_table(self, qtable, Ti):
        thetas = UIFunctions.robotic_input_fk(self)
        fk_dh = self.robotic_arm_fk.fk_dh(float(thetas[0]), float(thetas[1]), float(thetas[2]), float(thetas[3]))
        table_ui = qtable

        matrix = self.robotic_arm_fk.fk_hom_matrix(fk_dh[0], 0)

        # Determination of the homogenous transformation matrices
        for number in range(1, Ti):
            matrix = matrix @ self.robotic_arm_fk.fk_hom_matrix(fk_dh[0], number)

        # Add items to table
        row = 0
        for j in range(0, 4):
            values = [round(matrix[j][0],2),
                      round(matrix[j][1],2),
                      round(matrix[j][2],2),
                      round(matrix[j][3],2)]

            for i in range(0, table_ui.columnCount()):
                table_ui.setItem(row, i, QTableWidgetItem(str(values[i])))
            row += 1

    def display_ik_results(self, config_1, config_2):
        self.ui.lcdNumber_ik_theta1.display(config_1[0][0])
        self.ui.lcdNumber_ik_theta2.display(config_1[0][1])
        self.ui.lcdNumber_ik_theta3.display(config_1[0][2])
        self.ui.lcdNumber_ik_theta4.display(config_1[0][3])

        self.ui.lcdNumber_ik_theta1_2.display(config_2[0][0])
        self.ui.lcdNumber_ik_theta2_2.display(config_2[0][1])
        self.ui.lcdNumber_ik_theta3_2.display(config_2[0][2])
        self.ui.lcdNumber_ik_theta4_2.display(config_2[0][3])
