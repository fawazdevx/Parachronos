# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screenLxsiQj.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(680, 400)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        self.dropShadowFrame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(56, 58, 89);	\n"
"	color: rgb(220, 220, 220);\n"
"	border-radius:10px;\n"
"}")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.dropShadowFrame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.dropShadowFrame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.appName = QLabel(self.frame)
        self.appName.setObjectName(u"appName")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.appName.setFont(font)
        self.appName.setStyleSheet(u"color: rgb(255, 0, 127);")
        self.appName.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.appName)

        self.description = QLabel(self.frame)
        self.description.setObjectName(u"description")
        font1 = QFont()
        font1.setFamily(u"Segoe Print")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.description.setFont(font1)
        self.description.setStyleSheet(u"color: rgb(255, 0, 127);")
        self.description.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.description, 0, Qt.AlignBottom)


        self.verticalLayout_5.addWidget(self.frame)

        self.frame_3 = QFrame(self.dropShadowFrame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 0))
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(255, 0, 127);")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)


        self.verticalLayout_5.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.dropShadowFrame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, -1, 0, 0)
        self.Author = QLabel(self.frame_2)
        self.Author.setObjectName(u"Author")
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.Author.setFont(font2)
        self.Author.setStyleSheet(u"color: rgb(85, 85, 127);")
        self.Author.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.Author, 0, Qt.AlignBottom)

        self.progressBar = QProgressBar(self.frame_2)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(0, 10))
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"	color: rgb(255, 0, 127);\n"
"	background-color: rgb(53, 28, 117);\n"
"	text-align:center;\n"
"	border-radius:10px;\n"
"	border-style:none;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius:10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.472, x2:0.982955, y2:0.517, stop:0 rgba(255, 0, 127, 255), stop:1 rgba(53, 28, 117, 255));\n"
"}")
        self.progressBar.setValue(24)

        self.verticalLayout_3.addWidget(self.progressBar)


        self.verticalLayout_5.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.dropShadowFrame)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.appName.setText(QCoreApplication.translate("SplashScreen", u"<p align=\"left\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:30pt; font-weight:600; color:#ee208b;\">Parachronos</span></p>\n"
"<p align=\"leftr\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','monospace'; font-size:9.8pt; color:#c9c9d1;\">Unleashing the Polkadot Potential</span></p>", None))
        self.description.setText(QCoreApplication.translate("SplashScreen", u"<strong>Welcome</strong> to Parachronos", None))
        self.label.setText("")
        self.Author.setText(QCoreApplication.translate("SplashScreen", u"<p align=\"right\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-weight:600; color:#bd93f9;\">Created by: Fawaz H. Oyebode</span></p>", None))
    # retranslateUi

