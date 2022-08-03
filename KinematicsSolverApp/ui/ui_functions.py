""" Module contains class UIFunctions that contains created functions to control application"""

import os
import datetime as dt

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

        self.ui.tableWidget.insertRow(self.ui.tableWidget.currentRow() + 1)

    def RemoveRow(self):
        """ Remove selected row """

        if self.ui.tableWidget.rowCount() > 0:
            self.ui.tableWidget.removeRow(self.ui.tableWidget.currentRow())

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
