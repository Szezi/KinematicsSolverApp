# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_KinematicsSolverApp.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from KinematicsSolverApp.ui.icons import icons_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 680)
        MainWindow.setMinimumSize(QSize(1000, 680))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u" QToolTip {\n"
"     padding: 5px;\n"
"     border-radius: 3px;\n"
" }")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.centralwidget)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMaximumSize(QSize(16777215, 60))
        self.frame_top.setStyleSheet(u"background-color: rgb(212, 212, 206);")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_top)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top_lista = QFrame(self.frame_top)
        self.frame_top_lista.setObjectName(u"frame_top_lista")
        self.frame_top_lista.setMinimumSize(QSize(0, 0))
        self.frame_top_lista.setMaximumSize(QSize(70, 60))
        self.frame_top_lista.setStyleSheet(u"")
        self.frame_top_lista.setFrameShape(QFrame.NoFrame)
        self.frame_top_lista.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_top_lista)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_lista = QPushButton(self.frame_top_lista)
        self.btn_lista.setObjectName(u"btn_lista")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_lista.sizePolicy().hasHeightForWidth())
        self.btn_lista.setSizePolicy(sizePolicy)
        self.btn_lista.setMinimumSize(QSize(0, 0))
        self.btn_lista.setStyleSheet(u"QPushButton {\n"
"	\n"
"	background-image: url(:/24x24/24x24/icons8-activity-feed-50.png);\n"
"	background-position: left center;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	border-left: 25px solid rgb(2, 50, 70);\n"
"	background-color: rgb(2, 50, 70);\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(40, 112, 148);\n"
"	border-left: 25px solid rgb(40, 112, 148);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 25px solid rgb(85, 170, 255);\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.btn_lista)


        self.horizontalLayout.addWidget(self.frame_top_lista)

        self.frame_top_right = QFrame(self.frame_top)
        self.frame_top_right.setObjectName(u"frame_top_right")
        self.frame_top_right.setStyleSheet(u"background-color: rgb(40, 112, 148);")
        self.frame_top_right.setFrameShape(QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_top_right)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_top_right2 = QFrame(self.frame_top_right)
        self.frame_top_right2.setObjectName(u"frame_top_right2")
        self.frame_top_right2.setMinimumSize(QSize(0, 30))
        self.frame_top_right2.setMaximumSize(QSize(16777215, 30))
        self.frame_top_right2.setStyleSheet(u"background-color: rgb(2, 50, 70);")
        self.frame_top_right2.setFrameShape(QFrame.NoFrame)
        self.frame_top_right2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_right2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_name = QFrame(self.frame_top_right2)
        self.frame_name.setObjectName(u"frame_name")
        self.frame_name.setStyleSheet(u"")
        self.frame_name.setFrameShape(QFrame.NoFrame)
        self.frame_name.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_name)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 0, 10, 0)
        self.frame_name_logo = QFrame(self.frame_name)
        self.frame_name_logo.setObjectName(u"frame_name_logo")
        self.frame_name_logo.setMaximumSize(QSize(30, 30))
        self.frame_name_logo.setStyleSheet(u"background: transparent;\n"
"background-image: url(:/24x24/24x24/icons8-robot-50.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.frame_name_logo.setFrameShape(QFrame.NoFrame)
        self.frame_name_logo.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_name_logo)

        self.label_name = QLabel(self.frame_name)
        self.label_name.setObjectName(u"label_name")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_name.setFont(font)
        self.label_name.setStyleSheet(u"background: transparent;\n"
"color: rgb(222, 222, 222);\n"
"margin-left: 5px;")

        self.horizontalLayout_10.addWidget(self.label_name)


        self.horizontalLayout_4.addWidget(self.frame_name)

        self.frame_btn = QFrame(self.frame_top_right2)
        self.frame_btn.setObjectName(u"frame_btn")
        self.frame_btn.setMaximumSize(QSize(120, 16777215))
        self.frame_btn.setFrameShape(QFrame.NoFrame)
        self.frame_btn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btn)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_min = QPushButton(self.frame_btn)
        self.btn_min.setObjectName(u"btn_min")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_min.sizePolicy().hasHeightForWidth())
        self.btn_min.setSizePolicy(sizePolicy1)
        self.btn_min.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(40, 112, 148);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/20x20/20x20/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_min.setIcon(icon)
        self.btn_min.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.btn_min)

        self.btn_max = QPushButton(self.frame_btn)
        self.btn_max.setObjectName(u"btn_max")
        sizePolicy1.setHeightForWidth(self.btn_max.sizePolicy().hasHeightForWidth())
        self.btn_max.setSizePolicy(sizePolicy1)
        self.btn_max.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(40, 112, 148);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/20x20/20x20/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_max.setIcon(icon1)
        self.btn_max.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.btn_max)

        self.btn_close = QPushButton(self.frame_btn)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy1.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy1)
        self.btn_close.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(40, 112, 148);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/20x20/20x20/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon2)
        self.btn_close.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.btn_close)


        self.horizontalLayout_4.addWidget(self.frame_btn)


        self.verticalLayout_8.addWidget(self.frame_top_right2)

        self.frame_top_info = QFrame(self.frame_top_right)
        self.frame_top_info.setObjectName(u"frame_top_info")
        self.frame_top_info.setMinimumSize(QSize(0, 30))
        self.frame_top_info.setMaximumSize(QSize(16777215, 30))
        self.frame_top_info.setStyleSheet(u"")
        self.frame_top_info.setFrameShape(QFrame.NoFrame)
        self.frame_top_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_top_info)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.label_top_info_2 = QLabel(self.frame_top_info)
        self.label_top_info_2.setObjectName(u"label_top_info_2")
        self.label_top_info_2.setMinimumSize(QSize(0, 0))
        self.label_top_info_2.setMaximumSize(QSize(250, 16777215))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setBold(True)
        font1.setWeight(75)
        self.label_top_info_2.setFont(font1)
        self.label_top_info_2.setStyleSheet(u"color: rgb(222, 222, 222);")
        self.label_top_info_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_top_info_2)


        self.verticalLayout_8.addWidget(self.frame_top_info, 0, Qt.AlignRight)


        self.horizontalLayout.addWidget(self.frame_top_right)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_content = QFrame(self.centralwidget)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setStyleSheet(u"background-color: rgb(246, 246, 246);\n"
"")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_menu = QFrame(self.frame_content)
        self.frame_menu.setObjectName(u"frame_menu")
        self.frame_menu.setMinimumSize(QSize(70, 0))
        self.frame_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_menu.setStyleSheet(u"background-color: rgb(2, 50, 70);")
        self.frame_menu.setFrameShape(QFrame.NoFrame)
        self.frame_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_menu_top = QFrame(self.frame_menu)
        self.frame_menu_top.setObjectName(u"frame_menu_top")
        self.frame_menu_top.setFrameShape(QFrame.NoFrame)
        self.frame_menu_top.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_menu_top)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.frame_menu_top)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy2)
        self.btn_home.setMinimumSize(QSize(0, 60))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        self.btn_home.setFont(font2)
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"QPushButton {	\n"
"	background-image: url(:/24x24/24x24/icons8-four-squares-50.png);\n"
"	background-position:left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 25px solid rgb(2, 50, 70);\n"
"	background-color: rgb(2, 50, 70);\n"
"	text-align: left;\n"
"	padding-left: 45px;\n"
"	color: rgb(222, 222, 222);\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(40, 112, 148);\n"
"	border-left: 25px solid rgb(40, 112, 148);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 25px solid rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_home)

        self.btn_fk = QPushButton(self.frame_menu_top)
        self.btn_fk.setObjectName(u"btn_fk")
        sizePolicy2.setHeightForWidth(self.btn_fk.sizePolicy().hasHeightForWidth())
        self.btn_fk.setSizePolicy(sizePolicy2)
        self.btn_fk.setMinimumSize(QSize(0, 60))
        self.btn_fk.setFont(font2)
        self.btn_fk.setLayoutDirection(Qt.LeftToRight)
        self.btn_fk.setStyleSheet(u"QPushButton {	\n"
"	background-image: url(:/others/24x24/icons_fk.png);\n"
"	background-position:left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 25px solid rgb(2, 50, 70);\n"
"	background-color: rgb(2, 50, 70);\n"
"	text-align: left;\n"
"	padding-left: 45px;\n"
"	color: rgb(222, 222, 222);\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(40, 112, 148);\n"
"	border-left: 25px solid rgb(40, 112, 148);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 25px solid rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_fk)

        self.btn_ik = QPushButton(self.frame_menu_top)
        self.btn_ik.setObjectName(u"btn_ik")
        sizePolicy2.setHeightForWidth(self.btn_ik.sizePolicy().hasHeightForWidth())
        self.btn_ik.setSizePolicy(sizePolicy2)
        self.btn_ik.setMinimumSize(QSize(0, 60))
        self.btn_ik.setFont(font2)
        self.btn_ik.setLayoutDirection(Qt.LeftToRight)
        self.btn_ik.setStyleSheet(u"QPushButton {	\n"
"	background-image: url(:/others/24x24/icons_Ik.png);\n"
"	background-position:left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 25px solid rgb(2, 50, 70);\n"
"	background-color: rgb(2, 50, 70);\n"
"	text-align: left;\n"
"	padding-left: 45px;\n"
"	color: rgb(222, 222, 222);\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(40, 112, 148);\n"
"	border-left: 25px solid rgb(40, 112, 148);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 25px solid rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_ik)


        self.verticalLayout_3.addWidget(self.frame_menu_top, 0, Qt.AlignTop)

        self.frame_menu_bottom = QFrame(self.frame_menu)
        self.frame_menu_bottom.setObjectName(u"frame_menu_bottom")
        self.frame_menu_bottom.setMaximumSize(QSize(16777215, 100))
        self.frame_menu_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_menu_bottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_menu_bottom)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 50)
        self.btn_settings = QPushButton(self.frame_menu_bottom)
        self.btn_settings.setObjectName(u"btn_settings")
        sizePolicy2.setHeightForWidth(self.btn_settings.sizePolicy().hasHeightForWidth())
        self.btn_settings.setSizePolicy(sizePolicy2)
        self.btn_settings.setMinimumSize(QSize(0, 60))
        self.btn_settings.setFont(font2)
        self.btn_settings.setLayoutDirection(Qt.LeftToRight)
        self.btn_settings.setStyleSheet(u"QPushButton {	\n"
"	background-image: url(:/24x24/24x24/icons8-adjust-50.png);\n"
"	background-position:left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 25px solid rgb(2, 50, 70);\n"
"	background-color: rgb(2, 50, 70);\n"
"	text-align: left;\n"
"	padding-left: 45px;\n"
"	color: rgb(222, 222, 222);\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(40, 112, 148);\n"
"	border-left: 25px solid rgb(40, 112, 148);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"	border-left: 25px solid rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_5.addWidget(self.btn_settings)


        self.verticalLayout_3.addWidget(self.frame_menu_bottom)


        self.horizontalLayout_2.addWidget(self.frame_menu)

        self.frame_screens = QFrame(self.frame_content)
        self.frame_screens.setObjectName(u"frame_screens")
        self.frame_screens.setFrameShape(QFrame.NoFrame)
        self.frame_screens.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_screens)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_stackedWidget = QFrame(self.frame_screens)
        self.frame_stackedWidget.setObjectName(u"frame_stackedWidget")
        self.frame_stackedWidget.setFrameShape(QFrame.NoFrame)
        self.frame_stackedWidget.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_stackedWidget)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_stackedWidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.page_home.setLayoutDirection(Qt.LeftToRight)
        self.horizontalLayout_7 = QHBoxLayout(self.page_home)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_home_shortcuts = QFrame(self.page_home)
        self.frame_home_shortcuts.setObjectName(u"frame_home_shortcuts")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_home_shortcuts.sizePolicy().hasHeightForWidth())
        self.frame_home_shortcuts.setSizePolicy(sizePolicy3)
        self.frame_home_shortcuts.setMinimumSize(QSize(440, 0))
        self.frame_home_shortcuts.setFrameShape(QFrame.NoFrame)
        self.frame_home_shortcuts.setFrameShadow(QFrame.Raised)
        self.frame_home_shortcuts.setMidLineWidth(1)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_home_shortcuts)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_home_buttons = QFrame(self.frame_home_shortcuts)
        self.frame_home_buttons.setObjectName(u"frame_home_buttons")
        self.frame_home_buttons.setFrameShape(QFrame.StyledPanel)
        self.frame_home_buttons.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_home_buttons)
        self.verticalLayout_7.setSpacing(50)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(50, 50, 50, 50)
        self.btn_home_FK = QPushButton(self.frame_home_buttons)
        self.btn_home_FK.setObjectName(u"btn_home_FK")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btn_home_FK.sizePolicy().hasHeightForWidth())
        self.btn_home_FK.setSizePolicy(sizePolicy4)
        self.btn_home_FK.setMinimumSize(QSize(150, 150))
        self.btn_home_FK.setMaximumSize(QSize(200, 200))
        self.btn_home_FK.setSizeIncrement(QSize(10, 10))
        self.btn_home_FK.setBaseSize(QSize(100, 100))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(10)
        self.btn_home_FK.setFont(font3)
        self.btn_home_FK.setLayoutDirection(Qt.LeftToRight)
        self.btn_home_FK.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(222, 222, 222);\n"
"    border: 2px solid #555;\n"
"    border-radius: 25px;\n"
"    border-style: outset;\n"
"	background-color: rgb(2, 50, 70);\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(40, 112, 148);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_7.addWidget(self.btn_home_FK, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.btn_home_IK = QPushButton(self.frame_home_buttons)
        self.btn_home_IK.setObjectName(u"btn_home_IK")
        sizePolicy4.setHeightForWidth(self.btn_home_IK.sizePolicy().hasHeightForWidth())
        self.btn_home_IK.setSizePolicy(sizePolicy4)
        self.btn_home_IK.setMinimumSize(QSize(150, 150))
        self.btn_home_IK.setMaximumSize(QSize(200, 200))
        self.btn_home_IK.setFont(font3)
        self.btn_home_IK.setLayoutDirection(Qt.LeftToRight)
        self.btn_home_IK.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(222, 222, 222);\n"
"    border: 2px solid #555;\n"
"    border-radius: 25px;\n"
"    border-style: outset;\n"
"	background-color: rgb(2, 50, 70);\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(40, 112, 148);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_7.addWidget(self.btn_home_IK, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.btn_home_settings = QPushButton(self.frame_home_buttons)
        self.btn_home_settings.setObjectName(u"btn_home_settings")
        sizePolicy4.setHeightForWidth(self.btn_home_settings.sizePolicy().hasHeightForWidth())
        self.btn_home_settings.setSizePolicy(sizePolicy4)
        self.btn_home_settings.setMinimumSize(QSize(150, 150))
        self.btn_home_settings.setMaximumSize(QSize(200, 200))
        self.btn_home_settings.setFont(font3)
        self.btn_home_settings.setLayoutDirection(Qt.LeftToRight)
        self.btn_home_settings.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(222, 222, 222);\n"
"    border: 2px solid #555;\n"
"    border-radius: 25px;\n"
"    border-style: outset;\n"
"	background-color: rgb(2, 50, 70);\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(40, 112, 148);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_7.addWidget(self.btn_home_settings, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_11.addWidget(self.frame_home_buttons)

        self.frame_home_info = QFrame(self.frame_home_shortcuts)
        self.frame_home_info.setObjectName(u"frame_home_info")
        self.frame_home_info.setStyleSheet(u"")
        self.frame_home_info.setFrameShape(QFrame.StyledPanel)
        self.frame_home_info.setFrameShadow(QFrame.Raised)
        self.gridLayout_18 = QGridLayout(self.frame_home_info)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.label = QLabel(self.frame_home_info)
        self.label.setObjectName(u"label")
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setWeight(75)
        self.label.setFont(font4)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_18.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.frame_home_info)
        self.label_2.setObjectName(u"label_2")
        sizePolicy4.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy4)
        self.label_2.setMinimumSize(QSize(365, 270))
        self.label_2.setMaximumSize(QSize(365, 270))
        self.label_2.setPixmap(QPixmap(u":/others/others/scheme2.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setWordWrap(True)

        self.gridLayout_18.addWidget(self.label_2, 1, 0, 1, 1, Qt.AlignHCenter|Qt.AlignBottom)


        self.horizontalLayout_11.addWidget(self.frame_home_info)


        self.horizontalLayout_7.addWidget(self.frame_home_shortcuts)

        self.stackedWidget.addWidget(self.page_home)
        self.page_fk = QWidget()
        self.page_fk.setObjectName(u"page_fk")
        self.gridLayout_5 = QGridLayout(self.page_fk)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_fk = QTabWidget(self.page_fk)
        self.tabWidget_fk.setObjectName(u"tabWidget_fk")
        self.tabWidget_fk.setMinimumSize(QSize(0, 0))
        self.tab_fk_input_parameters = QWidget()
        self.tab_fk_input_parameters.setObjectName(u"tab_fk_input_parameters")
        self.gridLayout = QGridLayout(self.tab_fk_input_parameters)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_fk_input = QFrame(self.tab_fk_input_parameters)
        self.frame_fk_input.setObjectName(u"frame_fk_input")
        self.frame_fk_input.setMinimumSize(QSize(462, 285))
        self.frame_fk_input.setFrameShape(QFrame.StyledPanel)
        self.frame_fk_input.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_fk_input)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.btn_fk_init = QPushButton(self.frame_fk_input)
        self.btn_fk_init.setObjectName(u"btn_fk_init")
        sizePolicy4.setHeightForWidth(self.btn_fk_init.sizePolicy().hasHeightForWidth())
        self.btn_fk_init.setSizePolicy(sizePolicy4)
        self.btn_fk_init.setMinimumSize(QSize(50, 50))
        self.btn_fk_init.setMaximumSize(QSize(50, 50))
        self.btn_fk_init.setSizeIncrement(QSize(10, 10))
        self.btn_fk_init.setBaseSize(QSize(100, 100))
        self.btn_fk_init.setFont(font3)
        self.btn_fk_init.setLayoutDirection(Qt.LeftToRight)
        self.btn_fk_init.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(222, 222, 222);\n"
"    border: 2px solid #555;\n"
"    border-radius: 25px;\n"
"    border-style: outset;\n"
"	background-color: rgb(2, 50, 70);\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(40, 112, 148);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.gridLayout_3.addWidget(self.btn_fk_init, 1, 1, 1, 1)

        self.btn_fk_solve = QPushButton(self.frame_fk_input)
        self.btn_fk_solve.setObjectName(u"btn_fk_solve")
        sizePolicy4.setHeightForWidth(self.btn_fk_solve.sizePolicy().hasHeightForWidth())
        self.btn_fk_solve.setSizePolicy(sizePolicy4)
        self.btn_fk_solve.setMinimumSize(QSize(50, 50))
        self.btn_fk_solve.setMaximumSize(QSize(50, 50))
        self.btn_fk_solve.setSizeIncrement(QSize(10, 10))
        self.btn_fk_solve.setBaseSize(QSize(100, 100))
        self.btn_fk_solve.setFont(font3)
        self.btn_fk_solve.setLayoutDirection(Qt.LeftToRight)
        self.btn_fk_solve.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(222, 222, 222);\n"
"    border: 2px solid #555;\n"
"    border-radius: 25px;\n"
"    border-style: outset;\n"
"	background-color: rgb(2, 50, 70);\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(40, 112, 148);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.gridLayout_3.addWidget(self.btn_fk_solve, 3, 1, 1, 1)

        self.tableWidget_fk_theta = QTableWidget(self.frame_fk_input)
        if (self.tableWidget_fk_theta.columnCount() < 4):
            self.tableWidget_fk_theta.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_fk_theta.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_fk_theta.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_fk_theta.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_fk_theta.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget_fk_theta.rowCount() < 1):
            self.tableWidget_fk_theta.setRowCount(1)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_fk_theta.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_theta.setItem(0, 0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_theta.setItem(0, 1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_theta.setItem(0, 2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_theta.setItem(0, 3, __qtablewidgetitem8)
        self.tableWidget_fk_theta.setObjectName(u"tableWidget_fk_theta")
        sizePolicy3.setHeightForWidth(self.tableWidget_fk_theta.sizePolicy().hasHeightForWidth())
        self.tableWidget_fk_theta.setSizePolicy(sizePolicy3)
        self.tableWidget_fk_theta.setMinimumSize(QSize(386, 50))
        self.tableWidget_fk_theta.setMaximumSize(QSize(900, 16777215))
        self.tableWidget_fk_theta.setFrameShape(QFrame.NoFrame)
        self.tableWidget_fk_theta.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_fk_theta.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_fk_theta.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget_fk_theta.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_fk_theta.horizontalHeader().setDefaultSectionSize(90)
        self.tableWidget_fk_theta.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_fk_theta.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_fk_theta.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget_fk_theta.verticalHeader().setDefaultSectionSize(35)
        self.tableWidget_fk_theta.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_fk_theta.verticalHeader().setStretchLastSection(True)

        self.gridLayout_3.addWidget(self.tableWidget_fk_theta, 2, 0, 2, 1, Qt.AlignLeft)

        self.tableWidget_fk_unput = QTableWidget(self.frame_fk_input)
        if (self.tableWidget_fk_unput.columnCount() < 3):
            self.tableWidget_fk_unput.setColumnCount(3)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_fk_unput.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_fk_unput.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_fk_unput.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        if (self.tableWidget_fk_unput.rowCount() < 5):
            self.tableWidget_fk_unput.setRowCount(5)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_fk_unput.setVerticalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_fk_unput.setVerticalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_fk_unput.setVerticalHeaderItem(2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_fk_unput.setVerticalHeaderItem(3, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_fk_unput.setVerticalHeaderItem(4, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_unput.setItem(0, 0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_unput.setItem(0, 1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_unput.setItem(0, 2, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_unput.setItem(1, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_unput.setItem(1, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_unput.setItem(1, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_unput.setItem(2, 0, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_unput.setItem(2, 1, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_unput.setItem(2, 2, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_unput.setItem(3, 0, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_unput.setItem(3, 1, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_unput.setItem(3, 2, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_unput.setItem(4, 0, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_unput.setItem(4, 1, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_unput.setItem(4, 2, __qtablewidgetitem31)
        self.tableWidget_fk_unput.setObjectName(u"tableWidget_fk_unput")
        sizePolicy3.setHeightForWidth(self.tableWidget_fk_unput.sizePolicy().hasHeightForWidth())
        self.tableWidget_fk_unput.setSizePolicy(sizePolicy3)
        self.tableWidget_fk_unput.setMinimumSize(QSize(386, 196))
        self.tableWidget_fk_unput.setMaximumSize(QSize(900, 16777215))
        self.tableWidget_fk_unput.setFrameShape(QFrame.NoFrame)
        self.tableWidget_fk_unput.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_fk_unput.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_fk_unput.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget_fk_unput.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tableWidget_fk_unput.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_fk_unput.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget_fk_unput.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget_fk_unput.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_fk_unput.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_fk_unput.verticalHeader().setVisible(True)
        self.tableWidget_fk_unput.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_fk_unput.verticalHeader().setDefaultSectionSize(33)
        self.tableWidget_fk_unput.verticalHeader().setHighlightSections(False)
        self.tableWidget_fk_unput.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_fk_unput.verticalHeader().setStretchLastSection(True)

        self.gridLayout_3.addWidget(self.tableWidget_fk_unput, 0, 0, 2, 1, Qt.AlignLeft)


        self.gridLayout.addWidget(self.frame_fk_input, 0, 0, 1, 2)

        self.frame_fk_info = QFrame(self.tab_fk_input_parameters)
        self.frame_fk_info.setObjectName(u"frame_fk_info")
        self.frame_fk_info.setMinimumSize(QSize(462, 285))
        self.frame_fk_info.setFrameShape(QFrame.StyledPanel)
        self.frame_fk_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_fk_info)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.textBrowser_fk = QTextBrowser(self.frame_fk_info)
        self.textBrowser_fk.setObjectName(u"textBrowser_fk")
        sizePolicy4.setHeightForWidth(self.textBrowser_fk.sizePolicy().hasHeightForWidth())
        self.textBrowser_fk.setSizePolicy(sizePolicy4)
        self.textBrowser_fk.setMinimumSize(QSize(440, 250))
        self.textBrowser_fk.setFrameShape(QFrame.NoFrame)
        self.textBrowser_fk.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textBrowser_fk.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_14.addWidget(self.textBrowser_fk)


        self.gridLayout.addWidget(self.frame_fk_info, 0, 2, 2, 1)

        self.frame_fk_scheme = QFrame(self.tab_fk_input_parameters)
        self.frame_fk_scheme.setObjectName(u"frame_fk_scheme")
        self.frame_fk_scheme.setMinimumSize(QSize(462, 285))
        self.frame_fk_scheme.setFrameShape(QFrame.StyledPanel)
        self.frame_fk_scheme.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_fk_scheme)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_fk_scheme = QLabel(self.frame_fk_scheme)
        self.label_fk_scheme.setObjectName(u"label_fk_scheme")
        self.label_fk_scheme.setMinimumSize(QSize(440, 250))
        self.label_fk_scheme.setPixmap(QPixmap(u":/others/others/scheme2.png"))
        self.label_fk_scheme.setScaledContents(True)
        self.label_fk_scheme.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_fk_scheme)


        self.gridLayout.addWidget(self.frame_fk_scheme, 2, 2, 1, 1)

        self.frame_fk_dh = QFrame(self.tab_fk_input_parameters)
        self.frame_fk_dh.setObjectName(u"frame_fk_dh")
        self.frame_fk_dh.setMinimumSize(QSize(462, 285))
        self.frame_fk_dh.setFrameShape(QFrame.StyledPanel)
        self.frame_fk_dh.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_fk_dh)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tableWidget_fk_dh = QTableWidget(self.frame_fk_dh)
        if (self.tableWidget_fk_dh.columnCount() < 4):
            self.tableWidget_fk_dh.setColumnCount(4)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        font5 = QFont()
        font5.setBold(True)
        font5.setWeight(75)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem32.setFont(font5);
        __qtablewidgetitem32.setForeground(brush);
        self.tableWidget_fk_dh.setHorizontalHeaderItem(0, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem33.setFont(font5);
        __qtablewidgetitem33.setForeground(brush);
        self.tableWidget_fk_dh.setHorizontalHeaderItem(1, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem34.setFont(font5);
        __qtablewidgetitem34.setForeground(brush);
        self.tableWidget_fk_dh.setHorizontalHeaderItem(2, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem35.setFont(font5);
        __qtablewidgetitem35.setForeground(brush);
        self.tableWidget_fk_dh.setHorizontalHeaderItem(3, __qtablewidgetitem35)
        if (self.tableWidget_fk_dh.rowCount() < 5):
            self.tableWidget_fk_dh.setRowCount(5)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget_fk_dh.setVerticalHeaderItem(0, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget_fk_dh.setVerticalHeaderItem(1, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget_fk_dh.setVerticalHeaderItem(2, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableWidget_fk_dh.setVerticalHeaderItem(3, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableWidget_fk_dh.setVerticalHeaderItem(4, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        __qtablewidgetitem41.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_dh.setItem(0, 0, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        __qtablewidgetitem42.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_dh.setItem(0, 1, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        __qtablewidgetitem43.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_dh.setItem(0, 2, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        __qtablewidgetitem44.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_dh.setItem(0, 3, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        __qtablewidgetitem45.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_dh.setItem(1, 0, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        __qtablewidgetitem46.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_dh.setItem(1, 1, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        __qtablewidgetitem47.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_dh.setItem(1, 2, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        __qtablewidgetitem48.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_dh.setItem(1, 3, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        __qtablewidgetitem49.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_dh.setItem(2, 0, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        __qtablewidgetitem50.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_dh.setItem(2, 1, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        __qtablewidgetitem51.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_dh.setItem(2, 2, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        __qtablewidgetitem52.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_dh.setItem(2, 3, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        __qtablewidgetitem53.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_dh.setItem(3, 0, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        __qtablewidgetitem54.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_dh.setItem(3, 1, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        __qtablewidgetitem55.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_dh.setItem(3, 2, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        __qtablewidgetitem56.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_dh.setItem(3, 3, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        __qtablewidgetitem57.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_dh.setItem(4, 0, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        __qtablewidgetitem58.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_dh.setItem(4, 1, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        __qtablewidgetitem59.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_dh.setItem(4, 2, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        __qtablewidgetitem60.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_dh.setItem(4, 3, __qtablewidgetitem60)
        self.tableWidget_fk_dh.setObjectName(u"tableWidget_fk_dh")
        sizePolicy4.setHeightForWidth(self.tableWidget_fk_dh.sizePolicy().hasHeightForWidth())
        self.tableWidget_fk_dh.setSizePolicy(sizePolicy4)
        self.tableWidget_fk_dh.setMinimumSize(QSize(386, 250))
        self.tableWidget_fk_dh.setMaximumSize(QSize(900, 16777215))
        self.tableWidget_fk_dh.setFrameShape(QFrame.NoFrame)
        self.tableWidget_fk_dh.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_fk_dh.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_fk_dh.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget_fk_dh.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget_fk_dh.setTextElideMode(Qt.ElideNone)
        self.tableWidget_fk_dh.setWordWrap(False)
        self.tableWidget_fk_dh.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_fk_dh.horizontalHeader().setMinimumSectionSize(41)
        self.tableWidget_fk_dh.horizontalHeader().setDefaultSectionSize(90)
        self.tableWidget_fk_dh.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_fk_dh.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_fk_dh.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget_fk_dh.verticalHeader().setMinimumSectionSize(40)
        self.tableWidget_fk_dh.verticalHeader().setDefaultSectionSize(40)
        self.tableWidget_fk_dh.verticalHeader().setHighlightSections(True)
        self.tableWidget_fk_dh.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_fk_dh.verticalHeader().setStretchLastSection(False)

        self.gridLayout_4.addWidget(self.tableWidget_fk_dh, 1, 0, 1, 1, Qt.AlignLeft)

        self.horizontalSpacer_11 = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_11, 1, 1, 1, 1)

        self.label_fk_dh = QLabel(self.frame_fk_dh)
        self.label_fk_dh.setObjectName(u"label_fk_dh")
        sizePolicy1.setHeightForWidth(self.label_fk_dh.sizePolicy().hasHeightForWidth())
        self.label_fk_dh.setSizePolicy(sizePolicy1)
        self.label_fk_dh.setMinimumSize(QSize(386, 25))
        font6 = QFont()
        font6.setPointSize(10)
        font6.setBold(True)
        font6.setWeight(75)
        self.label_fk_dh.setFont(font6)

        self.gridLayout_4.addWidget(self.label_fk_dh, 0, 0, 1, 1, Qt.AlignBottom)


        self.gridLayout.addWidget(self.frame_fk_dh, 2, 0, 1, 1)

        self.tabWidget_fk.addTab(self.tab_fk_input_parameters, "")
        self.tab_fk_hom_matrices = QWidget()
        self.tab_fk_hom_matrices.setObjectName(u"tab_fk_hom_matrices")
        self.gridLayout_7 = QGridLayout(self.tab_fk_hom_matrices)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_T12 = QLabel(self.tab_fk_hom_matrices)
        self.label_T12.setObjectName(u"label_T12")
        font7 = QFont()
        font7.setPointSize(14)
        self.label_T12.setFont(font7)
        self.label_T12.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_T12, 0, 0, 1, 1)

        self.label_T14 = QLabel(self.tab_fk_hom_matrices)
        self.label_T14.setObjectName(u"label_T14")
        self.label_T14.setFont(font7)
        self.label_T14.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_T14, 0, 1, 1, 1)

        self.tableWidget_fk_T12 = QTableWidget(self.tab_fk_hom_matrices)
        if (self.tableWidget_fk_T12.columnCount() < 4):
            self.tableWidget_fk_T12.setColumnCount(4)
        __qtablewidgetitem61 = QTableWidgetItem()
        __qtablewidgetitem61.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem61.setFont(font5);
        __qtablewidgetitem61.setForeground(brush);
        self.tableWidget_fk_T12.setHorizontalHeaderItem(0, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        __qtablewidgetitem62.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem62.setFont(font5);
        __qtablewidgetitem62.setForeground(brush);
        self.tableWidget_fk_T12.setHorizontalHeaderItem(1, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        __qtablewidgetitem63.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem63.setFont(font5);
        __qtablewidgetitem63.setForeground(brush);
        self.tableWidget_fk_T12.setHorizontalHeaderItem(2, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        __qtablewidgetitem64.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem64.setFont(font5);
        __qtablewidgetitem64.setForeground(brush);
        self.tableWidget_fk_T12.setHorizontalHeaderItem(3, __qtablewidgetitem64)
        if (self.tableWidget_fk_T12.rowCount() < 4):
            self.tableWidget_fk_T12.setRowCount(4)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.tableWidget_fk_T12.setVerticalHeaderItem(0, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        self.tableWidget_fk_T12.setVerticalHeaderItem(1, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        self.tableWidget_fk_T12.setVerticalHeaderItem(2, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.tableWidget_fk_T12.setVerticalHeaderItem(3, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        __qtablewidgetitem69.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T12.setItem(0, 0, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        __qtablewidgetitem70.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T12.setItem(0, 1, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        __qtablewidgetitem71.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T12.setItem(0, 2, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        __qtablewidgetitem72.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T12.setItem(0, 3, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        __qtablewidgetitem73.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T12.setItem(1, 0, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        __qtablewidgetitem74.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T12.setItem(1, 1, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        __qtablewidgetitem75.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T12.setItem(1, 2, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        __qtablewidgetitem76.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T12.setItem(1, 3, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        __qtablewidgetitem77.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T12.setItem(2, 0, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        __qtablewidgetitem78.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T12.setItem(2, 1, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        __qtablewidgetitem79.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T12.setItem(2, 2, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        __qtablewidgetitem80.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T12.setItem(2, 3, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        __qtablewidgetitem81.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T12.setItem(3, 0, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        __qtablewidgetitem82.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T12.setItem(3, 1, __qtablewidgetitem82)
        __qtablewidgetitem83 = QTableWidgetItem()
        __qtablewidgetitem83.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T12.setItem(3, 2, __qtablewidgetitem83)
        __qtablewidgetitem84 = QTableWidgetItem()
        __qtablewidgetitem84.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T12.setItem(3, 3, __qtablewidgetitem84)
        self.tableWidget_fk_T12.setObjectName(u"tableWidget_fk_T12")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.tableWidget_fk_T12.sizePolicy().hasHeightForWidth())
        self.tableWidget_fk_T12.setSizePolicy(sizePolicy5)
        self.tableWidget_fk_T12.setMinimumSize(QSize(410, 140))
        self.tableWidget_fk_T12.setFrameShape(QFrame.NoFrame)
        self.tableWidget_fk_T12.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_fk_T12.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_fk_T12.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableWidget_fk_T12.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget_fk_T12.setTextElideMode(Qt.ElideNone)
        self.tableWidget_fk_T12.setWordWrap(False)
        self.tableWidget_fk_T12.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_fk_T12.horizontalHeader().setMinimumSectionSize(25)
        self.tableWidget_fk_T12.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget_fk_T12.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_fk_T12.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_fk_T12.verticalHeader().setDefaultSectionSize(25)
        self.tableWidget_fk_T12.verticalHeader().setHighlightSections(False)
        self.tableWidget_fk_T12.verticalHeader().setStretchLastSection(False)

        self.gridLayout_7.addWidget(self.tableWidget_fk_T12, 1, 0, 1, 1)

        self.tableWidget_fk_T14 = QTableWidget(self.tab_fk_hom_matrices)
        if (self.tableWidget_fk_T14.columnCount() < 4):
            self.tableWidget_fk_T14.setColumnCount(4)
        __qtablewidgetitem85 = QTableWidgetItem()
        __qtablewidgetitem85.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem85.setFont(font5);
        __qtablewidgetitem85.setForeground(brush);
        self.tableWidget_fk_T14.setHorizontalHeaderItem(0, __qtablewidgetitem85)
        __qtablewidgetitem86 = QTableWidgetItem()
        __qtablewidgetitem86.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem86.setFont(font5);
        __qtablewidgetitem86.setForeground(brush);
        self.tableWidget_fk_T14.setHorizontalHeaderItem(1, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        __qtablewidgetitem87.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem87.setFont(font5);
        __qtablewidgetitem87.setForeground(brush);
        self.tableWidget_fk_T14.setHorizontalHeaderItem(2, __qtablewidgetitem87)
        __qtablewidgetitem88 = QTableWidgetItem()
        __qtablewidgetitem88.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem88.setFont(font5);
        __qtablewidgetitem88.setForeground(brush);
        self.tableWidget_fk_T14.setHorizontalHeaderItem(3, __qtablewidgetitem88)
        if (self.tableWidget_fk_T14.rowCount() < 4):
            self.tableWidget_fk_T14.setRowCount(4)
        __qtablewidgetitem89 = QTableWidgetItem()
        self.tableWidget_fk_T14.setVerticalHeaderItem(0, __qtablewidgetitem89)
        __qtablewidgetitem90 = QTableWidgetItem()
        self.tableWidget_fk_T14.setVerticalHeaderItem(1, __qtablewidgetitem90)
        __qtablewidgetitem91 = QTableWidgetItem()
        self.tableWidget_fk_T14.setVerticalHeaderItem(2, __qtablewidgetitem91)
        __qtablewidgetitem92 = QTableWidgetItem()
        self.tableWidget_fk_T14.setVerticalHeaderItem(3, __qtablewidgetitem92)
        __qtablewidgetitem93 = QTableWidgetItem()
        __qtablewidgetitem93.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T14.setItem(0, 0, __qtablewidgetitem93)
        __qtablewidgetitem94 = QTableWidgetItem()
        __qtablewidgetitem94.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T14.setItem(0, 1, __qtablewidgetitem94)
        __qtablewidgetitem95 = QTableWidgetItem()
        __qtablewidgetitem95.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T14.setItem(0, 2, __qtablewidgetitem95)
        __qtablewidgetitem96 = QTableWidgetItem()
        __qtablewidgetitem96.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T14.setItem(0, 3, __qtablewidgetitem96)
        __qtablewidgetitem97 = QTableWidgetItem()
        __qtablewidgetitem97.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T14.setItem(1, 0, __qtablewidgetitem97)
        __qtablewidgetitem98 = QTableWidgetItem()
        __qtablewidgetitem98.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T14.setItem(1, 1, __qtablewidgetitem98)
        __qtablewidgetitem99 = QTableWidgetItem()
        __qtablewidgetitem99.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T14.setItem(1, 2, __qtablewidgetitem99)
        __qtablewidgetitem100 = QTableWidgetItem()
        __qtablewidgetitem100.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T14.setItem(1, 3, __qtablewidgetitem100)
        __qtablewidgetitem101 = QTableWidgetItem()
        __qtablewidgetitem101.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T14.setItem(2, 0, __qtablewidgetitem101)
        __qtablewidgetitem102 = QTableWidgetItem()
        __qtablewidgetitem102.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T14.setItem(2, 1, __qtablewidgetitem102)
        __qtablewidgetitem103 = QTableWidgetItem()
        __qtablewidgetitem103.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T14.setItem(2, 2, __qtablewidgetitem103)
        __qtablewidgetitem104 = QTableWidgetItem()
        __qtablewidgetitem104.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T14.setItem(2, 3, __qtablewidgetitem104)
        __qtablewidgetitem105 = QTableWidgetItem()
        __qtablewidgetitem105.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T14.setItem(3, 0, __qtablewidgetitem105)
        __qtablewidgetitem106 = QTableWidgetItem()
        __qtablewidgetitem106.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T14.setItem(3, 1, __qtablewidgetitem106)
        __qtablewidgetitem107 = QTableWidgetItem()
        __qtablewidgetitem107.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T14.setItem(3, 2, __qtablewidgetitem107)
        __qtablewidgetitem108 = QTableWidgetItem()
        __qtablewidgetitem108.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T14.setItem(3, 3, __qtablewidgetitem108)
        self.tableWidget_fk_T14.setObjectName(u"tableWidget_fk_T14")
        sizePolicy5.setHeightForWidth(self.tableWidget_fk_T14.sizePolicy().hasHeightForWidth())
        self.tableWidget_fk_T14.setSizePolicy(sizePolicy5)
        self.tableWidget_fk_T14.setMinimumSize(QSize(410, 140))
        self.tableWidget_fk_T14.setFrameShape(QFrame.NoFrame)
        self.tableWidget_fk_T14.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_fk_T14.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_fk_T14.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableWidget_fk_T14.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget_fk_T14.setTextElideMode(Qt.ElideNone)
        self.tableWidget_fk_T14.setWordWrap(False)
        self.tableWidget_fk_T14.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_fk_T14.horizontalHeader().setMinimumSectionSize(25)
        self.tableWidget_fk_T14.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget_fk_T14.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_fk_T14.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_fk_T14.verticalHeader().setDefaultSectionSize(25)
        self.tableWidget_fk_T14.verticalHeader().setHighlightSections(False)
        self.tableWidget_fk_T14.verticalHeader().setStretchLastSection(False)

        self.gridLayout_7.addWidget(self.tableWidget_fk_T14, 1, 1, 1, 1)

        self.label_T13 = QLabel(self.tab_fk_hom_matrices)
        self.label_T13.setObjectName(u"label_T13")
        self.label_T13.setFont(font7)
        self.label_T13.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_T13, 2, 0, 1, 1)

        self.label_T15 = QLabel(self.tab_fk_hom_matrices)
        self.label_T15.setObjectName(u"label_T15")
        self.label_T15.setFont(font7)
        self.label_T15.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_T15, 2, 1, 1, 1)

        self.tableWidget_fk_T13 = QTableWidget(self.tab_fk_hom_matrices)
        if (self.tableWidget_fk_T13.columnCount() < 4):
            self.tableWidget_fk_T13.setColumnCount(4)
        __qtablewidgetitem109 = QTableWidgetItem()
        __qtablewidgetitem109.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem109.setFont(font5);
        __qtablewidgetitem109.setForeground(brush);
        self.tableWidget_fk_T13.setHorizontalHeaderItem(0, __qtablewidgetitem109)
        __qtablewidgetitem110 = QTableWidgetItem()
        __qtablewidgetitem110.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem110.setFont(font5);
        __qtablewidgetitem110.setForeground(brush);
        self.tableWidget_fk_T13.setHorizontalHeaderItem(1, __qtablewidgetitem110)
        __qtablewidgetitem111 = QTableWidgetItem()
        __qtablewidgetitem111.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem111.setFont(font5);
        __qtablewidgetitem111.setForeground(brush);
        self.tableWidget_fk_T13.setHorizontalHeaderItem(2, __qtablewidgetitem111)
        __qtablewidgetitem112 = QTableWidgetItem()
        __qtablewidgetitem112.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem112.setFont(font5);
        __qtablewidgetitem112.setForeground(brush);
        self.tableWidget_fk_T13.setHorizontalHeaderItem(3, __qtablewidgetitem112)
        if (self.tableWidget_fk_T13.rowCount() < 4):
            self.tableWidget_fk_T13.setRowCount(4)
        __qtablewidgetitem113 = QTableWidgetItem()
        self.tableWidget_fk_T13.setVerticalHeaderItem(0, __qtablewidgetitem113)
        __qtablewidgetitem114 = QTableWidgetItem()
        self.tableWidget_fk_T13.setVerticalHeaderItem(1, __qtablewidgetitem114)
        __qtablewidgetitem115 = QTableWidgetItem()
        self.tableWidget_fk_T13.setVerticalHeaderItem(2, __qtablewidgetitem115)
        __qtablewidgetitem116 = QTableWidgetItem()
        self.tableWidget_fk_T13.setVerticalHeaderItem(3, __qtablewidgetitem116)
        __qtablewidgetitem117 = QTableWidgetItem()
        __qtablewidgetitem117.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T13.setItem(0, 0, __qtablewidgetitem117)
        __qtablewidgetitem118 = QTableWidgetItem()
        __qtablewidgetitem118.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T13.setItem(0, 1, __qtablewidgetitem118)
        __qtablewidgetitem119 = QTableWidgetItem()
        __qtablewidgetitem119.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T13.setItem(0, 2, __qtablewidgetitem119)
        __qtablewidgetitem120 = QTableWidgetItem()
        __qtablewidgetitem120.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T13.setItem(0, 3, __qtablewidgetitem120)
        __qtablewidgetitem121 = QTableWidgetItem()
        __qtablewidgetitem121.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T13.setItem(1, 0, __qtablewidgetitem121)
        __qtablewidgetitem122 = QTableWidgetItem()
        __qtablewidgetitem122.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T13.setItem(1, 1, __qtablewidgetitem122)
        __qtablewidgetitem123 = QTableWidgetItem()
        __qtablewidgetitem123.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T13.setItem(1, 2, __qtablewidgetitem123)
        __qtablewidgetitem124 = QTableWidgetItem()
        __qtablewidgetitem124.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T13.setItem(1, 3, __qtablewidgetitem124)
        __qtablewidgetitem125 = QTableWidgetItem()
        __qtablewidgetitem125.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T13.setItem(2, 0, __qtablewidgetitem125)
        __qtablewidgetitem126 = QTableWidgetItem()
        __qtablewidgetitem126.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T13.setItem(2, 1, __qtablewidgetitem126)
        __qtablewidgetitem127 = QTableWidgetItem()
        __qtablewidgetitem127.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T13.setItem(2, 2, __qtablewidgetitem127)
        __qtablewidgetitem128 = QTableWidgetItem()
        __qtablewidgetitem128.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T13.setItem(2, 3, __qtablewidgetitem128)
        __qtablewidgetitem129 = QTableWidgetItem()
        __qtablewidgetitem129.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T13.setItem(3, 0, __qtablewidgetitem129)
        __qtablewidgetitem130 = QTableWidgetItem()
        __qtablewidgetitem130.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T13.setItem(3, 1, __qtablewidgetitem130)
        __qtablewidgetitem131 = QTableWidgetItem()
        __qtablewidgetitem131.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T13.setItem(3, 2, __qtablewidgetitem131)
        __qtablewidgetitem132 = QTableWidgetItem()
        __qtablewidgetitem132.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T13.setItem(3, 3, __qtablewidgetitem132)
        self.tableWidget_fk_T13.setObjectName(u"tableWidget_fk_T13")
        sizePolicy5.setHeightForWidth(self.tableWidget_fk_T13.sizePolicy().hasHeightForWidth())
        self.tableWidget_fk_T13.setSizePolicy(sizePolicy5)
        self.tableWidget_fk_T13.setMinimumSize(QSize(410, 140))
        self.tableWidget_fk_T13.setFrameShape(QFrame.NoFrame)
        self.tableWidget_fk_T13.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_fk_T13.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_fk_T13.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableWidget_fk_T13.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget_fk_T13.setTextElideMode(Qt.ElideNone)
        self.tableWidget_fk_T13.setWordWrap(False)
        self.tableWidget_fk_T13.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_fk_T13.horizontalHeader().setMinimumSectionSize(25)
        self.tableWidget_fk_T13.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget_fk_T13.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_fk_T13.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_fk_T13.verticalHeader().setDefaultSectionSize(25)
        self.tableWidget_fk_T13.verticalHeader().setHighlightSections(False)
        self.tableWidget_fk_T13.verticalHeader().setStretchLastSection(False)

        self.gridLayout_7.addWidget(self.tableWidget_fk_T13, 3, 0, 1, 1)

        self.tableWidget_fk_T15 = QTableWidget(self.tab_fk_hom_matrices)
        if (self.tableWidget_fk_T15.columnCount() < 4):
            self.tableWidget_fk_T15.setColumnCount(4)
        __qtablewidgetitem133 = QTableWidgetItem()
        __qtablewidgetitem133.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem133.setFont(font5);
        __qtablewidgetitem133.setForeground(brush);
        self.tableWidget_fk_T15.setHorizontalHeaderItem(0, __qtablewidgetitem133)
        __qtablewidgetitem134 = QTableWidgetItem()
        __qtablewidgetitem134.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem134.setFont(font5);
        __qtablewidgetitem134.setForeground(brush);
        self.tableWidget_fk_T15.setHorizontalHeaderItem(1, __qtablewidgetitem134)
        __qtablewidgetitem135 = QTableWidgetItem()
        __qtablewidgetitem135.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem135.setFont(font5);
        __qtablewidgetitem135.setForeground(brush);
        self.tableWidget_fk_T15.setHorizontalHeaderItem(2, __qtablewidgetitem135)
        __qtablewidgetitem136 = QTableWidgetItem()
        __qtablewidgetitem136.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem136.setFont(font5);
        __qtablewidgetitem136.setForeground(brush);
        self.tableWidget_fk_T15.setHorizontalHeaderItem(3, __qtablewidgetitem136)
        if (self.tableWidget_fk_T15.rowCount() < 4):
            self.tableWidget_fk_T15.setRowCount(4)
        __qtablewidgetitem137 = QTableWidgetItem()
        self.tableWidget_fk_T15.setVerticalHeaderItem(0, __qtablewidgetitem137)
        __qtablewidgetitem138 = QTableWidgetItem()
        self.tableWidget_fk_T15.setVerticalHeaderItem(1, __qtablewidgetitem138)
        __qtablewidgetitem139 = QTableWidgetItem()
        self.tableWidget_fk_T15.setVerticalHeaderItem(2, __qtablewidgetitem139)
        __qtablewidgetitem140 = QTableWidgetItem()
        self.tableWidget_fk_T15.setVerticalHeaderItem(3, __qtablewidgetitem140)
        __qtablewidgetitem141 = QTableWidgetItem()
        __qtablewidgetitem141.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T15.setItem(0, 0, __qtablewidgetitem141)
        __qtablewidgetitem142 = QTableWidgetItem()
        __qtablewidgetitem142.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T15.setItem(0, 1, __qtablewidgetitem142)
        __qtablewidgetitem143 = QTableWidgetItem()
        __qtablewidgetitem143.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T15.setItem(0, 2, __qtablewidgetitem143)
        brush1 = QBrush(QColor(0, 170, 0, 255))
        brush1.setStyle(Qt.NoBrush)
        brush2 = QBrush(QColor(0, 170, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        font8 = QFont()
        font8.setBold(True)
        font8.setUnderline(True)
        font8.setWeight(75)
        __qtablewidgetitem144 = QTableWidgetItem()
        __qtablewidgetitem144.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem144.setFont(font8);
        __qtablewidgetitem144.setBackground(brush2);
        __qtablewidgetitem144.setForeground(brush1);
        self.tableWidget_fk_T15.setItem(0, 3, __qtablewidgetitem144)
        __qtablewidgetitem145 = QTableWidgetItem()
        __qtablewidgetitem145.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T15.setItem(1, 0, __qtablewidgetitem145)
        __qtablewidgetitem146 = QTableWidgetItem()
        __qtablewidgetitem146.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T15.setItem(1, 1, __qtablewidgetitem146)
        __qtablewidgetitem147 = QTableWidgetItem()
        __qtablewidgetitem147.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T15.setItem(1, 2, __qtablewidgetitem147)
        brush3 = QBrush(QColor(0, 170, 0, 255))
        brush3.setStyle(Qt.SolidPattern)
        __qtablewidgetitem148 = QTableWidgetItem()
        __qtablewidgetitem148.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem148.setFont(font8);
        __qtablewidgetitem148.setForeground(brush3);
        self.tableWidget_fk_T15.setItem(1, 3, __qtablewidgetitem148)
        __qtablewidgetitem149 = QTableWidgetItem()
        __qtablewidgetitem149.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T15.setItem(2, 0, __qtablewidgetitem149)
        __qtablewidgetitem150 = QTableWidgetItem()
        __qtablewidgetitem150.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T15.setItem(2, 1, __qtablewidgetitem150)
        __qtablewidgetitem151 = QTableWidgetItem()
        __qtablewidgetitem151.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T15.setItem(2, 2, __qtablewidgetitem151)
        __qtablewidgetitem152 = QTableWidgetItem()
        __qtablewidgetitem152.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem152.setFont(font8);
        __qtablewidgetitem152.setForeground(brush3);
        self.tableWidget_fk_T15.setItem(2, 3, __qtablewidgetitem152)
        __qtablewidgetitem153 = QTableWidgetItem()
        __qtablewidgetitem153.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T15.setItem(3, 0, __qtablewidgetitem153)
        __qtablewidgetitem154 = QTableWidgetItem()
        __qtablewidgetitem154.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T15.setItem(3, 1, __qtablewidgetitem154)
        __qtablewidgetitem155 = QTableWidgetItem()
        __qtablewidgetitem155.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T15.setItem(3, 2, __qtablewidgetitem155)
        __qtablewidgetitem156 = QTableWidgetItem()
        __qtablewidgetitem156.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_fk_T15.setItem(3, 3, __qtablewidgetitem156)
        self.tableWidget_fk_T15.setObjectName(u"tableWidget_fk_T15")
        sizePolicy5.setHeightForWidth(self.tableWidget_fk_T15.sizePolicy().hasHeightForWidth())
        self.tableWidget_fk_T15.setSizePolicy(sizePolicy5)
        self.tableWidget_fk_T15.setMinimumSize(QSize(410, 140))
        self.tableWidget_fk_T15.setFrameShape(QFrame.NoFrame)
        self.tableWidget_fk_T15.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_fk_T15.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_fk_T15.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableWidget_fk_T15.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget_fk_T15.setTextElideMode(Qt.ElideNone)
        self.tableWidget_fk_T15.setWordWrap(False)
        self.tableWidget_fk_T15.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_fk_T15.horizontalHeader().setMinimumSectionSize(25)
        self.tableWidget_fk_T15.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget_fk_T15.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_fk_T15.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_fk_T15.verticalHeader().setDefaultSectionSize(25)
        self.tableWidget_fk_T15.verticalHeader().setHighlightSections(False)
        self.tableWidget_fk_T15.verticalHeader().setStretchLastSection(False)

        self.gridLayout_7.addWidget(self.tableWidget_fk_T15, 3, 1, 1, 1)

        self.tabWidget_fk.addTab(self.tab_fk_hom_matrices, "")
        self.tab_fk_user = QWidget()
        self.tab_fk_user.setObjectName(u"tab_fk_user")
        self.gridLayout_2 = QGridLayout(self.tab_fk_user)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_fk_user_input = QFrame(self.tab_fk_user)
        self.frame_fk_user_input.setObjectName(u"frame_fk_user_input")
        sizePolicy6 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame_fk_user_input.sizePolicy().hasHeightForWidth())
        self.frame_fk_user_input.setSizePolicy(sizePolicy6)
        self.frame_fk_user_input.setMinimumSize(QSize(462, 285))
        self.frame_fk_user_input.setMaximumSize(QSize(900, 16777215))
        self.frame_fk_user_input.setFrameShape(QFrame.StyledPanel)
        self.frame_fk_user_input.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_fk_user_input)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.tableWidget_8 = QTableWidget(self.frame_fk_user_input)
        if (self.tableWidget_8.columnCount() < 4):
            self.tableWidget_8.setColumnCount(4)
        __qtablewidgetitem157 = QTableWidgetItem()
        __qtablewidgetitem157.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem157.setFont(font5);
        __qtablewidgetitem157.setForeground(brush);
        self.tableWidget_8.setHorizontalHeaderItem(0, __qtablewidgetitem157)
        __qtablewidgetitem158 = QTableWidgetItem()
        __qtablewidgetitem158.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem158.setFont(font5);
        __qtablewidgetitem158.setForeground(brush);
        self.tableWidget_8.setHorizontalHeaderItem(1, __qtablewidgetitem158)
        __qtablewidgetitem159 = QTableWidgetItem()
        __qtablewidgetitem159.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem159.setFont(font5);
        __qtablewidgetitem159.setForeground(brush);
        self.tableWidget_8.setHorizontalHeaderItem(2, __qtablewidgetitem159)
        __qtablewidgetitem160 = QTableWidgetItem()
        __qtablewidgetitem160.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem160.setFont(font5);
        __qtablewidgetitem160.setForeground(brush);
        self.tableWidget_8.setHorizontalHeaderItem(3, __qtablewidgetitem160)
        if (self.tableWidget_8.rowCount() < 5):
            self.tableWidget_8.setRowCount(5)
        __qtablewidgetitem161 = QTableWidgetItem()
        self.tableWidget_8.setVerticalHeaderItem(0, __qtablewidgetitem161)
        __qtablewidgetitem162 = QTableWidgetItem()
        self.tableWidget_8.setVerticalHeaderItem(1, __qtablewidgetitem162)
        __qtablewidgetitem163 = QTableWidgetItem()
        self.tableWidget_8.setVerticalHeaderItem(2, __qtablewidgetitem163)
        __qtablewidgetitem164 = QTableWidgetItem()
        self.tableWidget_8.setVerticalHeaderItem(3, __qtablewidgetitem164)
        __qtablewidgetitem165 = QTableWidgetItem()
        self.tableWidget_8.setVerticalHeaderItem(4, __qtablewidgetitem165)
        __qtablewidgetitem166 = QTableWidgetItem()
        __qtablewidgetitem166.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_8.setItem(0, 0, __qtablewidgetitem166)
        __qtablewidgetitem167 = QTableWidgetItem()
        __qtablewidgetitem167.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_8.setItem(0, 1, __qtablewidgetitem167)
        __qtablewidgetitem168 = QTableWidgetItem()
        __qtablewidgetitem168.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_8.setItem(0, 2, __qtablewidgetitem168)
        __qtablewidgetitem169 = QTableWidgetItem()
        __qtablewidgetitem169.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_8.setItem(0, 3, __qtablewidgetitem169)
        __qtablewidgetitem170 = QTableWidgetItem()
        __qtablewidgetitem170.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_8.setItem(1, 0, __qtablewidgetitem170)
        __qtablewidgetitem171 = QTableWidgetItem()
        __qtablewidgetitem171.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_8.setItem(1, 1, __qtablewidgetitem171)
        __qtablewidgetitem172 = QTableWidgetItem()
        __qtablewidgetitem172.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_8.setItem(1, 2, __qtablewidgetitem172)
        __qtablewidgetitem173 = QTableWidgetItem()
        __qtablewidgetitem173.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_8.setItem(1, 3, __qtablewidgetitem173)
        __qtablewidgetitem174 = QTableWidgetItem()
        __qtablewidgetitem174.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_8.setItem(2, 0, __qtablewidgetitem174)
        __qtablewidgetitem175 = QTableWidgetItem()
        __qtablewidgetitem175.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_8.setItem(2, 1, __qtablewidgetitem175)
        __qtablewidgetitem176 = QTableWidgetItem()
        __qtablewidgetitem176.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_8.setItem(2, 2, __qtablewidgetitem176)
        __qtablewidgetitem177 = QTableWidgetItem()
        __qtablewidgetitem177.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_8.setItem(2, 3, __qtablewidgetitem177)
        __qtablewidgetitem178 = QTableWidgetItem()
        __qtablewidgetitem178.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_8.setItem(3, 0, __qtablewidgetitem178)
        __qtablewidgetitem179 = QTableWidgetItem()
        __qtablewidgetitem179.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_8.setItem(3, 1, __qtablewidgetitem179)
        __qtablewidgetitem180 = QTableWidgetItem()
        __qtablewidgetitem180.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_8.setItem(3, 2, __qtablewidgetitem180)
        __qtablewidgetitem181 = QTableWidgetItem()
        __qtablewidgetitem181.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_8.setItem(3, 3, __qtablewidgetitem181)
        __qtablewidgetitem182 = QTableWidgetItem()
        __qtablewidgetitem182.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_8.setItem(4, 0, __qtablewidgetitem182)
        __qtablewidgetitem183 = QTableWidgetItem()
        __qtablewidgetitem183.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_8.setItem(4, 1, __qtablewidgetitem183)
        __qtablewidgetitem184 = QTableWidgetItem()
        __qtablewidgetitem184.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_8.setItem(4, 2, __qtablewidgetitem184)
        __qtablewidgetitem185 = QTableWidgetItem()
        __qtablewidgetitem185.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_8.setItem(4, 3, __qtablewidgetitem185)
        self.tableWidget_8.setObjectName(u"tableWidget_8")
        sizePolicy3.setHeightForWidth(self.tableWidget_8.sizePolicy().hasHeightForWidth())
        self.tableWidget_8.setSizePolicy(sizePolicy3)
        self.tableWidget_8.setMinimumSize(QSize(440, 250))
        self.tableWidget_8.setMaximumSize(QSize(900, 16777215))
        self.tableWidget_8.setFrameShape(QFrame.NoFrame)
        self.tableWidget_8.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_8.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_8.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget_8.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget_8.setTextElideMode(Qt.ElideNone)
        self.tableWidget_8.setWordWrap(False)
        self.tableWidget_8.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_8.horizontalHeader().setMinimumSectionSize(100)
        self.tableWidget_8.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget_8.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_8.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_8.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget_8.verticalHeader().setMinimumSectionSize(40)
        self.tableWidget_8.verticalHeader().setDefaultSectionSize(40)
        self.tableWidget_8.verticalHeader().setHighlightSections(True)
        self.tableWidget_8.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_8.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_16.addWidget(self.tableWidget_8)


        self.gridLayout_2.addWidget(self.frame_fk_user_input, 0, 0, 1, 1)

        self.frame_fk_user_extra = QFrame(self.tab_fk_user)
        self.frame_fk_user_extra.setObjectName(u"frame_fk_user_extra")
        self.frame_fk_user_extra.setMinimumSize(QSize(462, 285))
        self.frame_fk_user_extra.setMaximumSize(QSize(16777215, 16777215))
        self.frame_fk_user_extra.setFrameShape(QFrame.StyledPanel)
        self.frame_fk_user_extra.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_fk_user_extra)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_9)


        self.gridLayout_2.addWidget(self.frame_fk_user_extra, 1, 3, 2, 1)

        self.frame_fk_user_solve = QFrame(self.tab_fk_user)
        self.frame_fk_user_solve.setObjectName(u"frame_fk_user_solve")
        self.frame_fk_user_solve.setMinimumSize(QSize(462, 285))
        self.frame_fk_user_solve.setFrameShape(QFrame.StyledPanel)
        self.frame_fk_user_solve.setFrameShadow(QFrame.Raised)
        self.gridLayout_17 = QGridLayout(self.frame_fk_user_solve)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.btn_fk_user_solve = QPushButton(self.frame_fk_user_solve)
        self.btn_fk_user_solve.setObjectName(u"btn_fk_user_solve")
        sizePolicy4.setHeightForWidth(self.btn_fk_user_solve.sizePolicy().hasHeightForWidth())
        self.btn_fk_user_solve.setSizePolicy(sizePolicy4)
        self.btn_fk_user_solve.setMinimumSize(QSize(50, 50))
        self.btn_fk_user_solve.setMaximumSize(QSize(50, 50))
        self.btn_fk_user_solve.setSizeIncrement(QSize(10, 10))
        self.btn_fk_user_solve.setBaseSize(QSize(100, 100))
        self.btn_fk_user_solve.setFont(font3)
        self.btn_fk_user_solve.setLayoutDirection(Qt.LeftToRight)
        self.btn_fk_user_solve.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(222, 222, 222);\n"
"    border: 2px solid #555;\n"
"    border-radius: 25px;\n"
"    border-style: outset;\n"
"	background-color: rgb(2, 50, 70);\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(40, 112, 148);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.gridLayout_17.addWidget(self.btn_fk_user_solve, 2, 1, 1, 1, Qt.AlignBottom)

        self.btn_fk_user_sub = QPushButton(self.frame_fk_user_solve)
        self.btn_fk_user_sub.setObjectName(u"btn_fk_user_sub")
        sizePolicy4.setHeightForWidth(self.btn_fk_user_sub.sizePolicy().hasHeightForWidth())
        self.btn_fk_user_sub.setSizePolicy(sizePolicy4)
        self.btn_fk_user_sub.setMinimumSize(QSize(50, 50))
        self.btn_fk_user_sub.setMaximumSize(QSize(50, 50))
        self.btn_fk_user_sub.setSizeIncrement(QSize(10, 10))
        self.btn_fk_user_sub.setBaseSize(QSize(100, 100))
        self.btn_fk_user_sub.setFont(font3)
        self.btn_fk_user_sub.setLayoutDirection(Qt.LeftToRight)
        self.btn_fk_user_sub.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(222, 222, 222);\n"
"    border: 2px solid #555;\n"
"    border-radius: 25px;\n"
"    border-style: outset;\n"
"	background-color: rgb(2, 50, 70);\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(40, 112, 148);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.gridLayout_17.addWidget(self.btn_fk_user_sub, 0, 2, 1, 1, Qt.AlignTop)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_8, 0, 3, 1, 1)

        self.btn_fk_user_add = QPushButton(self.frame_fk_user_solve)
        self.btn_fk_user_add.setObjectName(u"btn_fk_user_add")
        sizePolicy4.setHeightForWidth(self.btn_fk_user_add.sizePolicy().hasHeightForWidth())
        self.btn_fk_user_add.setSizePolicy(sizePolicy4)
        self.btn_fk_user_add.setMinimumSize(QSize(50, 50))
        self.btn_fk_user_add.setMaximumSize(QSize(50, 50))
        self.btn_fk_user_add.setSizeIncrement(QSize(10, 10))
        self.btn_fk_user_add.setBaseSize(QSize(100, 100))
        self.btn_fk_user_add.setFont(font3)
        self.btn_fk_user_add.setLayoutDirection(Qt.LeftToRight)
        self.btn_fk_user_add.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(222, 222, 222);\n"
"    border: 2px solid #555;\n"
"    border-radius: 25px;\n"
"    border-style: outset;\n"
"	background-color: rgb(2, 50, 70);\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(40, 112, 148);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.gridLayout_17.addWidget(self.btn_fk_user_add, 0, 1, 1, 1, Qt.AlignTop)

        self.horizontalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_17.addItem(self.horizontalSpacer_10, 1, 3, 1, 1)


        self.gridLayout_2.addWidget(self.frame_fk_user_solve, 2, 0, 1, 3, Qt.AlignLeft)

        self.frame_fk_user_results = QFrame(self.tab_fk_user)
        self.frame_fk_user_results.setObjectName(u"frame_fk_user_results")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.frame_fk_user_results.sizePolicy().hasHeightForWidth())
        self.frame_fk_user_results.setSizePolicy(sizePolicy7)
        self.frame_fk_user_results.setMinimumSize(QSize(462, 285))
        self.frame_fk_user_results.setFrameShape(QFrame.StyledPanel)
        self.frame_fk_user_results.setFrameShadow(QFrame.Raised)
        self.gridLayout_16 = QGridLayout(self.frame_fk_user_results)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.label_fk_user_results = QLabel(self.frame_fk_user_results)
        self.label_fk_user_results.setObjectName(u"label_fk_user_results")
        self.label_fk_user_results.setMinimumSize(QSize(100, 50))
        self.label_fk_user_results.setMaximumSize(QSize(100, 50))
        self.label_fk_user_results.setFont(font6)
        self.label_fk_user_results.setAlignment(Qt.AlignCenter)

        self.gridLayout_16.addWidget(self.label_fk_user_results, 0, 1, 1, 1)

        self.label_fk_px = QLabel(self.frame_fk_user_results)
        self.label_fk_px.setObjectName(u"label_fk_px")
        self.label_fk_px.setMinimumSize(QSize(100, 50))
        self.label_fk_px.setMaximumSize(QSize(100, 50))
        self.label_fk_px.setFont(font6)
        self.label_fk_px.setAlignment(Qt.AlignCenter)

        self.gridLayout_16.addWidget(self.label_fk_px, 1, 0, 1, 1)

        self.label_fk_py = QLabel(self.frame_fk_user_results)
        self.label_fk_py.setObjectName(u"label_fk_py")
        self.label_fk_py.setMinimumSize(QSize(100, 50))
        self.label_fk_py.setMaximumSize(QSize(100, 50))
        self.label_fk_py.setFont(font6)
        self.label_fk_py.setAlignment(Qt.AlignCenter)

        self.gridLayout_16.addWidget(self.label_fk_py, 1, 1, 1, 1)

        self.label_fk_pz = QLabel(self.frame_fk_user_results)
        self.label_fk_pz.setObjectName(u"label_fk_pz")
        self.label_fk_pz.setMinimumSize(QSize(100, 50))
        self.label_fk_pz.setMaximumSize(QSize(100, 50))
        self.label_fk_pz.setFont(font6)
        self.label_fk_pz.setAlignment(Qt.AlignCenter)

        self.gridLayout_16.addWidget(self.label_fk_pz, 1, 2, 1, 1)

        self.lcdNumber_fk_px = QLCDNumber(self.frame_fk_user_results)
        self.lcdNumber_fk_px.setObjectName(u"lcdNumber_fk_px")
        self.lcdNumber_fk_px.setMinimumSize(QSize(100, 25))
        self.lcdNumber_fk_px.setMaximumSize(QSize(100, 25))
        self.lcdNumber_fk_px.setFrameShape(QFrame.StyledPanel)
        self.lcdNumber_fk_px.setFrameShadow(QFrame.Sunken)

        self.gridLayout_16.addWidget(self.lcdNumber_fk_px, 2, 0, 1, 1)

        self.lcdNumber_fk_py = QLCDNumber(self.frame_fk_user_results)
        self.lcdNumber_fk_py.setObjectName(u"lcdNumber_fk_py")
        self.lcdNumber_fk_py.setMinimumSize(QSize(100, 25))
        self.lcdNumber_fk_py.setMaximumSize(QSize(100, 25))
        self.lcdNumber_fk_py.setFrameShape(QFrame.StyledPanel)
        self.lcdNumber_fk_py.setFrameShadow(QFrame.Sunken)

        self.gridLayout_16.addWidget(self.lcdNumber_fk_py, 2, 1, 1, 1)

        self.lcdNumber_fk_pz = QLCDNumber(self.frame_fk_user_results)
        self.lcdNumber_fk_pz.setObjectName(u"lcdNumber_fk_pz")
        self.lcdNumber_fk_pz.setMinimumSize(QSize(100, 25))
        self.lcdNumber_fk_pz.setMaximumSize(QSize(100, 25))
        self.lcdNumber_fk_pz.setFrameShape(QFrame.StyledPanel)
        self.lcdNumber_fk_pz.setFrameShadow(QFrame.Sunken)

        self.gridLayout_16.addWidget(self.lcdNumber_fk_pz, 2, 2, 1, 1)


        self.gridLayout_2.addWidget(self.frame_fk_user_results, 0, 3, 1, 1)

        self.tabWidget_fk.addTab(self.tab_fk_user, "")

        self.gridLayout_5.addWidget(self.tabWidget_fk, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_fk)
        self.page_ik = QWidget()
        self.page_ik.setObjectName(u"page_ik")
        self.gridLayout_11 = QGridLayout(self.page_ik)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.page_ik)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_ik_input_parameters = QWidget()
        self.tab_ik_input_parameters.setObjectName(u"tab_ik_input_parameters")
        self.gridLayout_12 = QGridLayout(self.tab_ik_input_parameters)
        self.gridLayout_12.setSpacing(0)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_ik_input = QFrame(self.tab_ik_input_parameters)
        self.frame_ik_input.setObjectName(u"frame_ik_input")
        self.frame_ik_input.setMinimumSize(QSize(462, 285))
        self.frame_ik_input.setFrameShape(QFrame.StyledPanel)
        self.frame_ik_input.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_ik_input)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.btn_ik_init = QPushButton(self.frame_ik_input)
        self.btn_ik_init.setObjectName(u"btn_ik_init")
        sizePolicy4.setHeightForWidth(self.btn_ik_init.sizePolicy().hasHeightForWidth())
        self.btn_ik_init.setSizePolicy(sizePolicy4)
        self.btn_ik_init.setMinimumSize(QSize(50, 50))
        self.btn_ik_init.setMaximumSize(QSize(50, 50))
        self.btn_ik_init.setSizeIncrement(QSize(10, 10))
        self.btn_ik_init.setBaseSize(QSize(100, 100))
        self.btn_ik_init.setFont(font3)
        self.btn_ik_init.setLayoutDirection(Qt.LeftToRight)
        self.btn_ik_init.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(222, 222, 222);\n"
"    border: 2px solid #555;\n"
"    border-radius: 25px;\n"
"    border-style: outset;\n"
"	background-color: rgb(2, 50, 70);\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(40, 112, 148);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.gridLayout_6.addWidget(self.btn_ik_init, 1, 1, 1, 1)

        self.btn_ik_solve = QPushButton(self.frame_ik_input)
        self.btn_ik_solve.setObjectName(u"btn_ik_solve")
        sizePolicy4.setHeightForWidth(self.btn_ik_solve.sizePolicy().hasHeightForWidth())
        self.btn_ik_solve.setSizePolicy(sizePolicy4)
        self.btn_ik_solve.setMinimumSize(QSize(50, 50))
        self.btn_ik_solve.setMaximumSize(QSize(50, 50))
        self.btn_ik_solve.setSizeIncrement(QSize(10, 10))
        self.btn_ik_solve.setBaseSize(QSize(100, 100))
        self.btn_ik_solve.setFont(font3)
        self.btn_ik_solve.setLayoutDirection(Qt.LeftToRight)
        self.btn_ik_solve.setStyleSheet(u"QPushButton {	\n"
"	color: rgb(222, 222, 222);\n"
"    border: 2px solid #555;\n"
"    border-radius: 25px;\n"
"    border-style: outset;\n"
"	background-color: rgb(2, 50, 70);\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(40, 112, 148);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.gridLayout_6.addWidget(self.btn_ik_solve, 3, 1, 1, 1)

        self.tableWidget_ik_xyz = QTableWidget(self.frame_ik_input)
        if (self.tableWidget_ik_xyz.columnCount() < 3):
            self.tableWidget_ik_xyz.setColumnCount(3)
        __qtablewidgetitem186 = QTableWidgetItem()
        self.tableWidget_ik_xyz.setHorizontalHeaderItem(0, __qtablewidgetitem186)
        __qtablewidgetitem187 = QTableWidgetItem()
        self.tableWidget_ik_xyz.setHorizontalHeaderItem(1, __qtablewidgetitem187)
        __qtablewidgetitem188 = QTableWidgetItem()
        self.tableWidget_ik_xyz.setHorizontalHeaderItem(2, __qtablewidgetitem188)
        if (self.tableWidget_ik_xyz.rowCount() < 1):
            self.tableWidget_ik_xyz.setRowCount(1)
        __qtablewidgetitem189 = QTableWidgetItem()
        self.tableWidget_ik_xyz.setVerticalHeaderItem(0, __qtablewidgetitem189)
        __qtablewidgetitem190 = QTableWidgetItem()
        __qtablewidgetitem190.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_ik_xyz.setItem(0, 0, __qtablewidgetitem190)
        __qtablewidgetitem191 = QTableWidgetItem()
        __qtablewidgetitem191.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_ik_xyz.setItem(0, 1, __qtablewidgetitem191)
        __qtablewidgetitem192 = QTableWidgetItem()
        __qtablewidgetitem192.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_ik_xyz.setItem(0, 2, __qtablewidgetitem192)
        self.tableWidget_ik_xyz.setObjectName(u"tableWidget_ik_xyz")
        sizePolicy3.setHeightForWidth(self.tableWidget_ik_xyz.sizePolicy().hasHeightForWidth())
        self.tableWidget_ik_xyz.setSizePolicy(sizePolicy3)
        self.tableWidget_ik_xyz.setMinimumSize(QSize(386, 50))
        self.tableWidget_ik_xyz.setMaximumSize(QSize(900, 16777215))
        self.tableWidget_ik_xyz.setFrameShape(QFrame.NoFrame)
        self.tableWidget_ik_xyz.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_ik_xyz.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_ik_xyz.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget_ik_xyz.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_ik_xyz.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget_ik_xyz.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_ik_xyz.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_ik_xyz.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget_ik_xyz.verticalHeader().setDefaultSectionSize(35)
        self.tableWidget_ik_xyz.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_ik_xyz.verticalHeader().setStretchLastSection(True)

        self.gridLayout_6.addWidget(self.tableWidget_ik_xyz, 2, 0, 2, 1, Qt.AlignLeft)

        self.tableWidget_ik_input = QTableWidget(self.frame_ik_input)
        if (self.tableWidget_ik_input.columnCount() < 3):
            self.tableWidget_ik_input.setColumnCount(3)
        __qtablewidgetitem193 = QTableWidgetItem()
        self.tableWidget_ik_input.setHorizontalHeaderItem(0, __qtablewidgetitem193)
        __qtablewidgetitem194 = QTableWidgetItem()
        self.tableWidget_ik_input.setHorizontalHeaderItem(1, __qtablewidgetitem194)
        __qtablewidgetitem195 = QTableWidgetItem()
        self.tableWidget_ik_input.setHorizontalHeaderItem(2, __qtablewidgetitem195)
        if (self.tableWidget_ik_input.rowCount() < 5):
            self.tableWidget_ik_input.setRowCount(5)
        __qtablewidgetitem196 = QTableWidgetItem()
        self.tableWidget_ik_input.setVerticalHeaderItem(0, __qtablewidgetitem196)
        __qtablewidgetitem197 = QTableWidgetItem()
        self.tableWidget_ik_input.setVerticalHeaderItem(1, __qtablewidgetitem197)
        __qtablewidgetitem198 = QTableWidgetItem()
        self.tableWidget_ik_input.setVerticalHeaderItem(2, __qtablewidgetitem198)
        __qtablewidgetitem199 = QTableWidgetItem()
        self.tableWidget_ik_input.setVerticalHeaderItem(3, __qtablewidgetitem199)
        __qtablewidgetitem200 = QTableWidgetItem()
        self.tableWidget_ik_input.setVerticalHeaderItem(4, __qtablewidgetitem200)
        __qtablewidgetitem201 = QTableWidgetItem()
        __qtablewidgetitem201.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_ik_input.setItem(0, 0, __qtablewidgetitem201)
        __qtablewidgetitem202 = QTableWidgetItem()
        __qtablewidgetitem202.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_ik_input.setItem(0, 1, __qtablewidgetitem202)
        __qtablewidgetitem203 = QTableWidgetItem()
        __qtablewidgetitem203.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_ik_input.setItem(0, 2, __qtablewidgetitem203)
        __qtablewidgetitem204 = QTableWidgetItem()
        __qtablewidgetitem204.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_ik_input.setItem(1, 0, __qtablewidgetitem204)
        __qtablewidgetitem205 = QTableWidgetItem()
        __qtablewidgetitem205.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_ik_input.setItem(1, 1, __qtablewidgetitem205)
        __qtablewidgetitem206 = QTableWidgetItem()
        __qtablewidgetitem206.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_ik_input.setItem(1, 2, __qtablewidgetitem206)
        __qtablewidgetitem207 = QTableWidgetItem()
        __qtablewidgetitem207.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_ik_input.setItem(2, 0, __qtablewidgetitem207)
        __qtablewidgetitem208 = QTableWidgetItem()
        __qtablewidgetitem208.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_ik_input.setItem(2, 1, __qtablewidgetitem208)
        __qtablewidgetitem209 = QTableWidgetItem()
        __qtablewidgetitem209.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_ik_input.setItem(2, 2, __qtablewidgetitem209)
        __qtablewidgetitem210 = QTableWidgetItem()
        __qtablewidgetitem210.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_ik_input.setItem(3, 0, __qtablewidgetitem210)
        __qtablewidgetitem211 = QTableWidgetItem()
        __qtablewidgetitem211.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_ik_input.setItem(3, 1, __qtablewidgetitem211)
        __qtablewidgetitem212 = QTableWidgetItem()
        __qtablewidgetitem212.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_ik_input.setItem(3, 2, __qtablewidgetitem212)
        __qtablewidgetitem213 = QTableWidgetItem()
        __qtablewidgetitem213.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_ik_input.setItem(4, 0, __qtablewidgetitem213)
        __qtablewidgetitem214 = QTableWidgetItem()
        __qtablewidgetitem214.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_ik_input.setItem(4, 1, __qtablewidgetitem214)
        __qtablewidgetitem215 = QTableWidgetItem()
        __qtablewidgetitem215.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_ik_input.setItem(4, 2, __qtablewidgetitem215)
        self.tableWidget_ik_input.setObjectName(u"tableWidget_ik_input")
        sizePolicy3.setHeightForWidth(self.tableWidget_ik_input.sizePolicy().hasHeightForWidth())
        self.tableWidget_ik_input.setSizePolicy(sizePolicy3)
        self.tableWidget_ik_input.setMinimumSize(QSize(386, 196))
        self.tableWidget_ik_input.setMaximumSize(QSize(900, 16777215))
        self.tableWidget_ik_input.setFrameShape(QFrame.NoFrame)
        self.tableWidget_ik_input.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_ik_input.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_ik_input.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget_ik_input.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tableWidget_ik_input.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_ik_input.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget_ik_input.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget_ik_input.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_ik_input.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_ik_input.verticalHeader().setVisible(False)
        self.tableWidget_ik_input.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_ik_input.verticalHeader().setDefaultSectionSize(33)
        self.tableWidget_ik_input.verticalHeader().setHighlightSections(False)
        self.tableWidget_ik_input.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_ik_input.verticalHeader().setStretchLastSection(True)

        self.gridLayout_6.addWidget(self.tableWidget_ik_input, 0, 0, 2, 1, Qt.AlignLeft)


        self.gridLayout_12.addWidget(self.frame_ik_input, 1, 0, 1, 1)

        self.frame_ik_scheme = QFrame(self.tab_ik_input_parameters)
        self.frame_ik_scheme.setObjectName(u"frame_ik_scheme")
        self.frame_ik_scheme.setMinimumSize(QSize(462, 285))
        self.frame_ik_scheme.setFrameShape(QFrame.StyledPanel)
        self.frame_ik_scheme.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_ik_scheme)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_ik_scheme = QLabel(self.frame_ik_scheme)
        self.label_ik_scheme.setObjectName(u"label_ik_scheme")
        self.label_ik_scheme.setMinimumSize(QSize(440, 250))
        self.label_ik_scheme.setPixmap(QPixmap(u":/others/others/scheme2.png"))
        self.label_ik_scheme.setScaledContents(True)
        self.label_ik_scheme.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.label_ik_scheme)


        self.gridLayout_12.addWidget(self.frame_ik_scheme, 2, 1, 1, 1)

        self.frame_ik_info = QFrame(self.tab_ik_input_parameters)
        self.frame_ik_info.setObjectName(u"frame_ik_info")
        self.frame_ik_info.setMinimumSize(QSize(462, 285))
        self.frame_ik_info.setFrameShape(QFrame.StyledPanel)
        self.frame_ik_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_ik_info)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.textBrowser_ik = QTextBrowser(self.frame_ik_info)
        self.textBrowser_ik.setObjectName(u"textBrowser_ik")
        sizePolicy4.setHeightForWidth(self.textBrowser_ik.sizePolicy().hasHeightForWidth())
        self.textBrowser_ik.setSizePolicy(sizePolicy4)
        self.textBrowser_ik.setMinimumSize(QSize(440, 250))
        self.textBrowser_ik.setFrameShape(QFrame.NoFrame)
        self.textBrowser_ik.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textBrowser_ik.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_22.addWidget(self.textBrowser_ik)


        self.gridLayout_12.addWidget(self.frame_ik_info, 1, 1, 1, 1)

        self.frame_ik_dh = QFrame(self.tab_ik_input_parameters)
        self.frame_ik_dh.setObjectName(u"frame_ik_dh")
        self.frame_ik_dh.setMinimumSize(QSize(462, 285))
        self.frame_ik_dh.setFrameShape(QFrame.StyledPanel)
        self.frame_ik_dh.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_ik_dh)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_ik_theta1 = QLabel(self.frame_ik_dh)
        self.label_ik_theta1.setObjectName(u"label_ik_theta1")
        self.label_ik_theta1.setMinimumSize(QSize(100, 50))
        self.label_ik_theta1.setMaximumSize(QSize(100, 50))
        self.label_ik_theta1.setFont(font6)
        self.label_ik_theta1.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_ik_theta1, 1, 0, 1, 1)

        self.label_ik_theta3 = QLabel(self.frame_ik_dh)
        self.label_ik_theta3.setObjectName(u"label_ik_theta3")
        self.label_ik_theta3.setMinimumSize(QSize(100, 50))
        self.label_ik_theta3.setMaximumSize(QSize(100, 50))
        self.label_ik_theta3.setFont(font6)
        self.label_ik_theta3.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_ik_theta3, 1, 3, 1, 1)

        self.lcdNumber_ik_theta1 = QLCDNumber(self.frame_ik_dh)
        self.lcdNumber_ik_theta1.setObjectName(u"lcdNumber_ik_theta1")
        self.lcdNumber_ik_theta1.setMinimumSize(QSize(100, 25))
        self.lcdNumber_ik_theta1.setMaximumSize(QSize(100, 25))
        self.lcdNumber_ik_theta1.setFrameShape(QFrame.StyledPanel)
        self.lcdNumber_ik_theta1.setFrameShadow(QFrame.Sunken)

        self.gridLayout_10.addWidget(self.lcdNumber_ik_theta1, 2, 0, 1, 1)

        self.lcdNumber_ik_theta3 = QLCDNumber(self.frame_ik_dh)
        self.lcdNumber_ik_theta3.setObjectName(u"lcdNumber_ik_theta3")
        self.lcdNumber_ik_theta3.setMinimumSize(QSize(100, 25))
        self.lcdNumber_ik_theta3.setMaximumSize(QSize(100, 25))
        self.lcdNumber_ik_theta3.setFrameShape(QFrame.StyledPanel)
        self.lcdNumber_ik_theta3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_10.addWidget(self.lcdNumber_ik_theta3, 2, 3, 1, 1)

        self.label_ik_theta4 = QLabel(self.frame_ik_dh)
        self.label_ik_theta4.setObjectName(u"label_ik_theta4")
        self.label_ik_theta4.setMinimumSize(QSize(100, 50))
        self.label_ik_theta4.setMaximumSize(QSize(100, 50))
        self.label_ik_theta4.setFont(font6)
        self.label_ik_theta4.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_ik_theta4, 3, 3, 1, 1)

        self.label_ik_theta2 = QLabel(self.frame_ik_dh)
        self.label_ik_theta2.setObjectName(u"label_ik_theta2")
        self.label_ik_theta2.setMinimumSize(QSize(100, 50))
        self.label_ik_theta2.setMaximumSize(QSize(100, 50))
        self.label_ik_theta2.setFont(font6)
        self.label_ik_theta2.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_ik_theta2, 3, 0, 1, 1)

        self.lcdNumber_ik_theta2 = QLCDNumber(self.frame_ik_dh)
        self.lcdNumber_ik_theta2.setObjectName(u"lcdNumber_ik_theta2")
        self.lcdNumber_ik_theta2.setMinimumSize(QSize(100, 25))
        self.lcdNumber_ik_theta2.setMaximumSize(QSize(100, 25))
        self.lcdNumber_ik_theta2.setFrameShape(QFrame.StyledPanel)
        self.lcdNumber_ik_theta2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_10.addWidget(self.lcdNumber_ik_theta2, 4, 0, 1, 1)

        self.lcdNumber_ik_theta4 = QLCDNumber(self.frame_ik_dh)
        self.lcdNumber_ik_theta4.setObjectName(u"lcdNumber_ik_theta4")
        self.lcdNumber_ik_theta4.setMinimumSize(QSize(100, 25))
        self.lcdNumber_ik_theta4.setMaximumSize(QSize(100, 25))
        self.lcdNumber_ik_theta4.setFrameShape(QFrame.StyledPanel)
        self.lcdNumber_ik_theta4.setFrameShadow(QFrame.Sunken)

        self.gridLayout_10.addWidget(self.lcdNumber_ik_theta4, 4, 3, 1, 1)

        self.label_ik_results = QLabel(self.frame_ik_dh)
        self.label_ik_results.setObjectName(u"label_ik_results")
        self.label_ik_results.setMinimumSize(QSize(100, 50))
        self.label_ik_results.setMaximumSize(QSize(100, 50))
        self.label_ik_results.setFont(font6)
        self.label_ik_results.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_ik_results, 0, 2, 1, 1)


        self.gridLayout_12.addWidget(self.frame_ik_dh, 2, 0, 1, 1)

        self.tabWidget.addTab(self.tab_ik_input_parameters, "")
        self.tab_ik_extra = QWidget()
        self.tab_ik_extra.setObjectName(u"tab_ik_extra")
        self.tabWidget.addTab(self.tab_ik_extra, "")

        self.gridLayout_11.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_ik)
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.gridLayout_27 = QGridLayout(self.page_settings)
        self.gridLayout_27.setSpacing(0)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.gridLayout_27.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_2 = QTabWidget(self.page_settings)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tab_set_about = QWidget()
        self.tab_set_about.setObjectName(u"tab_set_about")
        self.gridLayout_13 = QGridLayout(self.tab_set_about)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.textBrowser = QTextBrowser(self.tab_set_about)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setFrameShape(QFrame.NoFrame)

        self.gridLayout_13.addWidget(self.textBrowser, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_set_about, "")
        self.tab_set_examp1 = QWidget()
        self.tab_set_examp1.setObjectName(u"tab_set_examp1")
        self.gridLayout_15 = QGridLayout(self.tab_set_examp1)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.label_example_1 = QLabel(self.tab_set_examp1)
        self.label_example_1.setObjectName(u"label_example_1")

        self.gridLayout_15.addWidget(self.label_example_1, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_set_examp1, "")
        self.tab_set_examp2 = QWidget()
        self.tab_set_examp2.setObjectName(u"tab_set_examp2")
        self.gridLayout_14 = QGridLayout(self.tab_set_examp2)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.label_example_2 = QLabel(self.tab_set_examp2)
        self.label_example_2.setObjectName(u"label_example_2")

        self.gridLayout_14.addWidget(self.label_example_2, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_set_examp2, "")

        self.gridLayout_27.addWidget(self.tabWidget_2, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_settings)

        self.horizontalLayout_9.addWidget(self.stackedWidget)


        self.verticalLayout_6.addWidget(self.frame_stackedWidget)

        self.frame_foot = QFrame(self.frame_screens)
        self.frame_foot.setObjectName(u"frame_foot")
        self.frame_foot.setMinimumSize(QSize(0, 30))
        self.frame_foot.setMaximumSize(QSize(16777215, 30))
        self.frame_foot.setStyleSheet(u"background-color: rgb(212, 212, 206);")
        self.frame_foot.setFrameShape(QFrame.NoFrame)
        self.frame_foot.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_foot)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.foot_label_log = QLabel(self.frame_foot)
        self.foot_label_log.setObjectName(u"foot_label_log")
        self.foot_label_log.setMinimumSize(QSize(50, 0))
        self.foot_label_log.setMaximumSize(QSize(50, 16777215))
        self.foot_label_log.setLayoutDirection(Qt.LeftToRight)
        self.foot_label_log.setFrameShadow(QFrame.Raised)
        self.foot_label_log.setLineWidth(0)
        self.foot_label_log.setPixmap(QPixmap(u":/16x16/16x16/icons8-alarms-50.png"))
        self.foot_label_log.setAlignment(Qt.AlignCenter)
        self.foot_label_log.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_3.addWidget(self.foot_label_log)

        self.Log = QTextBrowser(self.frame_foot)
        self.Log.setObjectName(u"Log")
        self.Log.setEnabled(True)
        self.Log.setMaximumSize(QSize(16777215, 20))
        self.Log.setFocusPolicy(Qt.StrongFocus)
        self.Log.setContextMenuPolicy(Qt.NoContextMenu)
        self.Log.setLayoutDirection(Qt.LeftToRight)
        self.Log.setStyleSheet(u"")
        self.Log.setInputMethodHints(Qt.ImhMultiLine)
        self.Log.setFrameShape(QFrame.NoFrame)
        self.Log.setFrameShadow(QFrame.Plain)
        self.Log.setLineWidth(0)
        self.Log.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.Log.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Log.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.Log.setAutoFormatting(QTextEdit.AutoAll)
        self.Log.setLineWrapMode(QTextEdit.NoWrap)
        self.Log.setOverwriteMode(False)
        self.Log.setTabStopWidth(0)
        self.Log.setAcceptRichText(True)
        self.Log.setCursorWidth(0)
        self.Log.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.Log.setOpenLinks(False)

        self.horizontalLayout_3.addWidget(self.Log, 0, Qt.AlignVCenter)

        self.foot_label_ver = QLabel(self.frame_foot)
        self.foot_label_ver.setObjectName(u"foot_label_ver")
        self.foot_label_ver.setMinimumSize(QSize(50, 0))
        self.foot_label_ver.setMaximumSize(QSize(50, 16777215))
        self.foot_label_ver.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.foot_label_ver)

        self.frame_grip = QFrame(self.frame_foot)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(25, 25))
        self.frame_grip.setMaximumSize(QSize(25, 16777215))
        self.frame_grip.setFrameShape(QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_grip)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 5, 0)
        self.label_foot_grip = QLabel(self.frame_grip)
        self.label_foot_grip.setObjectName(u"label_foot_grip")
        self.label_foot_grip.setMinimumSize(QSize(0, 0))
        self.label_foot_grip.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_foot_grip)


        self.horizontalLayout_3.addWidget(self.frame_grip)


        self.verticalLayout_6.addWidget(self.frame_foot)


        self.horizontalLayout_2.addWidget(self.frame_screens)


        self.verticalLayout.addWidget(self.frame_content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)
        self.tabWidget_fk.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.centralwidget.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.btn_lista.setText("")
        self.label_name.setText(QCoreApplication.translate("MainWindow", u"KinematicsSolverApp", None))
#if QT_CONFIG(tooltip)
        self.btn_min.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_min.setText("")
#if QT_CONFIG(tooltip)
        self.btn_max.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_max.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.label_top_info_2.setText(QCoreApplication.translate("MainWindow", u"| HOME", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.btn_fk.setText(QCoreApplication.translate("MainWindow", u"FORWARD KINEMATICS", None))
        self.btn_ik.setText(QCoreApplication.translate("MainWindow", u"INVERSE KINEMATICS", None))
        self.btn_settings.setText(QCoreApplication.translate("MainWindow", u"SETTINGS", None))
        self.btn_home_FK.setText(QCoreApplication.translate("MainWindow", u"Forward kin.", None))
        self.btn_home_IK.setText(QCoreApplication.translate("MainWindow", u"Inverse kin.", None))
        self.btn_home_settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"FORWARD AND INVERSE KINEMATICS SOLVER", None))
        self.label_2.setText("")
        self.btn_fk_init.setText(QCoreApplication.translate("MainWindow", u"Init", None))
        self.btn_fk_solve.setText(QCoreApplication.translate("MainWindow", u"Solve", None))
        ___qtablewidgetitem = self.tableWidget_fk_theta.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Theta1", None));
        ___qtablewidgetitem1 = self.tableWidget_fk_theta.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Theta2", None));
        ___qtablewidgetitem2 = self.tableWidget_fk_theta.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Theta3", None));
        ___qtablewidgetitem3 = self.tableWidget_fk_theta.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Theta4", None));
        ___qtablewidgetitem4 = self.tableWidget_fk_theta.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"1", None));

        __sortingEnabled = self.tableWidget_fk_theta.isSortingEnabled()
        self.tableWidget_fk_theta.setSortingEnabled(False)
        ___qtablewidgetitem5 = self.tableWidget_fk_theta.item(0, 0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"0.0", None));
        ___qtablewidgetitem6 = self.tableWidget_fk_theta.item(0, 1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"90.0", None));
        ___qtablewidgetitem7 = self.tableWidget_fk_theta.item(0, 2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"0.0", None));
        ___qtablewidgetitem8 = self.tableWidget_fk_theta.item(0, 3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"0.0", None));
        self.tableWidget_fk_theta.setSortingEnabled(__sortingEnabled)

        ___qtablewidgetitem9 = self.tableWidget_fk_unput.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"L", None));
        ___qtablewidgetitem10 = self.tableWidget_fk_unput.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"R-", None));
        ___qtablewidgetitem11 = self.tableWidget_fk_unput.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"R+", None));
        ___qtablewidgetitem12 = self.tableWidget_fk_unput.verticalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"L1", None));
        ___qtablewidgetitem13 = self.tableWidget_fk_unput.verticalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"L2", None));
        ___qtablewidgetitem14 = self.tableWidget_fk_unput.verticalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"L3", None));
        ___qtablewidgetitem15 = self.tableWidget_fk_unput.verticalHeaderItem(3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"L4", None));
        ___qtablewidgetitem16 = self.tableWidget_fk_unput.verticalHeaderItem(4)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"L5", None));

        __sortingEnabled1 = self.tableWidget_fk_unput.isSortingEnabled()
        self.tableWidget_fk_unput.setSortingEnabled(False)
        ___qtablewidgetitem17 = self.tableWidget_fk_unput.item(0, 0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"118", None));
        ___qtablewidgetitem18 = self.tableWidget_fk_unput.item(0, 1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"-80", None));
        ___qtablewidgetitem19 = self.tableWidget_fk_unput.item(0, 2)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"80", None));
        ___qtablewidgetitem20 = self.tableWidget_fk_unput.item(1, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"150", None));
        ___qtablewidgetitem21 = self.tableWidget_fk_unput.item(1, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem22 = self.tableWidget_fk_unput.item(1, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"175", None));
        ___qtablewidgetitem23 = self.tableWidget_fk_unput.item(2, 0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"150", None));
        ___qtablewidgetitem24 = self.tableWidget_fk_unput.item(2, 1)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"-115", None));
        ___qtablewidgetitem25 = self.tableWidget_fk_unput.item(2, 2)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"55", None));
        ___qtablewidgetitem26 = self.tableWidget_fk_unput.item(3, 0)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"54", None));
        ___qtablewidgetitem27 = self.tableWidget_fk_unput.item(3, 1)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"-85", None));
        ___qtablewidgetitem28 = self.tableWidget_fk_unput.item(3, 2)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"85", None));
        ___qtablewidgetitem29 = self.tableWidget_fk_unput.item(4, 0)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem30 = self.tableWidget_fk_unput.item(4, 1)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem31 = self.tableWidget_fk_unput.item(4, 2)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"0", None));
        self.tableWidget_fk_unput.setSortingEnabled(__sortingEnabled1)

        self.textBrowser_fk.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Robotics arm input parameters:</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">L1 - link1 - base height, length, range min, range max	</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">L2 - link2 - arm1, length, range mi"
                        "n, range max	</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">L3 - link3 - arm2, length, range min, range max	</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">L4 - link4 - effector L, length, range min, range max	</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">L5 - link5 - effector H, length, range min, range max	</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p></body></html>", None))
        self.label_fk_scheme.setText("")
        ___qtablewidgetitem32 = self.tableWidget_fk_dh.horizontalHeaderItem(0)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"\u03b8", None));
        ___qtablewidgetitem33 = self.tableWidget_fk_dh.horizontalHeaderItem(1)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"d", None));
        ___qtablewidgetitem34 = self.tableWidget_fk_dh.horizontalHeaderItem(2)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"a", None));
        ___qtablewidgetitem35 = self.tableWidget_fk_dh.horizontalHeaderItem(3)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"\u03b1", None));
        ___qtablewidgetitem36 = self.tableWidget_fk_dh.verticalHeaderItem(0)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem37 = self.tableWidget_fk_dh.verticalHeaderItem(1)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem38 = self.tableWidget_fk_dh.verticalHeaderItem(2)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem39 = self.tableWidget_fk_dh.verticalHeaderItem(3)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem40 = self.tableWidget_fk_dh.verticalHeaderItem(4)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"5", None));

        __sortingEnabled2 = self.tableWidget_fk_dh.isSortingEnabled()
        self.tableWidget_fk_dh.setSortingEnabled(False)
        ___qtablewidgetitem41 = self.tableWidget_fk_dh.item(0, 0)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem42 = self.tableWidget_fk_dh.item(0, 1)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem43 = self.tableWidget_fk_dh.item(0, 2)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem44 = self.tableWidget_fk_dh.item(0, 3)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem45 = self.tableWidget_fk_dh.item(1, 0)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem46 = self.tableWidget_fk_dh.item(1, 1)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem47 = self.tableWidget_fk_dh.item(1, 2)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem48 = self.tableWidget_fk_dh.item(1, 3)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem49 = self.tableWidget_fk_dh.item(2, 0)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem50 = self.tableWidget_fk_dh.item(2, 1)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem51 = self.tableWidget_fk_dh.item(2, 2)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem52 = self.tableWidget_fk_dh.item(2, 3)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem53 = self.tableWidget_fk_dh.item(3, 0)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem54 = self.tableWidget_fk_dh.item(3, 1)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem55 = self.tableWidget_fk_dh.item(3, 2)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem56 = self.tableWidget_fk_dh.item(3, 3)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem57 = self.tableWidget_fk_dh.item(4, 0)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem58 = self.tableWidget_fk_dh.item(4, 1)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem59 = self.tableWidget_fk_dh.item(4, 2)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem60 = self.tableWidget_fk_dh.item(4, 3)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"0", None));
        self.tableWidget_fk_dh.setSortingEnabled(__sortingEnabled2)

        self.label_fk_dh.setText(QCoreApplication.translate("MainWindow", u"Denavit - Hartenberg table", None))
        self.tabWidget_fk.setTabText(self.tabWidget_fk.indexOf(self.tab_fk_input_parameters), QCoreApplication.translate("MainWindow", u"Input / Solve", None))
        self.label_T12.setText(QCoreApplication.translate("MainWindow", u"T1-2", None))
        self.label_T14.setText(QCoreApplication.translate("MainWindow", u"T1-4", None))

        __sortingEnabled3 = self.tableWidget_fk_T12.isSortingEnabled()
        self.tableWidget_fk_T12.setSortingEnabled(False)
        ___qtablewidgetitem61 = self.tableWidget_fk_T12.item(0, 0)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem62 = self.tableWidget_fk_T12.item(0, 1)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem63 = self.tableWidget_fk_T12.item(0, 2)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem64 = self.tableWidget_fk_T12.item(0, 3)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem65 = self.tableWidget_fk_T12.item(1, 0)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem66 = self.tableWidget_fk_T12.item(1, 1)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem67 = self.tableWidget_fk_T12.item(1, 2)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem68 = self.tableWidget_fk_T12.item(1, 3)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem69 = self.tableWidget_fk_T12.item(2, 0)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem70 = self.tableWidget_fk_T12.item(2, 1)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem71 = self.tableWidget_fk_T12.item(2, 2)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem72 = self.tableWidget_fk_T12.item(2, 3)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem73 = self.tableWidget_fk_T12.item(3, 0)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem74 = self.tableWidget_fk_T12.item(3, 1)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem75 = self.tableWidget_fk_T12.item(3, 2)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem76 = self.tableWidget_fk_T12.item(3, 3)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("MainWindow", u"0", None));
        self.tableWidget_fk_T12.setSortingEnabled(__sortingEnabled3)


        __sortingEnabled4 = self.tableWidget_fk_T14.isSortingEnabled()
        self.tableWidget_fk_T14.setSortingEnabled(False)
        ___qtablewidgetitem77 = self.tableWidget_fk_T14.item(0, 0)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem78 = self.tableWidget_fk_T14.item(0, 1)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem79 = self.tableWidget_fk_T14.item(0, 2)
        ___qtablewidgetitem79.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem80 = self.tableWidget_fk_T14.item(0, 3)
        ___qtablewidgetitem80.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem81 = self.tableWidget_fk_T14.item(1, 0)
        ___qtablewidgetitem81.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem82 = self.tableWidget_fk_T14.item(1, 1)
        ___qtablewidgetitem82.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem83 = self.tableWidget_fk_T14.item(1, 2)
        ___qtablewidgetitem83.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem84 = self.tableWidget_fk_T14.item(1, 3)
        ___qtablewidgetitem84.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem85 = self.tableWidget_fk_T14.item(2, 0)
        ___qtablewidgetitem85.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem86 = self.tableWidget_fk_T14.item(2, 1)
        ___qtablewidgetitem86.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem87 = self.tableWidget_fk_T14.item(2, 2)
        ___qtablewidgetitem87.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem88 = self.tableWidget_fk_T14.item(2, 3)
        ___qtablewidgetitem88.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem89 = self.tableWidget_fk_T14.item(3, 0)
        ___qtablewidgetitem89.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem90 = self.tableWidget_fk_T14.item(3, 1)
        ___qtablewidgetitem90.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem91 = self.tableWidget_fk_T14.item(3, 2)
        ___qtablewidgetitem91.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem92 = self.tableWidget_fk_T14.item(3, 3)
        ___qtablewidgetitem92.setText(QCoreApplication.translate("MainWindow", u"0", None));
        self.tableWidget_fk_T14.setSortingEnabled(__sortingEnabled4)

        self.label_T13.setText(QCoreApplication.translate("MainWindow", u"T1-3", None))
        self.label_T15.setText(QCoreApplication.translate("MainWindow", u"T1-5", None))

        __sortingEnabled5 = self.tableWidget_fk_T13.isSortingEnabled()
        self.tableWidget_fk_T13.setSortingEnabled(False)
        ___qtablewidgetitem93 = self.tableWidget_fk_T13.item(0, 0)
        ___qtablewidgetitem93.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem94 = self.tableWidget_fk_T13.item(0, 1)
        ___qtablewidgetitem94.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem95 = self.tableWidget_fk_T13.item(0, 2)
        ___qtablewidgetitem95.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem96 = self.tableWidget_fk_T13.item(0, 3)
        ___qtablewidgetitem96.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem97 = self.tableWidget_fk_T13.item(1, 0)
        ___qtablewidgetitem97.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem98 = self.tableWidget_fk_T13.item(1, 1)
        ___qtablewidgetitem98.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem99 = self.tableWidget_fk_T13.item(1, 2)
        ___qtablewidgetitem99.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem100 = self.tableWidget_fk_T13.item(1, 3)
        ___qtablewidgetitem100.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem101 = self.tableWidget_fk_T13.item(2, 0)
        ___qtablewidgetitem101.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem102 = self.tableWidget_fk_T13.item(2, 1)
        ___qtablewidgetitem102.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem103 = self.tableWidget_fk_T13.item(2, 2)
        ___qtablewidgetitem103.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem104 = self.tableWidget_fk_T13.item(2, 3)
        ___qtablewidgetitem104.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem105 = self.tableWidget_fk_T13.item(3, 0)
        ___qtablewidgetitem105.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem106 = self.tableWidget_fk_T13.item(3, 1)
        ___qtablewidgetitem106.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem107 = self.tableWidget_fk_T13.item(3, 2)
        ___qtablewidgetitem107.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem108 = self.tableWidget_fk_T13.item(3, 3)
        ___qtablewidgetitem108.setText(QCoreApplication.translate("MainWindow", u"0", None));
        self.tableWidget_fk_T13.setSortingEnabled(__sortingEnabled5)


        __sortingEnabled6 = self.tableWidget_fk_T15.isSortingEnabled()
        self.tableWidget_fk_T15.setSortingEnabled(False)
        ___qtablewidgetitem109 = self.tableWidget_fk_T15.item(0, 0)
        ___qtablewidgetitem109.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem110 = self.tableWidget_fk_T15.item(0, 1)
        ___qtablewidgetitem110.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem111 = self.tableWidget_fk_T15.item(0, 2)
        ___qtablewidgetitem111.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem112 = self.tableWidget_fk_T15.item(0, 3)
        ___qtablewidgetitem112.setText(QCoreApplication.translate("MainWindow", u"0", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem112.setToolTip(QCoreApplication.translate("MainWindow", u"Px", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem113 = self.tableWidget_fk_T15.item(1, 0)
        ___qtablewidgetitem113.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem114 = self.tableWidget_fk_T15.item(1, 1)
        ___qtablewidgetitem114.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem115 = self.tableWidget_fk_T15.item(1, 2)
        ___qtablewidgetitem115.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem116 = self.tableWidget_fk_T15.item(1, 3)
        ___qtablewidgetitem116.setText(QCoreApplication.translate("MainWindow", u"0", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem116.setToolTip(QCoreApplication.translate("MainWindow", u"Py", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem117 = self.tableWidget_fk_T15.item(2, 0)
        ___qtablewidgetitem117.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem118 = self.tableWidget_fk_T15.item(2, 1)
        ___qtablewidgetitem118.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem119 = self.tableWidget_fk_T15.item(2, 2)
        ___qtablewidgetitem119.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem120 = self.tableWidget_fk_T15.item(2, 3)
        ___qtablewidgetitem120.setText(QCoreApplication.translate("MainWindow", u"0", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem120.setToolTip(QCoreApplication.translate("MainWindow", u"Pz", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem121 = self.tableWidget_fk_T15.item(3, 0)
        ___qtablewidgetitem121.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem122 = self.tableWidget_fk_T15.item(3, 1)
        ___qtablewidgetitem122.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem123 = self.tableWidget_fk_T15.item(3, 2)
        ___qtablewidgetitem123.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem124 = self.tableWidget_fk_T15.item(3, 3)
        ___qtablewidgetitem124.setText(QCoreApplication.translate("MainWindow", u"0", None));
        self.tableWidget_fk_T15.setSortingEnabled(__sortingEnabled6)

        self.tabWidget_fk.setTabText(self.tabWidget_fk.indexOf(self.tab_fk_hom_matrices), QCoreApplication.translate("MainWindow", u"Homogenious matrices", None))
        ___qtablewidgetitem125 = self.tableWidget_8.horizontalHeaderItem(0)
        ___qtablewidgetitem125.setText(QCoreApplication.translate("MainWindow", u"\u03b8", None));
        ___qtablewidgetitem126 = self.tableWidget_8.horizontalHeaderItem(1)
        ___qtablewidgetitem126.setText(QCoreApplication.translate("MainWindow", u"d", None));
        ___qtablewidgetitem127 = self.tableWidget_8.horizontalHeaderItem(2)
        ___qtablewidgetitem127.setText(QCoreApplication.translate("MainWindow", u"a", None));
        ___qtablewidgetitem128 = self.tableWidget_8.horizontalHeaderItem(3)
        ___qtablewidgetitem128.setText(QCoreApplication.translate("MainWindow", u"\u03b1", None));
        ___qtablewidgetitem129 = self.tableWidget_8.verticalHeaderItem(0)
        ___qtablewidgetitem129.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem130 = self.tableWidget_8.verticalHeaderItem(1)
        ___qtablewidgetitem130.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem131 = self.tableWidget_8.verticalHeaderItem(2)
        ___qtablewidgetitem131.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem132 = self.tableWidget_8.verticalHeaderItem(3)
        ___qtablewidgetitem132.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem133 = self.tableWidget_8.verticalHeaderItem(4)
        ___qtablewidgetitem133.setText(QCoreApplication.translate("MainWindow", u"5", None));

        __sortingEnabled7 = self.tableWidget_8.isSortingEnabled()
        self.tableWidget_8.setSortingEnabled(False)
        ___qtablewidgetitem134 = self.tableWidget_8.item(0, 0)
        ___qtablewidgetitem134.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem135 = self.tableWidget_8.item(0, 1)
        ___qtablewidgetitem135.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem136 = self.tableWidget_8.item(0, 2)
        ___qtablewidgetitem136.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem137 = self.tableWidget_8.item(0, 3)
        ___qtablewidgetitem137.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem138 = self.tableWidget_8.item(1, 0)
        ___qtablewidgetitem138.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem139 = self.tableWidget_8.item(1, 1)
        ___qtablewidgetitem139.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem140 = self.tableWidget_8.item(1, 2)
        ___qtablewidgetitem140.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem141 = self.tableWidget_8.item(1, 3)
        ___qtablewidgetitem141.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem142 = self.tableWidget_8.item(2, 0)
        ___qtablewidgetitem142.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem143 = self.tableWidget_8.item(2, 1)
        ___qtablewidgetitem143.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem144 = self.tableWidget_8.item(2, 2)
        ___qtablewidgetitem144.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem145 = self.tableWidget_8.item(2, 3)
        ___qtablewidgetitem145.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem146 = self.tableWidget_8.item(3, 0)
        ___qtablewidgetitem146.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem147 = self.tableWidget_8.item(3, 1)
        ___qtablewidgetitem147.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem148 = self.tableWidget_8.item(3, 2)
        ___qtablewidgetitem148.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem149 = self.tableWidget_8.item(3, 3)
        ___qtablewidgetitem149.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem150 = self.tableWidget_8.item(4, 0)
        ___qtablewidgetitem150.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem151 = self.tableWidget_8.item(4, 1)
        ___qtablewidgetitem151.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem152 = self.tableWidget_8.item(4, 2)
        ___qtablewidgetitem152.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem153 = self.tableWidget_8.item(4, 3)
        ___qtablewidgetitem153.setText(QCoreApplication.translate("MainWindow", u"0", None));
        self.tableWidget_8.setSortingEnabled(__sortingEnabled7)

        self.btn_fk_user_solve.setText(QCoreApplication.translate("MainWindow", u"Solve", None))
        self.btn_fk_user_sub.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.btn_fk_user_add.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label_fk_user_results.setText(QCoreApplication.translate("MainWindow", u"Results", None))
        self.label_fk_px.setText(QCoreApplication.translate("MainWindow", u"Px", None))
        self.label_fk_py.setText(QCoreApplication.translate("MainWindow", u"Py", None))
        self.label_fk_pz.setText(QCoreApplication.translate("MainWindow", u"Pz", None))
        self.tabWidget_fk.setTabText(self.tabWidget_fk.indexOf(self.tab_fk_user), QCoreApplication.translate("MainWindow", u"User", None))
        self.btn_ik_init.setText(QCoreApplication.translate("MainWindow", u"Init", None))
        self.btn_ik_solve.setText(QCoreApplication.translate("MainWindow", u"Solve", None))
        ___qtablewidgetitem154 = self.tableWidget_ik_xyz.horizontalHeaderItem(0)
        ___qtablewidgetitem154.setText(QCoreApplication.translate("MainWindow", u"Px", None));
        ___qtablewidgetitem155 = self.tableWidget_ik_xyz.horizontalHeaderItem(1)
        ___qtablewidgetitem155.setText(QCoreApplication.translate("MainWindow", u"Py", None));
        ___qtablewidgetitem156 = self.tableWidget_ik_xyz.horizontalHeaderItem(2)
        ___qtablewidgetitem156.setText(QCoreApplication.translate("MainWindow", u"Pz", None));
        ___qtablewidgetitem157 = self.tableWidget_ik_xyz.verticalHeaderItem(0)
        ___qtablewidgetitem157.setText(QCoreApplication.translate("MainWindow", u"1", None));

        __sortingEnabled8 = self.tableWidget_ik_xyz.isSortingEnabled()
        self.tableWidget_ik_xyz.setSortingEnabled(False)
        ___qtablewidgetitem158 = self.tableWidget_ik_xyz.item(0, 0)
        ___qtablewidgetitem158.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem159 = self.tableWidget_ik_xyz.item(0, 1)
        ___qtablewidgetitem159.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem160 = self.tableWidget_ik_xyz.item(0, 2)
        ___qtablewidgetitem160.setText(QCoreApplication.translate("MainWindow", u"472", None));
        self.tableWidget_ik_xyz.setSortingEnabled(__sortingEnabled8)

        ___qtablewidgetitem161 = self.tableWidget_ik_input.horizontalHeaderItem(0)
        ___qtablewidgetitem161.setText(QCoreApplication.translate("MainWindow", u"L", None));
        ___qtablewidgetitem162 = self.tableWidget_ik_input.horizontalHeaderItem(1)
        ___qtablewidgetitem162.setText(QCoreApplication.translate("MainWindow", u"R-", None));
        ___qtablewidgetitem163 = self.tableWidget_ik_input.horizontalHeaderItem(2)
        ___qtablewidgetitem163.setText(QCoreApplication.translate("MainWindow", u"R+", None));
        ___qtablewidgetitem164 = self.tableWidget_ik_input.verticalHeaderItem(0)
        ___qtablewidgetitem164.setText(QCoreApplication.translate("MainWindow", u"L1", None));
        ___qtablewidgetitem165 = self.tableWidget_ik_input.verticalHeaderItem(1)
        ___qtablewidgetitem165.setText(QCoreApplication.translate("MainWindow", u"L2", None));
        ___qtablewidgetitem166 = self.tableWidget_ik_input.verticalHeaderItem(2)
        ___qtablewidgetitem166.setText(QCoreApplication.translate("MainWindow", u"L3", None));
        ___qtablewidgetitem167 = self.tableWidget_ik_input.verticalHeaderItem(3)
        ___qtablewidgetitem167.setText(QCoreApplication.translate("MainWindow", u"L4", None));
        ___qtablewidgetitem168 = self.tableWidget_ik_input.verticalHeaderItem(4)
        ___qtablewidgetitem168.setText(QCoreApplication.translate("MainWindow", u"L5", None));

        __sortingEnabled9 = self.tableWidget_ik_input.isSortingEnabled()
        self.tableWidget_ik_input.setSortingEnabled(False)
        ___qtablewidgetitem169 = self.tableWidget_ik_input.item(0, 0)
        ___qtablewidgetitem169.setText(QCoreApplication.translate("MainWindow", u"118", None));
        ___qtablewidgetitem170 = self.tableWidget_ik_input.item(0, 1)
        ___qtablewidgetitem170.setText(QCoreApplication.translate("MainWindow", u"-80", None));
        ___qtablewidgetitem171 = self.tableWidget_ik_input.item(0, 2)
        ___qtablewidgetitem171.setText(QCoreApplication.translate("MainWindow", u"80", None));
        ___qtablewidgetitem172 = self.tableWidget_ik_input.item(1, 0)
        ___qtablewidgetitem172.setText(QCoreApplication.translate("MainWindow", u"150", None));
        ___qtablewidgetitem173 = self.tableWidget_ik_input.item(1, 1)
        ___qtablewidgetitem173.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem174 = self.tableWidget_ik_input.item(1, 2)
        ___qtablewidgetitem174.setText(QCoreApplication.translate("MainWindow", u"175", None));
        ___qtablewidgetitem175 = self.tableWidget_ik_input.item(2, 0)
        ___qtablewidgetitem175.setText(QCoreApplication.translate("MainWindow", u"150", None));
        ___qtablewidgetitem176 = self.tableWidget_ik_input.item(2, 1)
        ___qtablewidgetitem176.setText(QCoreApplication.translate("MainWindow", u"-115", None));
        ___qtablewidgetitem177 = self.tableWidget_ik_input.item(2, 2)
        ___qtablewidgetitem177.setText(QCoreApplication.translate("MainWindow", u"55", None));
        ___qtablewidgetitem178 = self.tableWidget_ik_input.item(3, 0)
        ___qtablewidgetitem178.setText(QCoreApplication.translate("MainWindow", u"54", None));
        ___qtablewidgetitem179 = self.tableWidget_ik_input.item(3, 1)
        ___qtablewidgetitem179.setText(QCoreApplication.translate("MainWindow", u"-85", None));
        ___qtablewidgetitem180 = self.tableWidget_ik_input.item(3, 2)
        ___qtablewidgetitem180.setText(QCoreApplication.translate("MainWindow", u"85", None));
        ___qtablewidgetitem181 = self.tableWidget_ik_input.item(4, 0)
        ___qtablewidgetitem181.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem182 = self.tableWidget_ik_input.item(4, 1)
        ___qtablewidgetitem182.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem183 = self.tableWidget_ik_input.item(4, 2)
        ___qtablewidgetitem183.setText(QCoreApplication.translate("MainWindow", u"0", None));
        self.tableWidget_ik_input.setSortingEnabled(__sortingEnabled9)

        self.label_ik_scheme.setText("")
        self.textBrowser_ik.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Robotics arm input parameters:</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">L1 - link1 - base height, length, range min, range max	</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">L2 - link2 - arm1, length, range mi"
                        "n, range max	</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">L3 - link3 - arm2, length, range min, range max	</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">L4 - link4 - effector L, length, range min, range max	</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">L5 - link5 - effector H, length, range min, range max	</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -q"
                        "t-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">(L4,L5 - effector)</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">2 arm with effector - no empty</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">1 arm with effector - L3 input 0</span></p></body></html>", None))
        self.label_ik_theta1.setText(QCoreApplication.translate("MainWindow", u"Theta1", None))
        self.label_ik_theta3.setText(QCoreApplication.translate("MainWindow", u"Theta3", None))
        self.label_ik_theta4.setText(QCoreApplication.translate("MainWindow", u"Theta4", None))
        self.label_ik_theta2.setText(QCoreApplication.translate("MainWindow", u"Theta2", None))
        self.label_ik_results.setText(QCoreApplication.translate("MainWindow", u"Results", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_ik_input_parameters), QCoreApplication.translate("MainWindow", u"Input / Solve", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_ik_extra), QCoreApplication.translate("MainWindow", u"Extra", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">About project</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">App allows to calculate forward and inverse kinematics of robotic arm with:<br />1 arm + effector and 2 arm + effector</span></p>\n"
""
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">To calculate forward kinematics Denavit-hartenberg table is being used. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">App alows to init robotic arm with specified parameters and the solve the kinematics. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">App allows user to also unput prepared dh table and the also do the calculetions.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-rig"
                        "ht:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">To calculate inverse kinematics geometrical method is being used. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">App allows to to init robotic arm with specified parameters aand then solve the kinematics.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p></body></html>", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_set_about), QCoreApplication.translate("MainWindow", u"About", None))
        self.label_example_1.setText("")
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_set_examp1), QCoreApplication.translate("MainWindow", u"Example 1", None))
        self.label_example_2.setText("")
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_set_examp2), QCoreApplication.translate("MainWindow", u"Example 2", None))
        self.foot_label_log.setText("")
        self.Log.setDocumentTitle("")
        self.Log.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Time | Log</span></p></body></html>", None))
        self.Log.setPlaceholderText("")
        self.foot_label_ver.setText(QCoreApplication.translate("MainWindow", u"ver. 1.0", None))
        self.label_foot_grip.setText(QCoreApplication.translate("MainWindow", u".:", None))
    # retranslateUi

