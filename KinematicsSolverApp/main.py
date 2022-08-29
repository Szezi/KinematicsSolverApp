import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from app_modules import *


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        self.dragPos = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Logging to file

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

        self.stdout_handler = logging.StreamHandler(sys.stdout)
        self.stdout_handler.setLevel(logging.DEBUG)
        self.stdout_handler.setFormatter(self.formatter)

        self.file_handler = logging.FileHandler(r'..\data\logs.log', mode='w')
        self.file_handler.setLevel(logging.DEBUG)
        self.file_handler.setFormatter(self.formatter)

        self.logger.addHandler(self.file_handler)
        self.logger.addHandler(self.stdout_handler)

        self.logger.info('Start app')

        # ==> START PAGE
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
        UIFunctions.select_standard_menu(self, "btn_home")

        # MENU
        ################################################################################################################
        self.ui.btn_lista.clicked.connect(lambda: UIFunctions.toggleMenu(self, 230, True))

        # MENU 1 HOME
        self.ui.btn_home.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_home))
        self.ui.btn_home.clicked.connect(lambda: UIFunctions.label_page(self, "HOME"))
        self.ui.btn_home.clicked.connect(lambda: UIFunctions.select_standard_menu(self, "btn_home"))
        self.ui.btn_home.clicked.connect(lambda: UIFunctions.log_list(self, 'Page changed to HOME'))

        # MENU 2 FK
        self.ui.btn_fk.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_fk))
        self.ui.btn_fk.clicked.connect(lambda: UIFunctions.label_page(self, "FORWARD KINEMATICS"))
        self.ui.btn_fk.clicked.connect(lambda: UIFunctions.select_standard_menu(self, "btn_fk"))
        self.ui.btn_fk.clicked.connect(lambda: UIFunctions.log_list(self, 'Page changed to FK'))

        # MENU 3 IK
        self.ui.btn_ik.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_ik))
        self.ui.btn_ik.clicked.connect(lambda: UIFunctions.label_page(self, "INVERSE KINEMATICS"))
        self.ui.btn_ik.clicked.connect(lambda: UIFunctions.select_standard_menu(self, "btn_ik"))
        self.ui.btn_ik.clicked.connect(lambda: UIFunctions.log_list(self, 'Page changed to IK'))

        # MENU 4 SETTINGS
        self.ui.btn_settings.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_settings))
        self.ui.btn_settings.clicked.connect(lambda: UIFunctions.label_page(self, "SETTINGS"))
        self.ui.btn_settings.clicked.connect(lambda: UIFunctions.select_standard_menu(self, "btn_settings"))
        self.ui.btn_settings.clicked.connect(lambda: UIFunctions.log_list(self, 'Page changed to settings'))

        # Pages
        ################################################################################################################

        # HOME
        self.ui.btn_home_FK.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_fk))
        self.ui.btn_home_FK.clicked.connect(lambda: UIFunctions.label_page(self, "FORWARD KINEMATICS"))
        self.ui.btn_home_FK.clicked.connect(lambda: UIFunctions.select_standard_menu(self, "btn_fk"))
        self.ui.btn_home_FK.clicked.connect(lambda: UIFunctions.log_list(self, 'Page changed to FK'))

        self.ui.btn_home_IK.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_ik))
        self.ui.btn_home_IK.clicked.connect(lambda: UIFunctions.label_page(self, "INVERSE KINEMATICS"))
        self.ui.btn_home_IK.clicked.connect(lambda: UIFunctions.select_standard_menu(self, "btn_ik"))
        self.ui.btn_home_IK.clicked.connect(lambda: UIFunctions.log_list(self, 'Page changed to IK'))

        self.ui.btn_home_settings.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_settings))
        self.ui.btn_home_settings.clicked.connect(lambda: UIFunctions.label_page(self, "SETTINGS"))
        self.ui.btn_home_settings.clicked.connect(lambda: UIFunctions.select_standard_menu(self, "btn_settings"))
        self.ui.btn_home_settings.clicked.connect(lambda: UIFunctions.log_list(self, 'Page changed to settings'))

        # FK
        # Tab init/solve auto
        self.ui.btn_fk_init.clicked.connect(lambda: AppFunctions.page_fk_init(self))
        self.ui.btn_fk_solve.clicked.connect(lambda: AppFunctions.page_fk_solve(self))
        # Tab USER mode
        self.ui.btn_fk_user_add.clicked.connect(lambda: UIFunctions.AddRow(self))
        self.ui.btn_fk_user_sub.clicked.connect(lambda: UIFunctions.RemoveRow(self))
        self.ui.btn_fk_user_solve.clicked.connect(lambda: AppFunctions.page_fk_solve_user(self))

        # IK
        self.ui.btn_ik_init.clicked.connect(lambda: AppFunctions.page_ik_init(self))
        self.ui.btn_ik_solve.clicked.connect(lambda: AppFunctions.page_ik_solve(self))

        ################################################################################################################

        # MOVE WINDOW
        def move_window(event):
            # RESTORE BEFORE MOVE
            if UIFunctions.returnStatus == 1:
                UIFunctions.maximize_restore(self)

            # IF LEFT CLICK MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # SET TITLE BAR
        self.ui.frame_top.mouseMoveEvent = move_window

        # ==> SET UI DEFINITIONS
        UIFunctions.uiDefinitions(self)

        # SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()

    # APP EVENTS
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()


GUI = MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GUI()
    sys.exit(app.exec_())
