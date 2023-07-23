# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface_PKDZtPef.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomSlideMenu
from Custom_Widgets.Widgets import QCustomStackedWidget
from PySide2extn.RoundProgressBar import roundProgressBar

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.ApplicationModal)
        MainWindow.resize(956, 700)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(940, 560))
        MainWindow.setStyleSheet(u"*{\n"
"    border:none;\n"
"    background-color:transparent;\n"
"    background:transparent;\n"
"    padding:0;\n"
"    margin:0;\n"
"    color:#fff;\n"
"}\n"
"#centralwidget{\n"
"    background-color:#1f232a;\n"
"}\n"
"#leftMenuSubContainer{\n"
"    background-color: #351c75;\n"
"}\n"
"#leftMenuSubContainer QPushButton{\n"
"   text-align:left;\n"
"   padding: 5px 10px;\n"
"   border-top-left-radius: 10px;\n"
"   border-bottom-left-radius: 10px;\n"
"}\n"
"#centerMenuSubContainer,#rightMenuSubContainer{\n"
"    background-color:#2c313c;\n"
"}\n"
"#QLineEdit{\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"#QLineEdit:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"#QLineEdit:focus{\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"#frame_4,#frame_8,#popupNotificationSubContainer, #quickLinksSubContainer{\n"
"	backgro"
                        "und-color:#351c75;\n"
"	border-radius: 10px;\n"
"}\n"
"#headerContainer,#footerContainer{\n"
"	background-color:#351c75;\n"
"}\n"
"#bottomBar {\n"
"	 background-color: rgb(44, 49, 58);\n"
"}\n"
"#bottomBar QLabel { \n"
"	font-size: 11px; color: rgb(113, 126, 149);\n"
"     padding-left: 10px;\n"
" 	padding-right: 10px;\n"
" 	padding-	bottom: 2px;\n"
"}\n"
"#extraCenter, #frame_62{\n"
"	border-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"#settingsMenu .QPushButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#settingsMenu QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#settingsMenu QPushButton:pressed {	\n"
"	background-color: rgb(255, 0, 127);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#cpu_cores_label .QLabel{\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	sele"
                        "ction-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"#popupNotificationSubContainer{\n"
"	background-color:#351c7;\n"
"	border-radius: 10px;\n"
"}\n"
"#frame_47 QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"	border-radius: 10px;\n"
"}\n"
"#frame_47 QPushButton:pressed {	\n"
"	background-color:#351c75;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius:10px;\n"
"}\n"
"#quickLinksSubContainer QPushButton:hover{\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#quickLinksSubContainer QPushButton:pressed {	\n"
"	background-color: rgb(255, 0, 127);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        self.leftMenuContainer.setMaximumSize(QSize(50, 16777215))
        self.leftMenuContainer.setStyleSheet(u"#centralwidget{\n"
"   background-color:#351c75;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuSubContainer = QWidget(self.leftMenuContainer)
        self.leftMenuSubContainer.setObjectName(u"leftMenuSubContainer")
        self.verticalLayout_2 = QVBoxLayout(self.leftMenuSubContainer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.frame = QFrame(self.leftMenuSubContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menuBtn = QPushButton(self.frame)
        self.menuBtn.setObjectName(u"menuBtn")
        icon = QIcon()
        icon.addFile(u":/icons/icons/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.menuBtn)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.leftMenuSubContainer)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 10)
        self.homeBtn = QPushButton(self.frame_2)
        self.homeBtn.setObjectName(u"homeBtn")
        font = QFont()
        font.setFamily(u"Segoe Print")
        font.setBold(True)
        font.setWeight(75)
        self.homeBtn.setFont(font)
        self.homeBtn.setStyleSheet(u"background-color:#1f232a;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon1)
        self.homeBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.homeBtn)

        self.networksBtn = QPushButton(self.frame_2)
        self.networksBtn.setObjectName(u"networksBtn")
        self.networksBtn.setFont(font)
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/codesandbox.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.networksBtn.setIcon(icon2)
        self.networksBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.networksBtn)

        self.tradeBtn = QPushButton(self.frame_2)
        self.tradeBtn.setObjectName(u"tradeBtn")
        self.tradeBtn.setFont(font)
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/trending-up.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tradeBtn.setIcon(icon3)
        self.tradeBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.tradeBtn)

        self.miningBtn = QPushButton(self.frame_2)
        self.miningBtn.setObjectName(u"miningBtn")
        self.miningBtn.setFont(font)
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/cpu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.miningBtn.setIcon(icon4)
        self.miningBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.miningBtn)

        self.mintingBtn = QPushButton(self.frame_2)
        self.mintingBtn.setObjectName(u"mintingBtn")
        self.mintingBtn.setFont(font)
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/github.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.mintingBtn.setIcon(icon5)
        self.mintingBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.mintingBtn)

        self.nftMarketBtn = QPushButton(self.frame_2)
        self.nftMarketBtn.setObjectName(u"nftMarketBtn")
        self.nftMarketBtn.setFont(font)
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/shopping-cart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.nftMarketBtn.setIcon(icon6)
        self.nftMarketBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.nftMarketBtn)

        self.walletBtn = QPushButton(self.frame_2)
        self.walletBtn.setObjectName(u"walletBtn")
        self.walletBtn.setFont(font)
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/credit-card.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.walletBtn.setIcon(icon7)
        self.walletBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.walletBtn)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.leftMenuSubContainer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 10, 0, 10)
        self.settingsBtn = QPushButton(self.frame_3)
        self.settingsBtn.setObjectName(u"settingsBtn")
        self.settingsBtn.setFont(font)
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsBtn.setIcon(icon8)
        self.settingsBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.settingsBtn)

        self.infoBtn = QPushButton(self.frame_3)
        self.infoBtn.setObjectName(u"infoBtn")
        self.infoBtn.setFont(font)
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.infoBtn.setIcon(icon9)
        self.infoBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.infoBtn)

        self.helpBtn = QPushButton(self.frame_3)
        self.helpBtn.setObjectName(u"helpBtn")
        self.helpBtn.setFont(font)
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.helpBtn.setIcon(icon10)
        self.helpBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.helpBtn)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.leftMenuSubContainer)


        self.horizontalLayout.addWidget(self.leftMenuContainer, 0, Qt.AlignLeft)

        self.centerMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.centerMenuContainer.setObjectName(u"centerMenuContainer")
        self.centerMenuContainer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_5 = QVBoxLayout(self.centerMenuContainer)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.centerMenuSubContainer = QWidget(self.centerMenuContainer)
        self.centerMenuSubContainer.setObjectName(u"centerMenuSubContainer")
        self.centerMenuSubContainer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_6 = QVBoxLayout(self.centerMenuSubContainer)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.frame_4 = QFrame(self.centerMenuSubContainer)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)

        self.closeCenterMenuBtn = QPushButton(self.frame_4)
        self.closeCenterMenuBtn.setObjectName(u"closeCenterMenuBtn")
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/x-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeCenterMenuBtn.setIcon(icon11)
        self.closeCenterMenuBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.closeCenterMenuBtn, 0, Qt.AlignRight)


        self.verticalLayout_6.addWidget(self.frame_4, 0, Qt.AlignTop)

        self.centerMenuPages = QCustomStackedWidget(self.centerMenuSubContainer)
        self.centerMenuPages.setObjectName(u"centerMenuPages")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.centerMenuPages.sizePolicy().hasHeightForWidth())
        self.centerMenuPages.setSizePolicy(sizePolicy2)
        self.centerMenuPages.setMinimumSize(QSize(0, 0))
        self.centerMenuPages.setMaximumSize(QSize(16777215, 16777215))
        self.centerMenuPages.setFrameShape(QFrame.NoFrame)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_7 = QVBoxLayout(self.page)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.settingsMenu = QFrame(self.page)
        self.settingsMenu.setObjectName(u"settingsMenu")
        self.settingsMenu.setFrameShape(QFrame.NoFrame)
        self.settingsMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.settingsMenu)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.securityBtn = QPushButton(self.settingsMenu)
        self.securityBtn.setObjectName(u"securityBtn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.securityBtn.sizePolicy().hasHeightForWidth())
        self.securityBtn.setSizePolicy(sizePolicy3)
        self.securityBtn.setMinimumSize(QSize(0, 45))
        self.securityBtn.setFont(font1)
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/shield.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.securityBtn.setIcon(icon12)
        self.securityBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_26.addWidget(self.securityBtn)

        self.currency = QPushButton(self.settingsMenu)
        self.currency.setObjectName(u"currency")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.currency.sizePolicy().hasHeightForWidth())
        self.currency.setSizePolicy(sizePolicy4)
        self.currency.setMinimumSize(QSize(0, 45))
        self.currency.setFont(font1)
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/dollar-sign.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.currency.setIcon(icon13)
        self.currency.setIconSize(QSize(24, 24))

        self.verticalLayout_26.addWidget(self.currency)

        self.verification = QPushButton(self.settingsMenu)
        self.verification.setObjectName(u"verification")
        self.verification.setMinimumSize(QSize(0, 45))
        self.verification.setFont(font1)
        icon14 = QIcon()
        icon14.addFile(u":/icons/icons/file-text.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.verification.setIcon(icon14)
        self.verification.setIconSize(QSize(24, 24))

        self.verticalLayout_26.addWidget(self.verification)

        self.pushButton_3 = QPushButton(self.settingsMenu)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 45))
        self.pushButton_3.setFont(font1)
        icon15 = QIcon()
        icon15.addFile(u":/icons/icons/smile.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon15)
        self.pushButton_3.setIconSize(QSize(24, 24))

        self.verticalLayout_26.addWidget(self.pushButton_3)

        self.pushButton_5 = QPushButton(self.settingsMenu)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(0, 45))
        self.pushButton_5.setFont(font1)
        icon16 = QIcon()
        icon16.addFile(u":/icons/icons/pie-chart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon16)
        self.pushButton_5.setIconSize(QSize(24, 24))

        self.verticalLayout_26.addWidget(self.pushButton_5)

        self.pushButton_9 = QPushButton(self.settingsMenu)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(0, 45))
        self.pushButton_9.setFont(font1)
        icon17 = QIcon()
        icon17.addFile(u":/icons/icons/user-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon17)
        self.pushButton_9.setIconSize(QSize(24, 24))

        self.verticalLayout_26.addWidget(self.pushButton_9)

        self.pushButton_21 = QPushButton(self.settingsMenu)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setMinimumSize(QSize(0, 45))
        self.pushButton_21.setFont(font1)
        icon18 = QIcon()
        icon18.addFile(u":/icons/icons/log-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_21.setIcon(icon18)
        self.pushButton_21.setIconSize(QSize(24, 24))

        self.verticalLayout_26.addWidget(self.pushButton_21)

        self.pushButton_42 = QPushButton(self.settingsMenu)
        self.pushButton_42.setObjectName(u"pushButton_42")
        self.pushButton_42.setMinimumSize(QSize(0, 45))
        self.pushButton_42.setFont(font1)
        icon19 = QIcon()
        icon19.addFile(u":/icons/icons/book.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_42.setIcon(icon19)
        self.pushButton_42.setIconSize(QSize(24, 24))

        self.verticalLayout_26.addWidget(self.pushButton_42)


        self.verticalLayout_7.addWidget(self.settingsMenu, 0, Qt.AlignTop)

        self.centerMenuPages.addWidget(self.page)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_9 = QVBoxLayout(self.page_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_4 = QLabel(self.page_3)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setFamily(u"Segoe Print")
        font2.setPointSize(13)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_4, 0, Qt.AlignTop)

        self.frame_62 = QFrame(self.page_3)
        self.frame_62.setObjectName(u"frame_62")
        sizePolicy.setHeightForWidth(self.frame_62.sizePolicy().hasHeightForWidth())
        self.frame_62.setSizePolicy(sizePolicy)
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)
        self.textEdit_3 = QTextEdit(self.frame_62)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(0, 0, 222, 696))
        sizePolicy.setHeightForWidth(self.textEdit_3.sizePolicy().hasHeightForWidth())
        self.textEdit_3.setSizePolicy(sizePolicy)
        self.textEdit_3.setMinimumSize(QSize(222, 0))
        font3 = QFont()
        font3.setPointSize(10)
        self.textEdit_3.setFont(font3)
        self.textEdit_3.setStyleSheet(u"background: transparent;")
        self.textEdit_3.setFrameShape(QFrame.NoFrame)
        self.textEdit_3.setReadOnly(True)

        self.verticalLayout_9.addWidget(self.frame_62)

        self.centerMenuPages.addWidget(self.page_3)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_8 = QVBoxLayout(self.page_2)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.extraCenter = QFrame(self.page_2)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setStyleSheet(u"")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_25.setSpacing(9)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(9, 9, 9, 9)
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setFont(font3)
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_25.addWidget(self.textEdit)


        self.verticalLayout_8.addWidget(self.extraCenter)

        self.centerMenuPages.addWidget(self.page_2)

        self.verticalLayout_6.addWidget(self.centerMenuPages)


        self.verticalLayout_5.addWidget(self.centerMenuSubContainer)


        self.horizontalLayout.addWidget(self.centerMenuContainer)

        self.mainBodyContainer = QWidget(self.centralwidget)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy5)
        self.mainBodyContainer.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, -1, 0)
        self.headerContainer = QWidget(self.mainBodyContainer)
        self.headerContainer.setObjectName(u"headerContainer")
        self.horizontalLayout_5 = QHBoxLayout(self.headerContainer)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_5 = QFrame(self.headerContainer)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.pushButton_41 = QPushButton(self.frame_5)
        self.pushButton_41.setObjectName(u"pushButton_41")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.pushButton_41.sizePolicy().hasHeightForWidth())
        self.pushButton_41.setSizePolicy(sizePolicy6)
        icon20 = QIcon()
        icon20.addFile(u":/icons/parachronos_adobe_express.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_41.setIcon(icon20)
        self.pushButton_41.setIconSize(QSize(40, 40))

        self.horizontalLayout_7.addWidget(self.pushButton_41)

        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        font4 = QFont()
        font4.setFamily(u"Segoe Print")
        font4.setPointSize(11)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_6.setFont(font4)

        self.horizontalLayout_7.addWidget(self.label_6)


        self.horizontalLayout_5.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.headerContainer)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.notificationBtn = QPushButton(self.frame_6)
        self.notificationBtn.setObjectName(u"notificationBtn")
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.notificationBtn.sizePolicy().hasHeightForWidth())
        self.notificationBtn.setSizePolicy(sizePolicy7)
        icon21 = QIcon()
        icon21.addFile(u":/icons/icons/bell.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.notificationBtn.setIcon(icon21)
        self.notificationBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.notificationBtn)

        self.moreMenuBtn = QPushButton(self.frame_6)
        self.moreMenuBtn.setObjectName(u"moreMenuBtn")
        sizePolicy7.setHeightForWidth(self.moreMenuBtn.sizePolicy().hasHeightForWidth())
        self.moreMenuBtn.setSizePolicy(sizePolicy7)
        icon22 = QIcon()
        icon22.addFile(u":/icons/icons/more-horizontal.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.moreMenuBtn.setIcon(icon22)
        self.moreMenuBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.moreMenuBtn)

        self.profileMenuBtn = QPushButton(self.frame_6)
        self.profileMenuBtn.setObjectName(u"profileMenuBtn")
        sizePolicy7.setHeightForWidth(self.profileMenuBtn.sizePolicy().hasHeightForWidth())
        self.profileMenuBtn.setSizePolicy(sizePolicy7)
        self.profileMenuBtn.setMaximumSize(QSize(16777215, 16777215))
        icon23 = QIcon()
        icon23.addFile(u":/icons/icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.profileMenuBtn.setIcon(icon23)
        self.profileMenuBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.profileMenuBtn)


        self.horizontalLayout_5.addWidget(self.frame_6, 0, Qt.AlignHCenter)

        self.frame_7 = QFrame(self.headerContainer)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.minimize_window_btn = QPushButton(self.frame_7)
        self.minimize_window_btn.setObjectName(u"minimize_window_btn")
        icon24 = QIcon()
        icon24.addFile(u":/icons/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_window_btn.setIcon(icon24)
        self.minimize_window_btn.setIconSize(QSize(16, 16))

        self.horizontalLayout_4.addWidget(self.minimize_window_btn)

        self.restore_window_btn = QPushButton(self.frame_7)
        self.restore_window_btn.setObjectName(u"restore_window_btn")
        icon25 = QIcon()
        icon25.addFile(u":/icons/icons/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_window_btn.setIcon(icon25)
        self.restore_window_btn.setIconSize(QSize(14, 14))

        self.horizontalLayout_4.addWidget(self.restore_window_btn)

        self.close_window_btn = QPushButton(self.frame_7)
        self.close_window_btn.setObjectName(u"close_window_btn")
        icon26 = QIcon()
        icon26.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_window_btn.setIcon(icon26)
        self.close_window_btn.setIconSize(QSize(16, 16))

        self.horizontalLayout_4.addWidget(self.close_window_btn)


        self.horizontalLayout_5.addWidget(self.frame_7, 0, Qt.AlignRight)


        self.verticalLayout_10.addWidget(self.headerContainer)

        self.mainBodyContent = QWidget(self.mainBodyContainer)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.mainBodyContent.sizePolicy().hasHeightForWidth())
        self.mainBodyContent.setSizePolicy(sizePolicy8)
        self.horizontalLayout_8 = QHBoxLayout(self.mainBodyContent)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.mainContentsContainer = QWidget(self.mainBodyContent)
        self.mainContentsContainer.setObjectName(u"mainContentsContainer")
        self.verticalLayout_15 = QVBoxLayout(self.mainContentsContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_8.addWidget(self.mainContentsContainer)

        self.mainPages = QCustomStackedWidget(self.mainBodyContent)
        self.mainPages.setObjectName(u"mainPages")
        sizePolicy.setHeightForWidth(self.mainPages.sizePolicy().hasHeightForWidth())
        self.mainPages.setSizePolicy(sizePolicy)
        self.mainPages.setToolTipDuration(0)
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.home_page.setStyleSheet(u"")
        self.verticalLayout_16 = QVBoxLayout(self.home_page)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_29 = QFrame(self.home_page)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.frame_29)
        self.verticalLayout_51.setSpacing(0)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.frame_29)
        self.label_10.setObjectName(u"label_10")
        font5 = QFont()
        font5.setFamily(u"Segoe Print")
        font5.setPointSize(12)
        font5.setBold(True)
        font5.setWeight(75)
        self.label_10.setFont(font5)
        self.label_10.setStyleSheet(u"border-radius:10px;")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_51.addWidget(self.label_10, 0, Qt.AlignTop)


        self.verticalLayout_16.addWidget(self.frame_29)

        self.widget_3 = QWidget(self.home_page)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setStyleSheet(u"border-radius:10px;")
        self.verticalLayout_52 = QVBoxLayout(self.widget_3)
        self.verticalLayout_52.setSpacing(0)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.frame_30 = QFrame(self.widget_3)
        self.frame_30.setObjectName(u"frame_30")
        sizePolicy4.setHeightForWidth(self.frame_30.sizePolicy().hasHeightForWidth())
        self.frame_30.setSizePolicy(sizePolicy4)
        self.frame_30.setStyleSheet(u"text-align:left;\n"
"padding: 5px 10px;\n"
"border-top-left-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.actionBar = QFrame(self.frame_30)
        self.actionBar.setObjectName(u"actionBar")
        sizePolicy1.setHeightForWidth(self.actionBar.sizePolicy().hasHeightForWidth())
        self.actionBar.setSizePolicy(sizePolicy1)
        self.actionBar.setStyleSheet(u"")
        self.actionBar.setFrameShape(QFrame.NoFrame)
        self.actionBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.actionBar)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.backBtn = QPushButton(self.actionBar)
        self.backBtn.setObjectName(u"backBtn")
        self.backBtn.setFont(font)
        self.backBtn.setStyleSheet(u"background-color:#1f232a;")
        icon27 = QIcon()
        icon27.addFile(u":/icons/icons/chevron-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.backBtn.setIcon(icon27)
        self.backBtn.setIconSize(QSize(16, 16))

        self.horizontalLayout_16.addWidget(self.backBtn)

        self.forwardBtn = QPushButton(self.actionBar)
        self.forwardBtn.setObjectName(u"forwardBtn")
        self.forwardBtn.setFont(font)
        self.forwardBtn.setStyleSheet(u"background-color:#1f232a;")
        icon28 = QIcon()
        icon28.addFile(u":/icons/icons/chevron-right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.forwardBtn.setIcon(icon28)
        self.forwardBtn.setIconSize(QSize(16, 16))

        self.horizontalLayout_16.addWidget(self.forwardBtn)

        self.reloadBtn = QPushButton(self.actionBar)
        self.reloadBtn.setObjectName(u"reloadBtn")
        self.reloadBtn.setFont(font)
        self.reloadBtn.setStyleSheet(u"background-color:#1f232a;")
        icon29 = QIcon()
        icon29.addFile(u":/icons/icons/rotate-cw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.reloadBtn.setIcon(icon29)
        self.reloadBtn.setIconSize(QSize(16, 16))

        self.horizontalLayout_16.addWidget(self.reloadBtn)

        self.polkBtn = QPushButton(self.actionBar)
        self.polkBtn.setObjectName(u"polkBtn")
        self.polkBtn.setStyleSheet(u"background-color:#1f232a;")
        self.polkBtn.setIcon(icon1)
        self.polkBtn.setIconSize(QSize(16, 16))

        self.horizontalLayout_16.addWidget(self.polkBtn)

        self.quickLinksBtn = QPushButton(self.actionBar)
        self.quickLinksBtn.setObjectName(u"quickLinksBtn")
        self.quickLinksBtn.setStyleSheet(u"background-color:#1f232a;")
        icon30 = QIcon()
        icon30.addFile(u":/icons/icons/grid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.quickLinksBtn.setIcon(icon30)

        self.horizontalLayout_16.addWidget(self.quickLinksBtn)


        self.horizontalLayout_13.addWidget(self.actionBar, 0, Qt.AlignTop)

        self.frame_32 = QFrame(self.frame_30)
        self.frame_32.setObjectName(u"frame_32")
        sizePolicy5.setHeightForWidth(self.frame_32.sizePolicy().hasHeightForWidth())
        self.frame_32.setSizePolicy(sizePolicy5)
        self.frame_32.setLayoutDirection(Qt.LeftToRight)
        self.frame_32.setFrameShape(QFrame.NoFrame)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.addressBar = QLineEdit(self.frame_32)
        self.addressBar.setObjectName(u"addressBar")
        sizePolicy5.setHeightForWidth(self.addressBar.sizePolicy().hasHeightForWidth())
        self.addressBar.setSizePolicy(sizePolicy5)
        self.addressBar.setMinimumSize(QSize(300, 30))
        self.addressBar.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_4.addWidget(self.addressBar, 0, 1, 1, 1)

        self.searchAddressBar = QPushButton(self.frame_32)
        self.searchAddressBar.setObjectName(u"searchAddressBar")
        sizePolicy6.setHeightForWidth(self.searchAddressBar.sizePolicy().hasHeightForWidth())
        self.searchAddressBar.setSizePolicy(sizePolicy6)
        self.searchAddressBar.setMinimumSize(QSize(30, 30))
        self.searchAddressBar.setFont(font)
        self.searchAddressBar.setStyleSheet(u"")
        icon31 = QIcon()
        icon31.addFile(u":/icons/icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.searchAddressBar.setIcon(icon31)
        self.searchAddressBar.setIconSize(QSize(16, 16))

        self.gridLayout_4.addWidget(self.searchAddressBar, 0, 2, 1, 1)

        self.CertBtn = QPushButton(self.frame_32)
        self.CertBtn.setObjectName(u"CertBtn")
        sizePolicy6.setHeightForWidth(self.CertBtn.sizePolicy().hasHeightForWidth())
        self.CertBtn.setSizePolicy(sizePolicy6)
        self.CertBtn.setStyleSheet(u"background-color:#1f232a;")
        icon32 = QIcon()
        icon32.addFile(u":/icons/icons/lock.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.CertBtn.setIcon(icon32)

        self.gridLayout_4.addWidget(self.CertBtn, 0, 0, 1, 1, Qt.AlignHCenter)


        self.horizontalLayout_17.addLayout(self.gridLayout_4)


        self.horizontalLayout_13.addWidget(self.frame_32, 0, Qt.AlignTop)

        self.frame_33 = QFrame(self.frame_30)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.NoFrame)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.zoomOutBtn = QPushButton(self.frame_33)
        self.zoomOutBtn.setObjectName(u"zoomOutBtn")
        self.zoomOutBtn.setStyleSheet(u"background-color:#1f232a;")
        icon33 = QIcon()
        icon33.addFile(u":/icons/icons/plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.zoomOutBtn.setIcon(icon33)

        self.horizontalLayout_18.addWidget(self.zoomOutBtn)

        self.zoomInBtn = QPushButton(self.frame_33)
        self.zoomInBtn.setObjectName(u"zoomInBtn")
        self.zoomInBtn.setStyleSheet(u"background-color:#1f232a;")
        self.zoomInBtn.setIcon(icon24)

        self.horizontalLayout_18.addWidget(self.zoomInBtn)

        self.pushButton_17 = QPushButton(self.frame_33)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setStyleSheet(u"background-color:#1f232a;")
        icon34 = QIcon()
        icon34.addFile(u":/icons/icons/heart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_17.setIcon(icon34)
        self.pushButton_17.setIconSize(QSize(16, 16))

        self.horizontalLayout_18.addWidget(self.pushButton_17)

        self.pushButton_19 = QPushButton(self.frame_33)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setStyleSheet(u"background-color:#1f232a;")
        icon35 = QIcon()
        icon35.addFile(u":/icons/icons/camera.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_19.setIcon(icon35)
        self.pushButton_19.setIconSize(QSize(16, 16))

        self.horizontalLayout_18.addWidget(self.pushButton_19)


        self.horizontalLayout_13.addWidget(self.frame_33, 0, Qt.AlignTop)


        self.verticalLayout_52.addWidget(self.frame_30)

        self.webViewContainer = QWidget(self.widget_3)
        self.webViewContainer.setObjectName(u"webViewContainer")
        sizePolicy.setHeightForWidth(self.webViewContainer.sizePolicy().hasHeightForWidth())
        self.webViewContainer.setSizePolicy(sizePolicy)
        self.webViewContainer.setMinimumSize(QSize(0, 0))
        self.webViewContainer.setStyleSheet(u"border-radius:10px;")
        self.verticalLayout_53 = QVBoxLayout(self.webViewContainer)
        self.verticalLayout_53.setSpacing(0)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_52.addWidget(self.webViewContainer)


        self.verticalLayout_16.addWidget(self.widget_3)

        self.mainPages.addWidget(self.home_page)
        self.para_page = QWidget()
        self.para_page.setObjectName(u"para_page")
        self.para_page.setStyleSheet(u"background-color: transparent;")
        self.verticalLayout_17 = QVBoxLayout(self.para_page)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_15 = QLabel(self.para_page)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font5)

        self.verticalLayout_17.addWidget(self.label_15)

        self.paraFrame = QFrame(self.para_page)
        self.paraFrame.setObjectName(u"paraFrame")
        sizePolicy4.setHeightForWidth(self.paraFrame.sizePolicy().hasHeightForWidth())
        self.paraFrame.setSizePolicy(sizePolicy4)
        font6 = QFont()
        font6.setFamily(u"MS Serif")
        self.paraFrame.setFont(font6)
        self.paraFrame.setFrameShape(QFrame.StyledPanel)
        self.paraFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.paraFrame)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.Dashboard = QFrame(self.paraFrame)
        self.Dashboard.setObjectName(u"Dashboard")
        sizePolicy4.setHeightForWidth(self.Dashboard.sizePolicy().hasHeightForWidth())
        self.Dashboard.setSizePolicy(sizePolicy4)
        self.Dashboard.setMinimumSize(QSize(0, 200))
        self.Dashboard.setFrameShape(QFrame.StyledPanel)
        self.Dashboard.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.Dashboard)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.frame_37 = QFrame(self.Dashboard)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.frame_37)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.frame_38 = QFrame(self.frame_37)
        self.frame_38.setObjectName(u"frame_38")
        sizePolicy9 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.frame_38.sizePolicy().hasHeightForWidth())
        self.frame_38.setSizePolicy(sizePolicy9)
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.frame_38)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.label_17 = QLabel(self.frame_38)
        self.label_17.setObjectName(u"label_17")
        font7 = QFont()
        font7.setFamily(u"Segoe Print")
        font7.setPointSize(14)
        font7.setBold(True)
        font7.setWeight(75)
        self.label_17.setFont(font7)

        self.verticalLayout_49.addWidget(self.label_17, 0, Qt.AlignTop)


        self.verticalLayout_48.addWidget(self.frame_38)

        self.frame_39 = QFrame(self.frame_37)
        self.frame_39.setObjectName(u"frame_39")
        sizePolicy6.setHeightForWidth(self.frame_39.sizePolicy().hasHeightForWidth())
        self.frame_39.setSizePolicy(sizePolicy6)
        self.frame_39.setMinimumSize(QSize(300, 50))
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.balanceLabel = QLabel(self.frame_39)
        self.balanceLabel.setObjectName(u"balanceLabel")
        sizePolicy6.setHeightForWidth(self.balanceLabel.sizePolicy().hasHeightForWidth())
        self.balanceLabel.setSizePolicy(sizePolicy6)
        self.balanceLabel.setMinimumSize(QSize(200, 40))
        font8 = QFont()
        font8.setBold(True)
        font8.setWeight(75)
        self.balanceLabel.setFont(font8)
        self.balanceLabel.setStyleSheet(u"background-color: rgb(255, 0, 127);\n"
"border-radius:10px;")
        self.balanceLabel.setInputMethodHints(Qt.ImhHiddenText)
        self.balanceLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.balanceLabel)

        self.checkBalanceBtn = QPushButton(self.frame_39)
        self.checkBalanceBtn.setObjectName(u"checkBalanceBtn")
        sizePolicy6.setHeightForWidth(self.checkBalanceBtn.sizePolicy().hasHeightForWidth())
        self.checkBalanceBtn.setSizePolicy(sizePolicy6)
        self.checkBalanceBtn.setMinimumSize(QSize(0, 40))
        self.checkBalanceBtn.setIconSize(QSize(24, 24))
        self.checkBalanceBtn.setCheckable(False)
        self.checkBalanceBtn.setChecked(False)

        self.horizontalLayout_19.addWidget(self.checkBalanceBtn)


        self.verticalLayout_48.addWidget(self.frame_39)


        self.horizontalLayout_35.addWidget(self.frame_37)

        self.frame_65 = QFrame(self.Dashboard)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(255, 0, 127);")
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_65)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label_26 = QLabel(self.frame_65)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font8)
        self.label_26.setTextFormat(Qt.AutoText)

        self.verticalLayout_31.addWidget(self.label_26)

        self.frame_67 = QFrame(self.frame_65)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.frame_67)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.label_71 = QLabel(self.frame_67)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setFont(font8)
        self.label_71.setTextFormat(Qt.AutoText)

        self.verticalLayout_44.addWidget(self.label_71)

        self.label_72 = QLabel(self.frame_67)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setFont(font8)
        self.label_72.setTextFormat(Qt.AutoText)

        self.verticalLayout_44.addWidget(self.label_72)

        self.frame_57 = QFrame(self.frame_67)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_57)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.pushButton_20 = QPushButton(self.frame_57)
        self.pushButton_20.setObjectName(u"pushButton_20")
        sizePolicy3.setHeightForWidth(self.pushButton_20.sizePolicy().hasHeightForWidth())
        self.pushButton_20.setSizePolicy(sizePolicy3)
        self.pushButton_20.setMinimumSize(QSize(40, 25))
        self.pushButton_20.setFont(font8)
        self.pushButton_20.setStyleSheet(u"background-color: #351c75;\n"
"border-radius:10px;")

        self.horizontalLayout_25.addWidget(self.pushButton_20)

        self.pushButton_8 = QPushButton(self.frame_57)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy3.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy3)
        self.pushButton_8.setMinimumSize(QSize(40, 25))
        self.pushButton_8.setFont(font8)
        self.pushButton_8.setStyleSheet(u"background-color: #351c75;\n"
"border-radius:10px;")

        self.horizontalLayout_25.addWidget(self.pushButton_8)


        self.verticalLayout_44.addWidget(self.frame_57)


        self.verticalLayout_31.addWidget(self.frame_67)


        self.horizontalLayout_35.addWidget(self.frame_65)

        self.frame_66 = QFrame(self.Dashboard)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setToolTipDuration(0)
        self.frame_66.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(255, 0, 127);")
        self.frame_66.setFrameShape(QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_66)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.stackedWidget = QStackedWidget(self.frame_66)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"border-radius:10px;")
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        sizePolicy6.setHeightForWidth(self.page_7.sizePolicy().hasHeightForWidth())
        self.page_7.setSizePolicy(sizePolicy6)
        self.page_7.setStyleSheet(u"border-radius:10px;\n"
"")
        self.horizontalLayout_38 = QHBoxLayout(self.page_7)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.frame_70 = QFrame(self.page_7)
        self.frame_70.setObjectName(u"frame_70")
        sizePolicy6.setHeightForWidth(self.frame_70.sizePolicy().hasHeightForWidth())
        self.frame_70.setSizePolicy(sizePolicy6)
        self.frame_70.setFrameShape(QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_70)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.pushButton_22 = QPushButton(self.frame_70)
        self.pushButton_22.setObjectName(u"pushButton_22")
        icon36 = QIcon()
        icon36.addFile(u":/icons/icons/sunrise.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_22.setIcon(icon36)
        self.pushButton_22.setIconSize(QSize(40, 40))

        self.horizontalLayout_39.addWidget(self.pushButton_22)

        self.frame_71 = QFrame(self.frame_70)
        self.frame_71.setObjectName(u"frame_71")
        sizePolicy6.setHeightForWidth(self.frame_71.sizePolicy().hasHeightForWidth())
        self.frame_71.setSizePolicy(sizePolicy6)
        self.frame_71.setFrameShape(QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QFrame.Raised)
        self.verticalLayout_76 = QVBoxLayout(self.frame_71)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.label_22 = QLabel(self.frame_71)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font8)

        self.verticalLayout_76.addWidget(self.label_22)

        self.label_23 = QLabel(self.frame_71)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font8)

        self.verticalLayout_76.addWidget(self.label_23)

        self.label_24 = QLabel(self.frame_71)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font8)

        self.verticalLayout_76.addWidget(self.label_24)

        self.label_25 = QLabel(self.frame_71)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font8)

        self.verticalLayout_76.addWidget(self.label_25)


        self.horizontalLayout_39.addWidget(self.frame_71)


        self.horizontalLayout_38.addWidget(self.frame_70)

        self.stackedWidget.addWidget(self.page_7)

        self.horizontalLayout_37.addWidget(self.stackedWidget)


        self.horizontalLayout_35.addWidget(self.frame_66)

        self.frame_72 = QFrame(self.Dashboard)
        self.frame_72.setObjectName(u"frame_72")
        self.frame_72.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(255, 0, 127);")
        self.frame_72.setFrameShape(QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QFrame.Raised)
        self.verticalLayout_77 = QVBoxLayout(self.frame_72)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.label_77 = QLabel(self.frame_72)
        self.label_77.setObjectName(u"label_77")
        sizePolicy6.setHeightForWidth(self.label_77.sizePolicy().hasHeightForWidth())
        self.label_77.setSizePolicy(sizePolicy6)
        self.label_77.setFont(font8)

        self.verticalLayout_77.addWidget(self.label_77)

        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setVerticalSpacing(0)
        self.addressBar_2 = QLineEdit(self.frame_72)
        self.addressBar_2.setObjectName(u"addressBar_2")
        sizePolicy5.setHeightForWidth(self.addressBar_2.sizePolicy().hasHeightForWidth())
        self.addressBar_2.setSizePolicy(sizePolicy5)
        self.addressBar_2.setMinimumSize(QSize(140, 30))
        self.addressBar_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_15.addWidget(self.addressBar_2, 0, 1, 1, 1)

        self.searchAddressBar_2 = QPushButton(self.frame_72)
        self.searchAddressBar_2.setObjectName(u"searchAddressBar_2")
        sizePolicy6.setHeightForWidth(self.searchAddressBar_2.sizePolicy().hasHeightForWidth())
        self.searchAddressBar_2.setSizePolicy(sizePolicy6)
        self.searchAddressBar_2.setMinimumSize(QSize(30, 30))
        self.searchAddressBar_2.setFont(font)
        self.searchAddressBar_2.setStyleSheet(u"background-color: rgb(31, 35, 42);")
        self.searchAddressBar_2.setIcon(icon31)
        self.searchAddressBar_2.setIconSize(QSize(16, 16))

        self.gridLayout_15.addWidget(self.searchAddressBar_2, 0, 2, 1, 1)

        self.CertBtn_3 = QPushButton(self.frame_72)
        self.CertBtn_3.setObjectName(u"CertBtn_3")
        sizePolicy6.setHeightForWidth(self.CertBtn_3.sizePolicy().hasHeightForWidth())
        self.CertBtn_3.setSizePolicy(sizePolicy6)
        self.CertBtn_3.setStyleSheet(u"background-color:#1f232a;\n"
"border-radius:10px;")
        self.CertBtn_3.setIcon(icon32)

        self.gridLayout_15.addWidget(self.CertBtn_3, 0, 0, 1, 1, Qt.AlignHCenter)


        self.verticalLayout_77.addLayout(self.gridLayout_15)

        self.label_78 = QLabel(self.frame_72)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setFont(font8)

        self.verticalLayout_77.addWidget(self.label_78)


        self.horizontalLayout_35.addWidget(self.frame_72)


        self.verticalLayout_23.addWidget(self.Dashboard)


        self.verticalLayout_17.addWidget(self.paraFrame)

        self.frame_68 = QFrame(self.para_page)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(255, 0, 127);")
        self.frame_68.setFrameShape(QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QFrame.Raised)
        self.verticalLayout_62 = QVBoxLayout(self.frame_68)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.frame_69 = QFrame(self.frame_68)
        self.frame_69.setObjectName(u"frame_69")
        font9 = QFont()
        font9.setPointSize(10)
        font9.setBold(True)
        font9.setUnderline(False)
        font9.setWeight(75)
        self.frame_69.setFont(font9)
        self.frame_69.setStyleSheet(u"")
        self.frame_69.setFrameShape(QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_69)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_73 = QLabel(self.frame_69)
        self.label_73.setObjectName(u"label_73")
        font10 = QFont()
        font10.setBold(True)
        font10.setUnderline(True)
        font10.setWeight(75)
        self.label_73.setFont(font10)
        self.label_73.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_36.addWidget(self.label_73)

        self.label_74 = QLabel(self.frame_69)
        self.label_74.setObjectName(u"label_74")
        font11 = QFont()
        font11.setBold(True)
        font11.setItalic(False)
        font11.setUnderline(True)
        font11.setWeight(75)
        self.label_74.setFont(font11)
        self.label_74.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_36.addWidget(self.label_74)

        self.label_75 = QLabel(self.frame_69)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setFont(font10)
        self.label_75.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_36.addWidget(self.label_75)

        self.label_76 = QLabel(self.frame_69)
        self.label_76.setObjectName(u"label_76")
        font12 = QFont()
        font12.setPointSize(8)
        font12.setBold(True)
        font12.setUnderline(True)
        font12.setWeight(75)
        self.label_76.setFont(font12)
        self.label_76.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_36.addWidget(self.label_76)


        self.verticalLayout_62.addWidget(self.frame_69)


        self.verticalLayout_17.addWidget(self.frame_68)

        self.scrollArea_3 = QScrollArea(self.para_page)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setStyleSheet(u"background-color: transparent;")
        self.scrollArea_3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 462, 366))
        self.verticalLayout_32 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.widget_4 = QWidget(self.scrollAreaWidgetContents_3)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_75 = QVBoxLayout(self.widget_4)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.frame_58 = QFrame(self.widget_4)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_58)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.pushButton_34 = QPushButton(self.frame_58)
        self.pushButton_34.setObjectName(u"pushButton_34")
        sizePolicy10 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.pushButton_34.sizePolicy().hasHeightForWidth())
        self.pushButton_34.setSizePolicy(sizePolicy10)
        font13 = QFont()
        font13.setPointSize(8)
        font13.setBold(True)
        font13.setWeight(75)
        self.pushButton_34.setFont(font13)
        icon37 = QIcon()
        icon37.addFile(u":/icons/icons/dot.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_34.setIcon(icon37)
        self.pushButton_34.setIconSize(QSize(24, 24))

        self.horizontalLayout_26.addWidget(self.pushButton_34)

        self.label_27 = QLabel(self.frame_58)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font8)
        self.label_27.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_26.addWidget(self.label_27)

        self.label_28 = QLabel(self.frame_58)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font8)
        self.label_28.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_26.addWidget(self.label_28)

        self.label_29 = QLabel(self.frame_58)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font8)
        self.label_29.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_26.addWidget(self.label_29)


        self.verticalLayout_75.addWidget(self.frame_58)

        self.frame_59 = QFrame(self.widget_4)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_59)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.pushButton_35 = QPushButton(self.frame_59)
        self.pushButton_35.setObjectName(u"pushButton_35")
        sizePolicy10.setHeightForWidth(self.pushButton_35.sizePolicy().hasHeightForWidth())
        self.pushButton_35.setSizePolicy(sizePolicy10)
        self.pushButton_35.setFont(font13)
        self.pushButton_35.setStyleSheet(u"background-color:transparent;")
        icon38 = QIcon()
        icon38.addFile(u":/icons/icons/bnb.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_35.setIcon(icon38)
        self.pushButton_35.setIconSize(QSize(24, 24))

        self.horizontalLayout_27.addWidget(self.pushButton_35)

        self.label_31 = QLabel(self.frame_59)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font8)
        self.label_31.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.label_31)

        self.label_30 = QLabel(self.frame_59)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font8)
        self.label_30.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.label_30)

        self.label_32 = QLabel(self.frame_59)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font8)
        self.label_32.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.label_32)


        self.verticalLayout_75.addWidget(self.frame_59)

        self.frame_60 = QFrame(self.widget_4)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_60)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.pushButton_36 = QPushButton(self.frame_60)
        self.pushButton_36.setObjectName(u"pushButton_36")
        sizePolicy10.setHeightForWidth(self.pushButton_36.sizePolicy().hasHeightForWidth())
        self.pushButton_36.setSizePolicy(sizePolicy10)
        self.pushButton_36.setFont(font13)
        icon39 = QIcon()
        icon39.addFile(u":/icons/icons/eos.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_36.setIcon(icon39)
        self.pushButton_36.setIconSize(QSize(24, 24))

        self.horizontalLayout_28.addWidget(self.pushButton_36)

        self.label_60 = QLabel(self.frame_60)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setFont(font8)
        self.label_60.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_28.addWidget(self.label_60)

        self.label_59 = QLabel(self.frame_60)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setFont(font8)
        self.label_59.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_28.addWidget(self.label_59)

        self.label_61 = QLabel(self.frame_60)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setFont(font8)
        self.label_61.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_28.addWidget(self.label_61)


        self.verticalLayout_75.addWidget(self.frame_60)

        self.frame_61 = QFrame(self.widget_4)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_61)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.pushButton_37 = QPushButton(self.frame_61)
        self.pushButton_37.setObjectName(u"pushButton_37")
        sizePolicy10.setHeightForWidth(self.pushButton_37.sizePolicy().hasHeightForWidth())
        self.pushButton_37.setSizePolicy(sizePolicy10)
        self.pushButton_37.setFont(font13)
        icon40 = QIcon()
        icon40.addFile(u":/icons/icons/etherum.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_37.setIcon(icon40)
        self.pushButton_37.setIconSize(QSize(24, 24))

        self.horizontalLayout_31.addWidget(self.pushButton_37)

        self.label_63 = QLabel(self.frame_61)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setFont(font8)
        self.label_63.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_31.addWidget(self.label_63)

        self.label_62 = QLabel(self.frame_61)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setFont(font8)
        self.label_62.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_31.addWidget(self.label_62)

        self.label_64 = QLabel(self.frame_61)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setFont(font8)
        self.label_64.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_31.addWidget(self.label_64)


        self.verticalLayout_75.addWidget(self.frame_61)

        self.frame_56 = QFrame(self.widget_4)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_56)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.pushButton_38 = QPushButton(self.frame_56)
        self.pushButton_38.setObjectName(u"pushButton_38")
        sizePolicy10.setHeightForWidth(self.pushButton_38.sizePolicy().hasHeightForWidth())
        self.pushButton_38.setSizePolicy(sizePolicy10)
        self.pushButton_38.setFont(font13)
        icon41 = QIcon()
        icon41.addFile(u":/icons/icons/polygon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_38.setIcon(icon41)
        self.pushButton_38.setIconSize(QSize(24, 24))

        self.horizontalLayout_32.addWidget(self.pushButton_38)

        self.label_44 = QLabel(self.frame_56)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setFont(font8)
        self.label_44.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_32.addWidget(self.label_44)

        self.label_37 = QLabel(self.frame_56)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font8)
        self.label_37.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_32.addWidget(self.label_37)

        self.label_45 = QLabel(self.frame_56)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setFont(font8)
        self.label_45.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_32.addWidget(self.label_45)


        self.verticalLayout_75.addWidget(self.frame_56)

        self.frame_63 = QFrame(self.widget_4)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_63)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.pushButton_39 = QPushButton(self.frame_63)
        self.pushButton_39.setObjectName(u"pushButton_39")
        sizePolicy10.setHeightForWidth(self.pushButton_39.sizePolicy().hasHeightForWidth())
        self.pushButton_39.setSizePolicy(sizePolicy10)
        self.pushButton_39.setFont(font13)
        icon42 = QIcon()
        icon42.addFile(u":/icons/icons/tether.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_39.setIcon(icon42)
        self.pushButton_39.setIconSize(QSize(24, 24))

        self.horizontalLayout_33.addWidget(self.pushButton_39)

        self.label_66 = QLabel(self.frame_63)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setFont(font8)
        self.label_66.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_33.addWidget(self.label_66)

        self.label_65 = QLabel(self.frame_63)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setFont(font8)
        self.label_65.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_33.addWidget(self.label_65)

        self.label_67 = QLabel(self.frame_63)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setFont(font8)
        self.label_67.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_33.addWidget(self.label_67)


        self.verticalLayout_75.addWidget(self.frame_63)

        self.frame_64 = QFrame(self.widget_4)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setFrameShape(QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_64)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.pushButton_40 = QPushButton(self.frame_64)
        self.pushButton_40.setObjectName(u"pushButton_40")
        sizePolicy10.setHeightForWidth(self.pushButton_40.sizePolicy().hasHeightForWidth())
        self.pushButton_40.setSizePolicy(sizePolicy10)
        self.pushButton_40.setFont(font13)
        icon43 = QIcon()
        icon43.addFile(u":/icons/icons/bitcoin.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_40.setIcon(icon43)
        self.pushButton_40.setIconSize(QSize(24, 24))

        self.horizontalLayout_34.addWidget(self.pushButton_40)

        self.label_68 = QLabel(self.frame_64)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setFont(font8)
        self.label_68.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_34.addWidget(self.label_68)

        self.label_69 = QLabel(self.frame_64)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setFont(font8)
        self.label_69.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_34.addWidget(self.label_69)

        self.label_70 = QLabel(self.frame_64)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setFont(font8)
        self.label_70.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_34.addWidget(self.label_70)


        self.verticalLayout_75.addWidget(self.frame_64)


        self.verticalLayout_32.addWidget(self.widget_4)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_17.addWidget(self.scrollArea_3)

        self.mainPages.addWidget(self.para_page)
        self.trade_page = QWidget()
        self.trade_page.setObjectName(u"trade_page")
        self.verticalLayout_18 = QVBoxLayout(self.trade_page)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_10 = QFrame(self.trade_page)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy)
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_10)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.frame_13 = QFrame(self.frame_10)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy)
        self.frame_13.setMinimumSize(QSize(800, 70))
        self.frame_13.setMaximumSize(QSize(0, 0))
        self.frame_13.setStyleSheet(u"background-color:transparent;\n"
"border-radius: 10px")
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(-1, 0, -1, 0)
        self.frame_76 = QFrame(self.frame_13)
        self.frame_76.setObjectName(u"frame_76")
        sizePolicy5.setHeightForWidth(self.frame_76.sizePolicy().hasHeightForWidth())
        self.frame_76.setSizePolicy(sizePolicy5)
        self.frame_76.setStyleSheet(u"background-color:transparent;")
        self.frame_76.setFrameShape(QFrame.StyledPanel)
        self.frame_76.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_76)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.frame_77 = QFrame(self.frame_76)
        self.frame_77.setObjectName(u"frame_77")
        self.frame_77.setStyleSheet(u"background-color: rgb(255, 0, 127);")
        self.frame_77.setFrameShape(QFrame.StyledPanel)
        self.frame_77.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_77)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.label_86 = QLabel(self.frame_77)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setFont(font1)
        self.label_86.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_42.addWidget(self.label_86)


        self.horizontalLayout_41.addWidget(self.frame_77)

        self.frame_78 = QFrame(self.frame_76)
        self.frame_78.setObjectName(u"frame_78")
        sizePolicy1.setHeightForWidth(self.frame_78.sizePolicy().hasHeightForWidth())
        self.frame_78.setSizePolicy(sizePolicy1)
        self.frame_78.setStyleSheet(u"background-color:transparent;\n"
"border-radius:10px;")
        self.frame_78.setFrameShape(QFrame.StyledPanel)
        self.frame_78.setFrameShadow(QFrame.Raised)
        self.verticalLayout_81 = QVBoxLayout(self.frame_78)
        self.verticalLayout_81.setSpacing(12)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.pushButton_44 = QPushButton(self.frame_78)
        self.pushButton_44.setObjectName(u"pushButton_44")
        sizePolicy11 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.pushButton_44.sizePolicy().hasHeightForWidth())
        self.pushButton_44.setSizePolicy(sizePolicy11)
        self.pushButton_44.setMinimumSize(QSize(50, 20))
        self.pushButton_44.setFont(font8)
        self.pushButton_44.setStyleSheet(u"background-color: #351c75;\n"
"border-radius:10px;")

        self.verticalLayout_81.addWidget(self.pushButton_44)

        self.pushButton_45 = QPushButton(self.frame_78)
        self.pushButton_45.setObjectName(u"pushButton_45")
        sizePolicy11.setHeightForWidth(self.pushButton_45.sizePolicy().hasHeightForWidth())
        self.pushButton_45.setSizePolicy(sizePolicy11)
        self.pushButton_45.setMinimumSize(QSize(50, 20))
        self.pushButton_45.setFont(font8)
        self.pushButton_45.setStyleSheet(u"background-color: #351c75;\n"
"border-radius:10px;")

        self.verticalLayout_81.addWidget(self.pushButton_45)


        self.horizontalLayout_41.addWidget(self.frame_78)


        self.horizontalLayout_53.addWidget(self.frame_76)

        self.frame_91 = QFrame(self.frame_13)
        self.frame_91.setObjectName(u"frame_91")
        self.frame_91.setStyleSheet(u"background-color:transparent;")
        self.frame_91.setFrameShape(QFrame.StyledPanel)
        self.frame_91.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.frame_91)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.frame_92 = QFrame(self.frame_91)
        self.frame_92.setObjectName(u"frame_92")
        self.frame_92.setStyleSheet(u"background-color: rgb(255, 0, 127);")
        self.frame_92.setFrameShape(QFrame.StyledPanel)
        self.frame_92.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.frame_92)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.label_91 = QLabel(self.frame_92)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setFont(font1)
        self.label_91.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_52.addWidget(self.label_91)


        self.horizontalLayout_51.addWidget(self.frame_92)

        self.frame_93 = QFrame(self.frame_91)
        self.frame_93.setObjectName(u"frame_93")
        self.frame_93.setStyleSheet(u"background-color:transparent;\n"
"border-radius:10px;")
        self.frame_93.setFrameShape(QFrame.StyledPanel)
        self.frame_93.setFrameShadow(QFrame.Raised)
        self.verticalLayout_86 = QVBoxLayout(self.frame_93)
        self.verticalLayout_86.setSpacing(12)
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")
        self.pushButton_54 = QPushButton(self.frame_93)
        self.pushButton_54.setObjectName(u"pushButton_54")
        sizePolicy11.setHeightForWidth(self.pushButton_54.sizePolicy().hasHeightForWidth())
        self.pushButton_54.setSizePolicy(sizePolicy11)
        self.pushButton_54.setMinimumSize(QSize(50, 20))
        self.pushButton_54.setFont(font8)
        self.pushButton_54.setStyleSheet(u"background-color: #351c75;\n"
"border-radius:10px;")

        self.verticalLayout_86.addWidget(self.pushButton_54)

        self.pushButton_55 = QPushButton(self.frame_93)
        self.pushButton_55.setObjectName(u"pushButton_55")
        sizePolicy11.setHeightForWidth(self.pushButton_55.sizePolicy().hasHeightForWidth())
        self.pushButton_55.setSizePolicy(sizePolicy11)
        self.pushButton_55.setMinimumSize(QSize(50, 20))
        self.pushButton_55.setFont(font8)
        self.pushButton_55.setStyleSheet(u"background-color: #351c75;\n"
"border-radius:10px;")

        self.verticalLayout_86.addWidget(self.pushButton_55)


        self.horizontalLayout_51.addWidget(self.frame_93)


        self.horizontalLayout_53.addWidget(self.frame_91)

        self.frame_88 = QFrame(self.frame_13)
        self.frame_88.setObjectName(u"frame_88")
        self.frame_88.setStyleSheet(u"background-color:transparent;")
        self.frame_88.setFrameShape(QFrame.StyledPanel)
        self.frame_88.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.frame_88)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.frame_89 = QFrame(self.frame_88)
        self.frame_89.setObjectName(u"frame_89")
        self.frame_89.setStyleSheet(u"background-color: rgb(255, 0, 127);")
        self.frame_89.setFrameShape(QFrame.StyledPanel)
        self.frame_89.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.frame_89)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.label_90 = QLabel(self.frame_89)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setFont(font1)
        self.label_90.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_50.addWidget(self.label_90)


        self.horizontalLayout_49.addWidget(self.frame_89)

        self.frame_90 = QFrame(self.frame_88)
        self.frame_90.setObjectName(u"frame_90")
        self.frame_90.setMinimumSize(QSize(60, 0))
        self.frame_90.setStyleSheet(u"background-color:transparent;\n"
"border-radius:10px;")
        self.frame_90.setFrameShape(QFrame.StyledPanel)
        self.frame_90.setFrameShadow(QFrame.Raised)
        self.verticalLayout_85 = QVBoxLayout(self.frame_90)
        self.verticalLayout_85.setSpacing(12)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.pushButton_52 = QPushButton(self.frame_90)
        self.pushButton_52.setObjectName(u"pushButton_52")
        sizePolicy11.setHeightForWidth(self.pushButton_52.sizePolicy().hasHeightForWidth())
        self.pushButton_52.setSizePolicy(sizePolicy11)
        self.pushButton_52.setMinimumSize(QSize(50, 20))
        self.pushButton_52.setFont(font8)
        self.pushButton_52.setStyleSheet(u"background-color: #351c75;\n"
"border-radius:10px;")

        self.verticalLayout_85.addWidget(self.pushButton_52, 0, Qt.AlignHCenter)

        self.pushButton_53 = QPushButton(self.frame_90)
        self.pushButton_53.setObjectName(u"pushButton_53")
        sizePolicy11.setHeightForWidth(self.pushButton_53.sizePolicy().hasHeightForWidth())
        self.pushButton_53.setSizePolicy(sizePolicy11)
        self.pushButton_53.setMinimumSize(QSize(50, 20))
        self.pushButton_53.setFont(font8)
        self.pushButton_53.setStyleSheet(u"background-color: #351c75;\n"
"border-radius:10px;")

        self.verticalLayout_85.addWidget(self.pushButton_53, 0, Qt.AlignHCenter)


        self.horizontalLayout_49.addWidget(self.frame_90)


        self.horizontalLayout_53.addWidget(self.frame_88)

        self.frame_85 = QFrame(self.frame_13)
        self.frame_85.setObjectName(u"frame_85")
        self.frame_85.setStyleSheet(u"background-color:transparent;")
        self.frame_85.setFrameShape(QFrame.StyledPanel)
        self.frame_85.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.frame_85)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.frame_86 = QFrame(self.frame_85)
        self.frame_86.setObjectName(u"frame_86")
        self.frame_86.setStyleSheet(u"background-color: rgb(255, 0, 127);")
        self.frame_86.setFrameShape(QFrame.StyledPanel)
        self.frame_86.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.frame_86)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.label_89 = QLabel(self.frame_86)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setFont(font1)
        self.label_89.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_48.addWidget(self.label_89)


        self.horizontalLayout_47.addWidget(self.frame_86)

        self.frame_87 = QFrame(self.frame_85)
        self.frame_87.setObjectName(u"frame_87")
        self.frame_87.setStyleSheet(u"background-color:transparent;\n"
"border-radius:10px;")
        self.frame_87.setFrameShape(QFrame.StyledPanel)
        self.frame_87.setFrameShadow(QFrame.Raised)
        self.verticalLayout_84 = QVBoxLayout(self.frame_87)
        self.verticalLayout_84.setSpacing(12)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.pushButton_50 = QPushButton(self.frame_87)
        self.pushButton_50.setObjectName(u"pushButton_50")
        sizePolicy11.setHeightForWidth(self.pushButton_50.sizePolicy().hasHeightForWidth())
        self.pushButton_50.setSizePolicy(sizePolicy11)
        self.pushButton_50.setMinimumSize(QSize(50, 20))
        self.pushButton_50.setFont(font8)
        self.pushButton_50.setStyleSheet(u"background-color: #351c75;\n"
"border-radius:10px;")

        self.verticalLayout_84.addWidget(self.pushButton_50)

        self.pushButton_51 = QPushButton(self.frame_87)
        self.pushButton_51.setObjectName(u"pushButton_51")
        sizePolicy11.setHeightForWidth(self.pushButton_51.sizePolicy().hasHeightForWidth())
        self.pushButton_51.setSizePolicy(sizePolicy11)
        self.pushButton_51.setMinimumSize(QSize(50, 20))
        self.pushButton_51.setFont(font8)
        self.pushButton_51.setStyleSheet(u"background-color: #351c75;\n"
"border-radius:10px;")

        self.verticalLayout_84.addWidget(self.pushButton_51)


        self.horizontalLayout_47.addWidget(self.frame_87)


        self.horizontalLayout_53.addWidget(self.frame_85)

        self.frame_82 = QFrame(self.frame_13)
        self.frame_82.setObjectName(u"frame_82")
        sizePolicy5.setHeightForWidth(self.frame_82.sizePolicy().hasHeightForWidth())
        self.frame_82.setSizePolicy(sizePolicy5)
        self.frame_82.setStyleSheet(u"background-color:transparent;")
        self.frame_82.setFrameShape(QFrame.StyledPanel)
        self.frame_82.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.frame_82)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.frame_83 = QFrame(self.frame_82)
        self.frame_83.setObjectName(u"frame_83")
        self.frame_83.setStyleSheet(u"background-color: rgb(255, 0, 127);")
        self.frame_83.setFrameShape(QFrame.StyledPanel)
        self.frame_83.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.frame_83)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.label_88 = QLabel(self.frame_83)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setFont(font1)
        self.label_88.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_46.addWidget(self.label_88)


        self.horizontalLayout_45.addWidget(self.frame_83)

        self.frame_84 = QFrame(self.frame_82)
        self.frame_84.setObjectName(u"frame_84")
        self.frame_84.setStyleSheet(u"background-color:transparent;\n"
"border-radius:10px;")
        self.frame_84.setFrameShape(QFrame.StyledPanel)
        self.frame_84.setFrameShadow(QFrame.Raised)
        self.verticalLayout_83 = QVBoxLayout(self.frame_84)
        self.verticalLayout_83.setSpacing(12)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.pushButton_48 = QPushButton(self.frame_84)
        self.pushButton_48.setObjectName(u"pushButton_48")
        sizePolicy11.setHeightForWidth(self.pushButton_48.sizePolicy().hasHeightForWidth())
        self.pushButton_48.setSizePolicy(sizePolicy11)
        self.pushButton_48.setMinimumSize(QSize(50, 20))
        self.pushButton_48.setFont(font8)
        self.pushButton_48.setStyleSheet(u"background-color: #351c75;\n"
"border-radius:10px;")

        self.verticalLayout_83.addWidget(self.pushButton_48)

        self.pushButton_49 = QPushButton(self.frame_84)
        self.pushButton_49.setObjectName(u"pushButton_49")
        sizePolicy11.setHeightForWidth(self.pushButton_49.sizePolicy().hasHeightForWidth())
        self.pushButton_49.setSizePolicy(sizePolicy11)
        self.pushButton_49.setMinimumSize(QSize(50, 20))
        self.pushButton_49.setFont(font8)
        self.pushButton_49.setStyleSheet(u"background-color: #351c75;\n"
"border-radius:10px;")

        self.verticalLayout_83.addWidget(self.pushButton_49)


        self.horizontalLayout_45.addWidget(self.frame_84)


        self.horizontalLayout_53.addWidget(self.frame_82)

        self.frame_79 = QFrame(self.frame_13)
        self.frame_79.setObjectName(u"frame_79")
        sizePolicy5.setHeightForWidth(self.frame_79.sizePolicy().hasHeightForWidth())
        self.frame_79.setSizePolicy(sizePolicy5)
        self.frame_79.setStyleSheet(u"background-color:transparent;")
        self.frame_79.setFrameShape(QFrame.StyledPanel)
        self.frame_79.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_79)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.frame_80 = QFrame(self.frame_79)
        self.frame_80.setObjectName(u"frame_80")
        self.frame_80.setStyleSheet(u"background-color: rgb(255, 0, 127);")
        self.frame_80.setFrameShape(QFrame.StyledPanel)
        self.frame_80.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_80)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.label_87 = QLabel(self.frame_80)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setFont(font1)
        self.label_87.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_44.addWidget(self.label_87)


        self.horizontalLayout_43.addWidget(self.frame_80)

        self.frame_81 = QFrame(self.frame_79)
        self.frame_81.setObjectName(u"frame_81")
        self.frame_81.setStyleSheet(u"background-color:transparent;\n"
"border-radius:10px;")
        self.frame_81.setFrameShape(QFrame.StyledPanel)
        self.frame_81.setFrameShadow(QFrame.Raised)
        self.verticalLayout_82 = QVBoxLayout(self.frame_81)
        self.verticalLayout_82.setSpacing(12)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.pushButton_46 = QPushButton(self.frame_81)
        self.pushButton_46.setObjectName(u"pushButton_46")
        sizePolicy11.setHeightForWidth(self.pushButton_46.sizePolicy().hasHeightForWidth())
        self.pushButton_46.setSizePolicy(sizePolicy11)
        self.pushButton_46.setMinimumSize(QSize(50, 20))
        self.pushButton_46.setFont(font8)
        self.pushButton_46.setStyleSheet(u"background-color: #351c75;\n"
"border-radius:10px;")

        self.verticalLayout_82.addWidget(self.pushButton_46)

        self.pushButton_47 = QPushButton(self.frame_81)
        self.pushButton_47.setObjectName(u"pushButton_47")
        sizePolicy11.setHeightForWidth(self.pushButton_47.sizePolicy().hasHeightForWidth())
        self.pushButton_47.setSizePolicy(sizePolicy11)
        self.pushButton_47.setMinimumSize(QSize(50, 20))
        self.pushButton_47.setFont(font8)
        self.pushButton_47.setStyleSheet(u"background-color: #351c75;\n"
"border-radius:10px;")

        self.verticalLayout_82.addWidget(self.pushButton_47)


        self.horizontalLayout_43.addWidget(self.frame_81)


        self.horizontalLayout_53.addWidget(self.frame_79)


        self.verticalLayout_29.addWidget(self.frame_13, 0, Qt.AlignTop)

        self.frame_12 = QFrame(self.frame_10)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy8.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy8)
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.trading_charts_cont = QGridLayout(self.frame_12)
        self.trading_charts_cont.setObjectName(u"trading_charts_cont")

        self.verticalLayout_29.addWidget(self.frame_12)


        self.verticalLayout_18.addWidget(self.frame_10)

        self.mainPages.addWidget(self.trade_page)
        self.mining_page = QWidget()
        self.mining_page.setObjectName(u"mining_page")
        self.verticalLayout_21 = QVBoxLayout(self.mining_page)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.progressBarContainer = QFrame(self.mining_page)
        self.progressBarContainer.setObjectName(u"progressBarContainer")
        self.progressBarContainer.setFrameShape(QFrame.StyledPanel)
        self.progressBarContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.progressBarContainer)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.progressBar = roundProgressBar(self.progressBarContainer)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(250, 250))
        self.progressBar.setMaximumSize(QSize(400, 400))

        self.verticalLayout_27.addWidget(self.progressBar)

        self.start_stopBtn = QPushButton(self.progressBarContainer)
        self.start_stopBtn.setObjectName(u"start_stopBtn")
        sizePolicy6.setHeightForWidth(self.start_stopBtn.sizePolicy().hasHeightForWidth())
        self.start_stopBtn.setSizePolicy(sizePolicy6)
        self.start_stopBtn.setMinimumSize(QSize(100, 30))
        self.start_stopBtn.setFont(font1)

        self.verticalLayout_27.addWidget(self.start_stopBtn, 0, Qt.AlignHCenter)


        self.verticalLayout_21.addWidget(self.progressBarContainer, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.cpu_freq_label = QLabel(self.mining_page)
        self.cpu_freq_label.setObjectName(u"cpu_freq_label")
        sizePolicy6.setHeightForWidth(self.cpu_freq_label.sizePolicy().hasHeightForWidth())
        self.cpu_freq_label.setSizePolicy(sizePolicy6)
        self.cpu_freq_label.setMinimumSize(QSize(30, 30))
        font14 = QFont()
        font14.setFamily(u"Segoe UI")
        font14.setPointSize(12)
        font14.setBold(True)
        font14.setWeight(75)
        self.cpu_freq_label.setFont(font14)
        self.cpu_freq_label.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_21.addWidget(self.cpu_freq_label)

        self.cpu_processors_label = QLabel(self.mining_page)
        self.cpu_processors_label.setObjectName(u"cpu_processors_label")
        sizePolicy6.setHeightForWidth(self.cpu_processors_label.sizePolicy().hasHeightForWidth())
        self.cpu_processors_label.setSizePolicy(sizePolicy6)
        self.cpu_processors_label.setMinimumSize(QSize(30, 30))
        self.cpu_processors_label.setFont(font14)
        self.cpu_processors_label.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.cpu_processors_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_21.addWidget(self.cpu_processors_label)

        self.mainPages.addWidget(self.mining_page)
        self.nfts_page = QWidget()
        self.nfts_page.setObjectName(u"nfts_page")
        self.nfts_page.setStyleSheet(u"background-color:#1f232a;")
        self.verticalLayout_22 = QVBoxLayout(self.nfts_page)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_16 = QLabel(self.nfts_page)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font2)
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_16)

        self.scrollArea = QScrollArea(self.nfts_page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFont(font3)
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 648, 966))
        self.verticalLayout_28 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.widget = QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(15)
        self.frame_28 = QFrame(self.widget)
        self.frame_28.setObjectName(u"frame_28")
        sizePolicy1.setHeightForWidth(self.frame_28.sizePolicy().hasHeightForWidth())
        self.frame_28.setSizePolicy(sizePolicy1)
        self.frame_28.setMinimumSize(QSize(0, 0))
        self.frame_28.setMaximumSize(QSize(200, 300))
        self.frame_28.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(255, 0, 127);")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_28)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.label_56 = QLabel(self.frame_28)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setPixmap(QPixmap(u"images/intel.png"))
        self.label_56.setScaledContents(True)

        self.verticalLayout_46.addWidget(self.label_56)

        self.pushButton_15 = QPushButton(self.frame_28)
        self.pushButton_15.setObjectName(u"pushButton_15")
        sizePolicy6.setHeightForWidth(self.pushButton_15.sizePolicy().hasHeightForWidth())
        self.pushButton_15.setSizePolicy(sizePolicy6)
        self.pushButton_15.setMinimumSize(QSize(60, 30))
        self.pushButton_15.setFont(font8)
        self.pushButton_15.setStyleSheet(u"background-color:#351c75;\n"
"border-radius:10px;")
        icon44 = QIcon()
        icon44.addFile(u":/icons/icons/slack.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_15.setIcon(icon44)

        self.verticalLayout_46.addWidget(self.pushButton_15, 0, Qt.AlignHCenter)


        self.gridLayout_2.addWidget(self.frame_28, 0, 0, 1, 1)

        self.frame_15 = QFrame(self.widget)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy1.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy1)
        self.frame_15.setMinimumSize(QSize(0, 0))
        self.frame_15.setMaximumSize(QSize(200, 300))
        self.frame_15.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(255, 0, 127);")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_15)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.label_35 = QLabel(self.frame_15)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setPixmap(QPixmap(u"images/intel.png"))
        self.label_35.setScaledContents(True)

        self.verticalLayout_33.addWidget(self.label_35)

        self.pushButton_4 = QPushButton(self.frame_15)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy6.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy6)
        self.pushButton_4.setMinimumSize(QSize(60, 30))
        self.pushButton_4.setFont(font8)
        self.pushButton_4.setStyleSheet(u"background-color:#351c75;\n"
"border-radius:10px;")
        self.pushButton_4.setIcon(icon44)

        self.verticalLayout_33.addWidget(self.pushButton_4, 0, Qt.AlignHCenter)


        self.gridLayout_2.addWidget(self.frame_15, 0, 1, 1, 1)

        self.frame_16 = QFrame(self.widget)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMaximumSize(QSize(200, 300))
        self.frame_16.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(255, 0, 127);")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_16)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.label_34 = QLabel(self.frame_16)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setPixmap(QPixmap(u"images/intel.png"))
        self.label_34.setScaledContents(True)

        self.verticalLayout_34.addWidget(self.label_34)

        self.pushButton_7 = QPushButton(self.frame_16)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy6.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy6)
        self.pushButton_7.setMinimumSize(QSize(60, 30))
        self.pushButton_7.setFont(font8)
        self.pushButton_7.setStyleSheet(u"background-color:#351c75;\n"
"border-radius:10px;")
        self.pushButton_7.setIcon(icon44)

        self.verticalLayout_34.addWidget(self.pushButton_7, 0, Qt.AlignHCenter)


        self.gridLayout_2.addWidget(self.frame_16, 0, 2, 1, 1)

        self.frame_54 = QFrame(self.widget)
        self.frame_54.setObjectName(u"frame_54")
        sizePolicy1.setHeightForWidth(self.frame_54.sizePolicy().hasHeightForWidth())
        self.frame_54.setSizePolicy(sizePolicy1)
        self.frame_54.setMinimumSize(QSize(0, 0))
        self.frame_54.setMaximumSize(QSize(200, 300))
        self.frame_54.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(255, 0, 127);")
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.verticalLayout_73 = QVBoxLayout(self.frame_54)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.label_58 = QLabel(self.frame_54)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setPixmap(QPixmap(u"images/intel.png"))
        self.label_58.setScaledContents(True)

        self.verticalLayout_73.addWidget(self.label_58)

        self.pushButton_30 = QPushButton(self.frame_54)
        self.pushButton_30.setObjectName(u"pushButton_30")
        sizePolicy6.setHeightForWidth(self.pushButton_30.sizePolicy().hasHeightForWidth())
        self.pushButton_30.setSizePolicy(sizePolicy6)
        self.pushButton_30.setMinimumSize(QSize(60, 30))
        self.pushButton_30.setFont(font8)
        self.pushButton_30.setStyleSheet(u"background-color:#351c75;\n"
"border-radius:10px;")
        self.pushButton_30.setIcon(icon44)

        self.verticalLayout_73.addWidget(self.pushButton_30, 0, Qt.AlignHCenter)


        self.gridLayout_2.addWidget(self.frame_54, 1, 0, 1, 1)

        self.frame_51 = QFrame(self.widget)
        self.frame_51.setObjectName(u"frame_51")
        sizePolicy1.setHeightForWidth(self.frame_51.sizePolicy().hasHeightForWidth())
        self.frame_51.setSizePolicy(sizePolicy1)
        self.frame_51.setMinimumSize(QSize(0, 0))
        self.frame_51.setMaximumSize(QSize(200, 300))
        self.frame_51.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(255, 0, 127);")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.verticalLayout_70 = QVBoxLayout(self.frame_51)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.label_57 = QLabel(self.frame_51)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setPixmap(QPixmap(u"images/intel.png"))
        self.label_57.setScaledContents(True)

        self.verticalLayout_70.addWidget(self.label_57)

        self.pushButton_16 = QPushButton(self.frame_51)
        self.pushButton_16.setObjectName(u"pushButton_16")
        sizePolicy6.setHeightForWidth(self.pushButton_16.sizePolicy().hasHeightForWidth())
        self.pushButton_16.setSizePolicy(sizePolicy6)
        self.pushButton_16.setMinimumSize(QSize(60, 30))
        self.pushButton_16.setFont(font8)
        self.pushButton_16.setStyleSheet(u"background-color:#351c75;\n"
"border-radius:10px;")
        self.pushButton_16.setIcon(icon44)

        self.verticalLayout_70.addWidget(self.pushButton_16, 0, Qt.AlignHCenter)


        self.gridLayout_2.addWidget(self.frame_51, 1, 1, 1, 1)

        self.frame_27 = QFrame(self.widget)
        self.frame_27.setObjectName(u"frame_27")
        sizePolicy1.setHeightForWidth(self.frame_27.sizePolicy().hasHeightForWidth())
        self.frame_27.setSizePolicy(sizePolicy1)
        self.frame_27.setMinimumSize(QSize(0, 0))
        self.frame_27.setMaximumSize(QSize(200, 300))
        self.frame_27.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(255, 0, 127);")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_27)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.label_53 = QLabel(self.frame_27)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setPixmap(QPixmap(u"images/intel.png"))
        self.label_53.setScaledContents(True)

        self.verticalLayout_45.addWidget(self.label_53)

        self.pushButton_6 = QPushButton(self.frame_27)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy6.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy6)
        self.pushButton_6.setMinimumSize(QSize(60, 30))
        self.pushButton_6.setFont(font8)
        self.pushButton_6.setStyleSheet(u"background-color:#351c75;\n"
"border-radius:10px;")
        self.pushButton_6.setIcon(icon44)

        self.verticalLayout_45.addWidget(self.pushButton_6, 0, Qt.AlignHCenter)


        self.gridLayout_2.addWidget(self.frame_27, 1, 2, 1, 1)

        self.frame_11 = QFrame(self.widget)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(200, 300))
        self.frame_11.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(255, 0, 127);")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_11)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label_36 = QLabel(self.frame_11)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setPixmap(QPixmap(u"images/intel.png"))
        self.label_36.setScaledContents(True)

        self.verticalLayout_30.addWidget(self.label_36)

        self.pushButton = QPushButton(self.frame_11)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy6.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy6)
        self.pushButton.setMinimumSize(QSize(60, 30))
        self.pushButton.setFont(font8)
        self.pushButton.setStyleSheet(u"background-color:#351c75;\n"
"border-radius:10px;")
        self.pushButton.setIcon(icon44)

        self.verticalLayout_30.addWidget(self.pushButton, 0, Qt.AlignHCenter)


        self.gridLayout_2.addWidget(self.frame_11, 2, 0, 1, 1)


        self.verticalLayout_28.addWidget(self.widget)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_22.addWidget(self.scrollArea)

        self.mainPages.addWidget(self.nfts_page)
        self.nftsMarketplacePage = QWidget()
        self.nftsMarketplacePage.setObjectName(u"nftsMarketplacePage")
        self.nftsMarketplacePage.setStyleSheet(u"background-color:#1f232a;")
        self.verticalLayout_43 = QVBoxLayout(self.nftsMarketplacePage)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.label_80 = QLabel(self.nftsMarketplacePage)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setFont(font2)
        self.label_80.setAlignment(Qt.AlignCenter)

        self.verticalLayout_43.addWidget(self.label_80)

        self.scrollArea_2 = QScrollArea(self.nftsMarketplacePage)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setFont(font3)
        self.scrollArea_2.setFrameShape(QFrame.NoFrame)
        self.scrollArea_2.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 648, 1596))
        self.verticalLayout_36 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.widget_2 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"background-color:#1f232a;")
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(15)
        self.frame_17 = QFrame(self.widget_2)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(200, 300))
        self.frame_17.setStyleSheet(u"border-radius:10px;\n"
"background-color: #351c75;")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_17)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.label_38 = QLabel(self.frame_17)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setPixmap(QPixmap(u"images/intel.png"))
        self.label_38.setScaledContents(True)

        self.verticalLayout_37.addWidget(self.label_38)

        self.pushButton_10 = QPushButton(self.frame_17)
        self.pushButton_10.setObjectName(u"pushButton_10")
        sizePolicy6.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy6)
        self.pushButton_10.setMinimumSize(QSize(60, 30))
        self.pushButton_10.setFont(font8)
        self.pushButton_10.setStyleSheet(u"background-color:#351c75;\n"
"border-radius:10px;")
        icon45 = QIcon()
        icon45.addFile(u":/icons/icons/box.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_10.setIcon(icon45)

        self.verticalLayout_37.addWidget(self.pushButton_10, 0, Qt.AlignHCenter)


        self.gridLayout.addWidget(self.frame_17, 0, 0, 1, 1)

        self.frame_18 = QFrame(self.widget_2)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMaximumSize(QSize(200, 300))
        self.frame_18.setStyleSheet(u"border-radius:10px;\n"
"background-color: #351c75;")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_18)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.label_39 = QLabel(self.frame_18)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setPixmap(QPixmap(u"images/intel.png"))
        self.label_39.setScaledContents(True)

        self.verticalLayout_38.addWidget(self.label_39)

        self.pushButton_11 = QPushButton(self.frame_18)
        self.pushButton_11.setObjectName(u"pushButton_11")
        sizePolicy6.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy6)
        self.pushButton_11.setMinimumSize(QSize(60, 30))
        self.pushButton_11.setFont(font8)
        self.pushButton_11.setStyleSheet(u"background-color:#351c75;\n"
"border-radius:10px;")
        self.pushButton_11.setIcon(icon45)

        self.verticalLayout_38.addWidget(self.pushButton_11, 0, Qt.AlignHCenter)


        self.gridLayout.addWidget(self.frame_18, 0, 1, 1, 1)

        self.frame_19 = QFrame(self.widget_2)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMaximumSize(QSize(200, 300))
        self.frame_19.setStyleSheet(u"border-radius:10px;\n"
"background-color: #351c75;")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_19)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.label_40 = QLabel(self.frame_19)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setPixmap(QPixmap(u"images/intel.png"))
        self.label_40.setScaledContents(True)

        self.verticalLayout_39.addWidget(self.label_40)

        self.pushButton_12 = QPushButton(self.frame_19)
        self.pushButton_12.setObjectName(u"pushButton_12")
        sizePolicy6.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy6)
        self.pushButton_12.setMinimumSize(QSize(60, 30))
        self.pushButton_12.setFont(font8)
        self.pushButton_12.setStyleSheet(u"background-color:#351c75;\n"
"border-radius:10px;")
        self.pushButton_12.setIcon(icon45)

        self.verticalLayout_39.addWidget(self.pushButton_12, 0, Qt.AlignHCenter)


        self.gridLayout.addWidget(self.frame_19, 0, 3, 1, 1)

        self.frame_24 = QFrame(self.widget_2)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setMaximumSize(QSize(200, 300))
        self.frame_24.setStyleSheet(u"border-radius:10px;\n"
"background-color: #351c75;")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_64 = QVBoxLayout(self.frame_24)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.label_47 = QLabel(self.frame_24)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setPixmap(QPixmap(u"images/intel.png"))
        self.label_47.setScaledContents(True)

        self.verticalLayout_64.addWidget(self.label_47)

        self.pushButton_24 = QPushButton(self.frame_24)
        self.pushButton_24.setObjectName(u"pushButton_24")
        sizePolicy6.setHeightForWidth(self.pushButton_24.sizePolicy().hasHeightForWidth())
        self.pushButton_24.setSizePolicy(sizePolicy6)
        self.pushButton_24.setMinimumSize(QSize(60, 30))
        self.pushButton_24.setFont(font8)
        self.pushButton_24.setStyleSheet(u"background-color:#351c75;\n"
"border-radius:10px;")

        self.verticalLayout_64.addWidget(self.pushButton_24, 0, Qt.AlignHCenter)


        self.gridLayout.addWidget(self.frame_24, 1, 0, 1, 1)

        self.frame_25 = QFrame(self.widget_2)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMaximumSize(QSize(200, 300))
        self.frame_25.setStyleSheet(u"border-radius:10px;\n"
"background-color: #351c75;")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_65 = QVBoxLayout(self.frame_25)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.label_48 = QLabel(self.frame_25)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setPixmap(QPixmap(u"images/intel.png"))
        self.label_48.setScaledContents(True)

        self.verticalLayout_65.addWidget(self.label_48)

        self.pushButton_25 = QPushButton(self.frame_25)
        self.pushButton_25.setObjectName(u"pushButton_25")
        sizePolicy6.setHeightForWidth(self.pushButton_25.sizePolicy().hasHeightForWidth())
        self.pushButton_25.setSizePolicy(sizePolicy6)
        self.pushButton_25.setMinimumSize(QSize(60, 30))
        self.pushButton_25.setFont(font8)
        self.pushButton_25.setStyleSheet(u"background-color:#351c75;\n"
"border-radius:10px;")

        self.verticalLayout_65.addWidget(self.pushButton_25, 0, Qt.AlignHCenter)


        self.gridLayout.addWidget(self.frame_25, 1, 1, 1, 1)

        self.frame_23 = QFrame(self.widget_2)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setMaximumSize(QSize(200, 300))
        self.frame_23.setStyleSheet(u"border-radius:10px;\n"
"background-color: #351c75;")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_63 = QVBoxLayout(self.frame_23)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.label_46 = QLabel(self.frame_23)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setPixmap(QPixmap(u"images/intel.png"))
        self.label_46.setScaledContents(True)

        self.verticalLayout_63.addWidget(self.label_46)

        self.pushButton_23 = QPushButton(self.frame_23)
        self.pushButton_23.setObjectName(u"pushButton_23")
        sizePolicy6.setHeightForWidth(self.pushButton_23.sizePolicy().hasHeightForWidth())
        self.pushButton_23.setSizePolicy(sizePolicy6)
        self.pushButton_23.setMinimumSize(QSize(60, 30))
        self.pushButton_23.setFont(font8)
        self.pushButton_23.setStyleSheet(u"background-color:#351c75;\n"
"border-radius:10px;")
        self.pushButton_23.setIcon(icon45)

        self.verticalLayout_63.addWidget(self.pushButton_23, 0, Qt.AlignHCenter)


        self.gridLayout.addWidget(self.frame_23, 1, 3, 1, 1)

        self.frame_50 = QFrame(self.widget_2)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setMaximumSize(QSize(200, 300))
        self.frame_50.setStyleSheet(u"border-radius:10px;\n"
"background-color: #351c75;")
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.verticalLayout_69 = QVBoxLayout(self.frame_50)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.label_52 = QLabel(self.frame_50)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setPixmap(QPixmap(u"images/intel.png"))
        self.label_52.setScaledContents(True)

        self.verticalLayout_69.addWidget(self.label_52)

        self.pushButton_29 = QPushButton(self.frame_50)
        self.pushButton_29.setObjectName(u"pushButton_29")
        sizePolicy6.setHeightForWidth(self.pushButton_29.sizePolicy().hasHeightForWidth())
        self.pushButton_29.setSizePolicy(sizePolicy6)
        self.pushButton_29.setMinimumSize(QSize(60, 30))
        self.pushButton_29.setFont(font8)
        self.pushButton_29.setStyleSheet(u"background-color:#351c75;\n"
"border-radius:10px;")
        self.pushButton_29.setIcon(icon45)

        self.verticalLayout_69.addWidget(self.pushButton_29)


        self.gridLayout.addWidget(self.frame_50, 2, 0, 1, 1)

        self.frame_48 = QFrame(self.widget_2)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setMaximumSize(QSize(200, 300))
        self.frame_48.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(255, 0, 127);")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.verticalLayout_67 = QVBoxLayout(self.frame_48)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.label_50 = QLabel(self.frame_48)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setPixmap(QPixmap(u"images/intel.png"))
        self.label_50.setScaledContents(True)

        self.verticalLayout_67.addWidget(self.label_50)

        self.pushButton_27 = QPushButton(self.frame_48)
        self.pushButton_27.setObjectName(u"pushButton_27")
        sizePolicy6.setHeightForWidth(self.pushButton_27.sizePolicy().hasHeightForWidth())
        self.pushButton_27.setSizePolicy(sizePolicy6)
        self.pushButton_27.setMinimumSize(QSize(60, 30))
        self.pushButton_27.setFont(font8)
        self.pushButton_27.setStyleSheet(u"background-color:#351c75;\n"
"border-radius:10px;")
        self.pushButton_27.setIcon(icon45)

        self.verticalLayout_67.addWidget(self.pushButton_27, 0, Qt.AlignHCenter)


        self.gridLayout.addWidget(self.frame_48, 2, 1, 1, 1)

        self.frame_53 = QFrame(self.widget_2)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setMaximumSize(QSize(200, 300))
        self.frame_53.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(255, 0, 127);")
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.verticalLayout_72 = QVBoxLayout(self.frame_53)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.label_55 = QLabel(self.frame_53)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setPixmap(QPixmap(u"images/intel.png"))
        self.label_55.setScaledContents(True)

        self.verticalLayout_72.addWidget(self.label_55)

        self.pushButton_32 = QPushButton(self.frame_53)
        self.pushButton_32.setObjectName(u"pushButton_32")
        sizePolicy6.setHeightForWidth(self.pushButton_32.sizePolicy().hasHeightForWidth())
        self.pushButton_32.setSizePolicy(sizePolicy6)
        self.pushButton_32.setMinimumSize(QSize(60, 30))
        self.pushButton_32.setFont(font8)
        self.pushButton_32.setStyleSheet(u"background-color:#351c75;\n"
"border-radius:10px;")
        self.pushButton_32.setIcon(icon45)

        self.verticalLayout_72.addWidget(self.pushButton_32, 0, Qt.AlignHCenter)


        self.gridLayout.addWidget(self.frame_53, 3, 0, 1, 1)

        self.frame_52 = QFrame(self.widget_2)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setMaximumSize(QSize(200, 300))
        self.frame_52.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(255, 0, 127);")
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.verticalLayout_71 = QVBoxLayout(self.frame_52)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.label_54 = QLabel(self.frame_52)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setPixmap(QPixmap(u"images/intel.png"))
        self.label_54.setScaledContents(True)

        self.verticalLayout_71.addWidget(self.label_54)

        self.pushButton_31 = QPushButton(self.frame_52)
        self.pushButton_31.setObjectName(u"pushButton_31")
        sizePolicy6.setHeightForWidth(self.pushButton_31.sizePolicy().hasHeightForWidth())
        self.pushButton_31.setSizePolicy(sizePolicy6)
        self.pushButton_31.setMinimumSize(QSize(60, 30))
        self.pushButton_31.setFont(font8)
        self.pushButton_31.setStyleSheet(u"background-color:#351c75;\n"
"border-radius:10px;")
        self.pushButton_31.setIcon(icon45)

        self.verticalLayout_71.addWidget(self.pushButton_31, 0, Qt.AlignHCenter)


        self.gridLayout.addWidget(self.frame_52, 3, 1, 1, 1)

        self.frame_21 = QFrame(self.widget_2)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMaximumSize(QSize(200, 300))
        self.frame_21.setStyleSheet(u"border-radius:10px;\n"
"background-color: #351c75;")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_21)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.label_42 = QLabel(self.frame_21)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setPixmap(QPixmap(u"images/intel.png"))
        self.label_42.setScaledContents(True)

        self.verticalLayout_41.addWidget(self.label_42)

        self.pushButton_14 = QPushButton(self.frame_21)
        self.pushButton_14.setObjectName(u"pushButton_14")
        sizePolicy6.setHeightForWidth(self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy6)
        self.pushButton_14.setMinimumSize(QSize(60, 30))
        self.pushButton_14.setFont(font8)
        self.pushButton_14.setStyleSheet(u"background-color:#351c75;\n"
"border-radius:10px;")
        self.pushButton_14.setIcon(icon45)

        self.verticalLayout_41.addWidget(self.pushButton_14, 0, Qt.AlignHCenter)


        self.gridLayout.addWidget(self.frame_21, 3, 3, 1, 1)

        self.frame_20 = QFrame(self.widget_2)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMaximumSize(QSize(200, 300))
        self.frame_20.setStyleSheet(u"border-radius:10px;\n"
"background-color: #351c75;")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_20)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.label_41 = QLabel(self.frame_20)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setPixmap(QPixmap(u"images/intel.png"))
        self.label_41.setScaledContents(True)

        self.verticalLayout_40.addWidget(self.label_41)

        self.pushButton_13 = QPushButton(self.frame_20)
        self.pushButton_13.setObjectName(u"pushButton_13")
        sizePolicy6.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy6)
        self.pushButton_13.setMinimumSize(QSize(60, 30))
        self.pushButton_13.setFont(font8)
        self.pushButton_13.setStyleSheet(u"background-color:#351c75;\n"
"border-radius:10px;")
        self.pushButton_13.setIcon(icon45)

        self.verticalLayout_40.addWidget(self.pushButton_13, 0, Qt.AlignHCenter)


        self.gridLayout.addWidget(self.frame_20, 4, 0, 1, 1)

        self.frame_26 = QFrame(self.widget_2)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMaximumSize(QSize(200, 300))
        self.frame_26.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(255, 0, 127);")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_66 = QVBoxLayout(self.frame_26)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.label_49 = QLabel(self.frame_26)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setPixmap(QPixmap(u"images/intel.png"))
        self.label_49.setScaledContents(True)

        self.verticalLayout_66.addWidget(self.label_49)

        self.pushButton_26 = QPushButton(self.frame_26)
        self.pushButton_26.setObjectName(u"pushButton_26")
        sizePolicy6.setHeightForWidth(self.pushButton_26.sizePolicy().hasHeightForWidth())
        self.pushButton_26.setSizePolicy(sizePolicy6)
        self.pushButton_26.setMinimumSize(QSize(60, 30))
        self.pushButton_26.setFont(font8)
        self.pushButton_26.setStyleSheet(u"background-color:#351c75;\n"
"border-radius:10px;")
        self.pushButton_26.setIcon(icon45)

        self.verticalLayout_66.addWidget(self.pushButton_26, 0, Qt.AlignHCenter)


        self.gridLayout.addWidget(self.frame_26, 4, 1, 1, 1)

        self.frame_22 = QFrame(self.widget_2)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMaximumSize(QSize(200, 300))
        self.frame_22.setStyleSheet(u"border-radius:10px;\n"
"background-color: #351c75;")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_22)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.label_43 = QLabel(self.frame_22)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setPixmap(QPixmap(u"images/intel.png"))
        self.label_43.setScaledContents(True)

        self.verticalLayout_42.addWidget(self.label_43)

        self.pushButton_18 = QPushButton(self.frame_22)
        self.pushButton_18.setObjectName(u"pushButton_18")
        sizePolicy6.setHeightForWidth(self.pushButton_18.sizePolicy().hasHeightForWidth())
        self.pushButton_18.setSizePolicy(sizePolicy6)
        self.pushButton_18.setMinimumSize(QSize(60, 30))
        self.pushButton_18.setFont(font8)
        self.pushButton_18.setStyleSheet(u"background-color:#351c75;\n"
"border-radius:10px;")
        self.pushButton_18.setIcon(icon45)

        self.verticalLayout_42.addWidget(self.pushButton_18, 0, Qt.AlignHCenter)


        self.gridLayout.addWidget(self.frame_22, 4, 3, 1, 1)

        self.frame_49 = QFrame(self.widget_2)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setMaximumSize(QSize(200, 300))
        self.frame_49.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(255, 0, 127);")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.verticalLayout_68 = QVBoxLayout(self.frame_49)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.label_51 = QLabel(self.frame_49)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setPixmap(QPixmap(u"images/intel.png"))
        self.label_51.setScaledContents(True)

        self.verticalLayout_68.addWidget(self.label_51)

        self.pushButton_28 = QPushButton(self.frame_49)
        self.pushButton_28.setObjectName(u"pushButton_28")
        sizePolicy6.setHeightForWidth(self.pushButton_28.sizePolicy().hasHeightForWidth())
        self.pushButton_28.setSizePolicy(sizePolicy6)
        self.pushButton_28.setMinimumSize(QSize(60, 30))
        self.pushButton_28.setFont(font8)
        self.pushButton_28.setStyleSheet(u"background-color:#351c75;\n"
"border-radius:10px;")
        self.pushButton_28.setIcon(icon45)

        self.verticalLayout_68.addWidget(self.pushButton_28, 0, Qt.AlignHCenter)


        self.gridLayout.addWidget(self.frame_49, 2, 3, 1, 1)


        self.verticalLayout_36.addWidget(self.widget_2)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_43.addWidget(self.scrollArea_2)

        self.mainPages.addWidget(self.nftsMarketplacePage)
        self.wallet_page = QWidget()
        self.wallet_page.setObjectName(u"wallet_page")
        self.frame_47 = QFrame(self.wallet_page)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setGeometry(QRect(-10, 10, 1370, 838))
        sizePolicy.setHeightForWidth(self.frame_47.sizePolicy().hasHeightForWidth())
        self.frame_47.setSizePolicy(sizePolicy)
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.frame_43 = QFrame(self.frame_47)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setGeometry(QRect(9, 9, 336, 143))
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.verticalLayout_61 = QVBoxLayout(self.frame_43)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.frame_44 = QFrame(self.frame_43)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.verticalLayout_59 = QVBoxLayout(self.frame_44)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(0, -1, -1, -1)
        self.frame_45 = QFrame(self.frame_44)
        self.frame_45.setObjectName(u"frame_45")
        sizePolicy9.setHeightForWidth(self.frame_45.sizePolicy().hasHeightForWidth())
        self.frame_45.setSizePolicy(sizePolicy9)
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.verticalLayout_60 = QVBoxLayout(self.frame_45)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.label_33 = QLabel(self.frame_45)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font7)

        self.verticalLayout_60.addWidget(self.label_33, 0, Qt.AlignTop)


        self.verticalLayout_59.addWidget(self.frame_45)

        self.frame_46 = QFrame(self.frame_44)
        self.frame_46.setObjectName(u"frame_46")
        sizePolicy6.setHeightForWidth(self.frame_46.sizePolicy().hasHeightForWidth())
        self.frame_46.setSizePolicy(sizePolicy6)
        self.frame_46.setMinimumSize(QSize(300, 50))
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.balanceLabel_2 = QLabel(self.frame_46)
        self.balanceLabel_2.setObjectName(u"balanceLabel_2")
        sizePolicy6.setHeightForWidth(self.balanceLabel_2.sizePolicy().hasHeightForWidth())
        self.balanceLabel_2.setSizePolicy(sizePolicy6)
        self.balanceLabel_2.setMinimumSize(QSize(200, 40))
        self.balanceLabel_2.setFont(font8)
        self.balanceLabel_2.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(255, 0, 127);")
        self.balanceLabel_2.setInputMethodHints(Qt.ImhHiddenText)
        self.balanceLabel_2.setFrameShape(QFrame.StyledPanel)
        self.balanceLabel_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_22.addWidget(self.balanceLabel_2)

        self.checkBalanceBtn_2 = QPushButton(self.frame_46)
        self.checkBalanceBtn_2.setObjectName(u"checkBalanceBtn_2")
        sizePolicy6.setHeightForWidth(self.checkBalanceBtn_2.sizePolicy().hasHeightForWidth())
        self.checkBalanceBtn_2.setSizePolicy(sizePolicy6)
        self.checkBalanceBtn_2.setMinimumSize(QSize(0, 40))
        icon46 = QIcon()
        icon46.addFile(u":/icons/icons/eye.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.checkBalanceBtn_2.setIcon(icon46)
        self.checkBalanceBtn_2.setIconSize(QSize(24, 24))
        self.checkBalanceBtn_2.setCheckable(False)
        self.checkBalanceBtn_2.setChecked(False)

        self.horizontalLayout_22.addWidget(self.checkBalanceBtn_2)


        self.verticalLayout_59.addWidget(self.frame_46)


        self.verticalLayout_61.addWidget(self.frame_44)

        self.frame_35 = QFrame(self.frame_47)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setGeometry(QRect(9, 158, 772, 319))
        sizePolicy12 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.frame_35.sizePolicy().hasHeightForWidth())
        self.frame_35.setSizePolicy(sizePolicy12)
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_31 = QFrame(self.frame_35)
        self.frame_31.setObjectName(u"frame_31")
        sizePolicy6.setHeightForWidth(self.frame_31.sizePolicy().hasHeightForWidth())
        self.frame_31.setSizePolicy(sizePolicy6)
        self.frame_31.setMinimumSize(QSize(0, 0))
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_31)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.frame_34 = QFrame(self.frame_31)
        self.frame_34.setObjectName(u"frame_34")
#if QT_CONFIG(tooltip)
        self.frame_34.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.frame_34)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.label_18 = QLabel(self.frame_34)
        self.label_18.setObjectName(u"label_18")
        font15 = QFont()
        font15.setPointSize(12)
        font15.setBold(True)
        font15.setWeight(75)
        self.label_18.setFont(font15)
#if QT_CONFIG(tooltip)
        self.label_18.setToolTip(u"")
#endif // QT_CONFIG(tooltip)

        self.verticalLayout_50.addWidget(self.label_18)

        self.label_12 = QLabel(self.frame_34)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font15)
        self.label_12.setToolTipDuration(-1)

        self.verticalLayout_50.addWidget(self.label_12)


        self.verticalLayout_47.addWidget(self.frame_34)

        self.inputFrame = QFrame(self.frame_31)
        self.inputFrame.setObjectName(u"inputFrame")
        sizePolicy.setHeightForWidth(self.inputFrame.sizePolicy().hasHeightForWidth())
        self.inputFrame.setSizePolicy(sizePolicy)
        self.inputFrame.setMinimumSize(QSize(0, 0))
        self.inputFrame.setFrameShape(QFrame.StyledPanel)
        self.inputFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.inputFrame)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.addressLine = QFrame(self.inputFrame)
        self.addressLine.setObjectName(u"addressLine")
        sizePolicy12.setHeightForWidth(self.addressLine.sizePolicy().hasHeightForWidth())
        self.addressLine.setSizePolicy(sizePolicy12)
        self.addressLine.setLayoutDirection(Qt.LeftToRight)
        self.addressLine.setFrameShape(QFrame.NoFrame)
        self.addressLine.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.addressLine)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.addressLineEdit = QLineEdit(self.addressLine)
        self.addressLineEdit.setObjectName(u"addressLineEdit")
        sizePolicy5.setHeightForWidth(self.addressLineEdit.sizePolicy().hasHeightForWidth())
        self.addressLineEdit.setSizePolicy(sizePolicy5)
        self.addressLineEdit.setMinimumSize(QSize(300, 40))
        self.addressLineEdit.setFont(font8)
        self.addressLineEdit.setStyleSheet(u"background-color: rgb(255, 0, 127);")

        self.gridLayout_5.addWidget(self.addressLineEdit, 0, 1, 1, 1)

        self.CertBtn_2 = QPushButton(self.addressLine)
        self.CertBtn_2.setObjectName(u"CertBtn_2")
        self.CertBtn_2.setStyleSheet(u"background-color:#1f232a;")
        icon47 = QIcon()
        icon47.addFile(u":/icons/icons/clipboard.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.CertBtn_2.setIcon(icon47)
        self.CertBtn_2.setIconSize(QSize(24, 24))

        self.gridLayout_5.addWidget(self.CertBtn_2, 0, 0, 1, 1, Qt.AlignHCenter)


        self.horizontalLayout_20.addLayout(self.gridLayout_5)


        self.verticalLayout_24.addWidget(self.addressLine)

        self.frame_36 = QFrame(self.inputFrame)
        self.frame_36.setObjectName(u"frame_36")
        sizePolicy8.setHeightForWidth(self.frame_36.sizePolicy().hasHeightForWidth())
        self.frame_36.setSizePolicy(sizePolicy8)
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_11 = QLabel(self.frame_36)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font15)

        self.horizontalLayout_29.addWidget(self.label_11, 0, Qt.AlignLeft|Qt.AlignBottom)


        self.verticalLayout_24.addWidget(self.frame_36, 0, Qt.AlignLeft|Qt.AlignBottom)

        self.amountLine = QFrame(self.inputFrame)
        self.amountLine.setObjectName(u"amountLine")
        sizePolicy1.setHeightForWidth(self.amountLine.sizePolicy().hasHeightForWidth())
        self.amountLine.setSizePolicy(sizePolicy1)
        self.amountLine.setMinimumSize(QSize(0, 0))
        self.amountLine.setMaximumSize(QSize(350, 50))
        self.amountLine.setLayoutDirection(Qt.LeftToRight)
        self.amountLine.setFrameShape(QFrame.NoFrame)
        self.amountLine.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.amountLine)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.amountLineEdit = QLineEdit(self.amountLine)
        self.amountLineEdit.setObjectName(u"amountLineEdit")
        sizePolicy5.setHeightForWidth(self.amountLineEdit.sizePolicy().hasHeightForWidth())
        self.amountLineEdit.setSizePolicy(sizePolicy5)
        self.amountLineEdit.setMinimumSize(QSize(300, 40))
        self.amountLineEdit.setFont(font8)
        self.amountLineEdit.setStyleSheet(u"background-color: rgb(255, 0, 127);")

        self.gridLayout_6.addWidget(self.amountLineEdit, 0, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.amountLine)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setIcon(icon45)
        self.pushButton_2.setIconSize(QSize(24, 24))

        self.gridLayout_6.addWidget(self.pushButton_2, 0, 0, 1, 1)


        self.horizontalLayout_23.addLayout(self.gridLayout_6)


        self.verticalLayout_24.addWidget(self.amountLine)


        self.verticalLayout_47.addWidget(self.inputFrame)

        self.btnFrame = QFrame(self.frame_31)
        self.btnFrame.setObjectName(u"btnFrame")
        self.btnFrame.setFrameShape(QFrame.StyledPanel)
        self.btnFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_54 = QVBoxLayout(self.btnFrame)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.receiveBtn = QPushButton(self.btnFrame)
        self.receiveBtn.setObjectName(u"receiveBtn")
        sizePolicy6.setHeightForWidth(self.receiveBtn.sizePolicy().hasHeightForWidth())
        self.receiveBtn.setSizePolicy(sizePolicy6)
        self.receiveBtn.setMinimumSize(QSize(200, 50))
        font16 = QFont()
        font16.setFamily(u"Segoe Print")
        font16.setPointSize(10)
        font16.setBold(True)
        font16.setWeight(75)
        self.receiveBtn.setFont(font16)
        self.receiveBtn.setStyleSheet(u"")

        self.verticalLayout_54.addWidget(self.receiveBtn)


        self.verticalLayout_47.addWidget(self.btnFrame)


        self.horizontalLayout_14.addWidget(self.frame_31)

        self.frame_40 = QFrame(self.frame_35)
        self.frame_40.setObjectName(u"frame_40")
        sizePolicy6.setHeightForWidth(self.frame_40.sizePolicy().hasHeightForWidth())
        self.frame_40.setSizePolicy(sizePolicy6)
        self.frame_40.setMinimumSize(QSize(200, 200))
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.verticalLayout_58 = QVBoxLayout(self.frame_40)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.frame_41 = QFrame(self.frame_40)
        self.frame_41.setObjectName(u"frame_41")
#if QT_CONFIG(tooltip)
        self.frame_41.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.frame_41)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.label_19 = QLabel(self.frame_41)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font15)
#if QT_CONFIG(tooltip)
        self.label_19.setToolTip(u"")
#endif // QT_CONFIG(tooltip)

        self.verticalLayout_55.addWidget(self.label_19)

        self.label_20 = QLabel(self.frame_41)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font15)
#if QT_CONFIG(tooltip)
        self.label_20.setToolTip(u"")
#endif // QT_CONFIG(tooltip)

        self.verticalLayout_55.addWidget(self.label_20)


        self.verticalLayout_58.addWidget(self.frame_41)

        self.inputFrame_2 = QFrame(self.frame_40)
        self.inputFrame_2.setObjectName(u"inputFrame_2")
        sizePolicy.setHeightForWidth(self.inputFrame_2.sizePolicy().hasHeightForWidth())
        self.inputFrame_2.setSizePolicy(sizePolicy)
        self.inputFrame_2.setFrameShape(QFrame.StyledPanel)
        self.inputFrame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_57 = QVBoxLayout(self.inputFrame_2)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.addressLine_2 = QFrame(self.inputFrame_2)
        self.addressLine_2.setObjectName(u"addressLine_2")
        sizePolicy12.setHeightForWidth(self.addressLine_2.sizePolicy().hasHeightForWidth())
        self.addressLine_2.setSizePolicy(sizePolicy12)
        self.addressLine_2.setLayoutDirection(Qt.LeftToRight)
        self.addressLine_2.setStyleSheet(u"gridline-color: rgb(255, 0, 127);")
        self.addressLine_2.setFrameShape(QFrame.NoFrame)
        self.addressLine_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.addressLine_2)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.addressLineEditT = QLineEdit(self.addressLine_2)
        self.addressLineEditT.setObjectName(u"addressLineEditT")
        sizePolicy5.setHeightForWidth(self.addressLineEditT.sizePolicy().hasHeightForWidth())
        self.addressLineEditT.setSizePolicy(sizePolicy5)
        self.addressLineEditT.setMinimumSize(QSize(300, 40))
        self.addressLineEditT.setFont(font8)
        self.addressLineEditT.setStyleSheet(u"background-color: rgb(255, 0, 127);")

        self.gridLayout_7.addWidget(self.addressLineEditT, 0, 1, 1, 1)

        self.CertBtn_4 = QPushButton(self.addressLine_2)
        self.CertBtn_4.setObjectName(u"CertBtn_4")
        self.CertBtn_4.setStyleSheet(u"")
        self.CertBtn_4.setIcon(icon47)
        self.CertBtn_4.setIconSize(QSize(24, 24))

        self.gridLayout_7.addWidget(self.CertBtn_4, 0, 0, 1, 1, Qt.AlignHCenter)


        self.horizontalLayout_21.addLayout(self.gridLayout_7)


        self.verticalLayout_57.addWidget(self.addressLine_2)

        self.frame_42 = QFrame(self.inputFrame_2)
        self.frame_42.setObjectName(u"frame_42")
        sizePolicy8.setHeightForWidth(self.frame_42.sizePolicy().hasHeightForWidth())
        self.frame_42.setSizePolicy(sizePolicy8)
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_21 = QLabel(self.frame_42)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font15)

        self.horizontalLayout_30.addWidget(self.label_21, 0, Qt.AlignLeft|Qt.AlignBottom)


        self.verticalLayout_57.addWidget(self.frame_42, 0, Qt.AlignLeft|Qt.AlignBottom)

        self.amountLine_2 = QFrame(self.inputFrame_2)
        self.amountLine_2.setObjectName(u"amountLine_2")
        sizePolicy1.setHeightForWidth(self.amountLine_2.sizePolicy().hasHeightForWidth())
        self.amountLine_2.setSizePolicy(sizePolicy1)
        self.amountLine_2.setMaximumSize(QSize(350, 50))
        self.amountLine_2.setLayoutDirection(Qt.LeftToRight)
        self.amountLine_2.setStyleSheet(u"gridline-color: rgb(255, 0, 127);")
        self.amountLine_2.setFrameShape(QFrame.NoFrame)
        self.amountLine_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.amountLine_2)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.amountLineEditT = QLineEdit(self.amountLine_2)
        self.amountLineEditT.setObjectName(u"amountLineEditT")
        sizePolicy5.setHeightForWidth(self.amountLineEditT.sizePolicy().hasHeightForWidth())
        self.amountLineEditT.setSizePolicy(sizePolicy5)
        self.amountLineEditT.setMinimumSize(QSize(300, 40))
        self.amountLineEditT.setFont(font8)
        self.amountLineEditT.setStyleSheet(u"background-color: rgb(255, 0, 127);")

        self.gridLayout_8.addWidget(self.amountLineEditT, 0, 1, 1, 1)

        self.pushButton_33 = QPushButton(self.amountLine_2)
        self.pushButton_33.setObjectName(u"pushButton_33")
        self.pushButton_33.setIcon(icon45)
        self.pushButton_33.setIconSize(QSize(24, 24))

        self.gridLayout_8.addWidget(self.pushButton_33, 0, 0, 1, 1)


        self.horizontalLayout_24.addLayout(self.gridLayout_8)


        self.verticalLayout_57.addWidget(self.amountLine_2)


        self.verticalLayout_58.addWidget(self.inputFrame_2)

        self.btnFrame_2 = QFrame(self.frame_40)
        self.btnFrame_2.setObjectName(u"btnFrame_2")
        self.btnFrame_2.setFrameShape(QFrame.StyledPanel)
        self.btnFrame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_56 = QVBoxLayout(self.btnFrame_2)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.sendAssetsBtn = QPushButton(self.btnFrame_2)
        self.sendAssetsBtn.setObjectName(u"sendAssetsBtn")
        sizePolicy6.setHeightForWidth(self.sendAssetsBtn.sizePolicy().hasHeightForWidth())
        self.sendAssetsBtn.setSizePolicy(sizePolicy6)
        self.sendAssetsBtn.setMinimumSize(QSize(200, 50))
        self.sendAssetsBtn.setFont(font16)
        self.sendAssetsBtn.setStyleSheet(u"")

        self.verticalLayout_56.addWidget(self.sendAssetsBtn)


        self.verticalLayout_58.addWidget(self.btnFrame_2)


        self.horizontalLayout_14.addWidget(self.frame_40)

        self.mainPages.addWidget(self.wallet_page)

        self.horizontalLayout_8.addWidget(self.mainPages)

        self.rightMenuContainer = QCustomSlideMenu(self.mainBodyContent)
        self.rightMenuContainer.setObjectName(u"rightMenuContainer")
        self.rightMenuContainer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_11 = QVBoxLayout(self.rightMenuContainer)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.rightMenuSubContainer = QWidget(self.rightMenuContainer)
        self.rightMenuSubContainer.setObjectName(u"rightMenuSubContainer")
        self.rightMenuSubContainer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_12 = QVBoxLayout(self.rightMenuSubContainer)
        self.verticalLayout_12.setSpacing(5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(5, 5, 5, 5)
        self.frame_8 = QFrame(self.rightMenuSubContainer)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_7 = QLabel(self.frame_8)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font8)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_7)

        self.closeRightMenuBtn = QPushButton(self.frame_8)
        self.closeRightMenuBtn.setObjectName(u"closeRightMenuBtn")
        self.closeRightMenuBtn.setIcon(icon11)
        self.closeRightMenuBtn.setIconSize(QSize(20, 24))

        self.horizontalLayout_9.addWidget(self.closeRightMenuBtn, 0, Qt.AlignRight)


        self.verticalLayout_12.addWidget(self.frame_8)

        self.rightMenuPages = QCustomStackedWidget(self.rightMenuSubContainer)
        self.rightMenuPages.setObjectName(u"rightMenuPages")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_13 = QVBoxLayout(self.page_4)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_8 = QLabel(self.page_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_8, 0, Qt.AlignTop)

        self.frame_55 = QFrame(self.page_4)
        self.frame_55.setObjectName(u"frame_55")
        sizePolicy.setHeightForWidth(self.frame_55.sizePolicy().hasHeightForWidth())
        self.frame_55.setSizePolicy(sizePolicy)
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.frame_55)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 100, 368, 42))
        self.gridLayout_9 = QGridLayout(self.layoutWidget)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.addressLineEditT_2 = QLineEdit(self.layoutWidget)
        self.addressLineEditT_2.setObjectName(u"addressLineEditT_2")
        sizePolicy5.setHeightForWidth(self.addressLineEditT_2.sizePolicy().hasHeightForWidth())
        self.addressLineEditT_2.setSizePolicy(sizePolicy5)
        self.addressLineEditT_2.setMinimumSize(QSize(300, 40))
        self.addressLineEditT_2.setFont(font)
        self.addressLineEditT_2.setStyleSheet(u"background-color: rgb(255, 0, 127);")

        self.gridLayout_9.addWidget(self.addressLineEditT_2, 0, 1, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font8)

        self.gridLayout_9.addWidget(self.label_2, 0, 0, 1, 1)

        self.layoutWidget_2 = QWidget(self.frame_55)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(0, 160, 367, 42))
        self.gridLayout_10 = QGridLayout(self.layoutWidget_2)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.addressLineEditT_3 = QLineEdit(self.layoutWidget_2)
        self.addressLineEditT_3.setObjectName(u"addressLineEditT_3")
        sizePolicy5.setHeightForWidth(self.addressLineEditT_3.sizePolicy().hasHeightForWidth())
        self.addressLineEditT_3.setSizePolicy(sizePolicy5)
        self.addressLineEditT_3.setMinimumSize(QSize(300, 40))
        self.addressLineEditT_3.setFont(font)
        self.addressLineEditT_3.setStyleSheet(u"background-color: rgb(255, 0, 127);")

        self.gridLayout_10.addWidget(self.addressLineEditT_3, 0, 1, 1, 1)

        self.label_3 = QLabel(self.layoutWidget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font8)

        self.gridLayout_10.addWidget(self.label_3, 0, 0, 1, 1)

        self.layoutWidget_3 = QWidget(self.frame_55)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(0, 220, 342, 42))
        self.gridLayout_11 = QGridLayout(self.layoutWidget_3)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.addressLineEditT_4 = QLineEdit(self.layoutWidget_3)
        self.addressLineEditT_4.setObjectName(u"addressLineEditT_4")
        sizePolicy5.setHeightForWidth(self.addressLineEditT_4.sizePolicy().hasHeightForWidth())
        self.addressLineEditT_4.setSizePolicy(sizePolicy5)
        self.addressLineEditT_4.setMinimumSize(QSize(300, 40))
        self.addressLineEditT_4.setFont(font8)
        self.addressLineEditT_4.setStyleSheet(u"background-color: rgb(255, 0, 127);")

        self.gridLayout_11.addWidget(self.addressLineEditT_4, 0, 1, 1, 1)

        self.CertBtn_5 = QPushButton(self.layoutWidget_3)
        self.CertBtn_5.setObjectName(u"CertBtn_5")
        self.CertBtn_5.setStyleSheet(u"")
        icon48 = QIcon()
        icon48.addFile(u":/icons/icons/phone.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.CertBtn_5.setIcon(icon48)
        self.CertBtn_5.setIconSize(QSize(24, 24))

        self.gridLayout_11.addWidget(self.CertBtn_5, 0, 0, 1, 1, Qt.AlignHCenter)

        self.layoutWidget_4 = QWidget(self.frame_55)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(0, 270, 342, 42))
        self.gridLayout_12 = QGridLayout(self.layoutWidget_4)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.addressLineEditT_5 = QLineEdit(self.layoutWidget_4)
        self.addressLineEditT_5.setObjectName(u"addressLineEditT_5")
        sizePolicy5.setHeightForWidth(self.addressLineEditT_5.sizePolicy().hasHeightForWidth())
        self.addressLineEditT_5.setSizePolicy(sizePolicy5)
        self.addressLineEditT_5.setMinimumSize(QSize(300, 40))
        self.addressLineEditT_5.setFont(font8)
        self.addressLineEditT_5.setStyleSheet(u"background-color: rgb(255, 0, 127);")

        self.gridLayout_12.addWidget(self.addressLineEditT_5, 0, 1, 1, 1)

        self.CertBtn_6 = QPushButton(self.layoutWidget_4)
        self.CertBtn_6.setObjectName(u"CertBtn_6")
        self.CertBtn_6.setStyleSheet(u"")
        icon49 = QIcon()
        icon49.addFile(u":/icons/icons/globe.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.CertBtn_6.setIcon(icon49)
        self.CertBtn_6.setIconSize(QSize(24, 24))

        self.gridLayout_12.addWidget(self.CertBtn_6, 0, 0, 1, 1, Qt.AlignHCenter)

        self.layoutWidget_5 = QWidget(self.frame_55)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(0, 320, 342, 42))
        self.gridLayout_13 = QGridLayout(self.layoutWidget_5)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.addressLineEditT_6 = QLineEdit(self.layoutWidget_5)
        self.addressLineEditT_6.setObjectName(u"addressLineEditT_6")
        sizePolicy5.setHeightForWidth(self.addressLineEditT_6.sizePolicy().hasHeightForWidth())
        self.addressLineEditT_6.setSizePolicy(sizePolicy5)
        self.addressLineEditT_6.setMinimumSize(QSize(300, 40))
        self.addressLineEditT_6.setFont(font8)
        self.addressLineEditT_6.setStyleSheet(u"background-color: rgb(255, 0, 127);")

        self.gridLayout_13.addWidget(self.addressLineEditT_6, 0, 1, 1, 1)

        self.CertBtn_7 = QPushButton(self.layoutWidget_5)
        self.CertBtn_7.setObjectName(u"CertBtn_7")
        self.CertBtn_7.setStyleSheet(u"")
        icon50 = QIcon()
        icon50.addFile(u":/icons/icons/user-check.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.CertBtn_7.setIcon(icon50)
        self.CertBtn_7.setIconSize(QSize(24, 24))

        self.gridLayout_13.addWidget(self.CertBtn_7, 0, 0, 1, 1, Qt.AlignHCenter)

        self.layoutWidget_6 = QWidget(self.frame_55)
        self.layoutWidget_6.setObjectName(u"layoutWidget_6")
        self.layoutWidget_6.setGeometry(QRect(0, 370, 342, 42))
        self.gridLayout_14 = QGridLayout(self.layoutWidget_6)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.addressLineEditT_7 = QLineEdit(self.layoutWidget_6)
        self.addressLineEditT_7.setObjectName(u"addressLineEditT_7")
        sizePolicy5.setHeightForWidth(self.addressLineEditT_7.sizePolicy().hasHeightForWidth())
        self.addressLineEditT_7.setSizePolicy(sizePolicy5)
        self.addressLineEditT_7.setMinimumSize(QSize(300, 40))
        self.addressLineEditT_7.setFont(font8)
        self.addressLineEditT_7.setStyleSheet(u"background-color: rgb(255, 0, 127);")

        self.gridLayout_14.addWidget(self.addressLineEditT_7, 0, 1, 1, 1)

        self.CertBtn_8 = QPushButton(self.layoutWidget_6)
        self.CertBtn_8.setObjectName(u"CertBtn_8")
        self.CertBtn_8.setStyleSheet(u"")
        icon51 = QIcon()
        icon51.addFile(u":/icons/icons/mail.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.CertBtn_8.setIcon(icon51)
        self.CertBtn_8.setIconSize(QSize(24, 24))

        self.gridLayout_14.addWidget(self.CertBtn_8, 0, 0, 1, 1, Qt.AlignHCenter)

        self.btnFrame_3 = QFrame(self.frame_55)
        self.btnFrame_3.setObjectName(u"btnFrame_3")
        self.btnFrame_3.setGeometry(QRect(60, 420, 354, 68))
        self.btnFrame_3.setFrameShape(QFrame.StyledPanel)
        self.btnFrame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_74 = QVBoxLayout(self.btnFrame_3)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.registerBtn = QPushButton(self.btnFrame_3)
        self.registerBtn.setObjectName(u"registerBtn")
        sizePolicy6.setHeightForWidth(self.registerBtn.sizePolicy().hasHeightForWidth())
        self.registerBtn.setSizePolicy(sizePolicy6)
        self.registerBtn.setMinimumSize(QSize(200, 50))
        self.registerBtn.setFont(font16)
        self.registerBtn.setStyleSheet(u"background-color:#351c75;\n"
"border-radius:10px;")

        self.verticalLayout_74.addWidget(self.registerBtn)


        self.verticalLayout_13.addWidget(self.frame_55)

        self.rightMenuPages.addWidget(self.page_4)
        self.page_5 = QCustomSlideMenu()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_14 = QVBoxLayout(self.page_5)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_9 = QLabel(self.page_5)
        self.label_9.setObjectName(u"label_9")
        sizePolicy8.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy8)
        self.label_9.setFont(font2)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_9)

        self.rightMenuPages.addWidget(self.page_5)

        self.verticalLayout_12.addWidget(self.rightMenuPages)


        self.verticalLayout_11.addWidget(self.rightMenuSubContainer)


        self.horizontalLayout_8.addWidget(self.rightMenuContainer, 0, Qt.AlignRight)


        self.verticalLayout_10.addWidget(self.mainBodyContent)

        self.quickLinksContainer = QCustomSlideMenu(self.mainBodyContainer)
        self.quickLinksContainer.setObjectName(u"quickLinksContainer")
        self.quickLinksContainer.setInputMethodHints(Qt.ImhNone)
        self.verticalLayout_78 = QVBoxLayout(self.quickLinksContainer)
        self.verticalLayout_78.setSpacing(6)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.verticalLayout_78.setContentsMargins(9, 9, 9, 9)
        self.quickLinksSubContainer = QWidget(self.quickLinksContainer)
        self.quickLinksSubContainer.setObjectName(u"quickLinksSubContainer")
        sizePolicy13 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.quickLinksSubContainer.sizePolicy().hasHeightForWidth())
        self.quickLinksSubContainer.setSizePolicy(sizePolicy13)
        self.verticalLayout_79 = QVBoxLayout(self.quickLinksSubContainer)
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.label_79 = QLabel(self.quickLinksSubContainer)
        self.label_79.setObjectName(u"label_79")
        font17 = QFont()
        font17.setFamily(u"Segoe Print")
        font17.setPointSize(9)
        font17.setBold(True)
        font17.setWeight(75)
        self.label_79.setFont(font17)

        self.verticalLayout_79.addWidget(self.label_79)

        self.closequickLinkBtn = QPushButton(self.quickLinksSubContainer)
        self.closequickLinkBtn.setObjectName(u"closequickLinkBtn")
        sizePolicy3.setHeightForWidth(self.closequickLinkBtn.sizePolicy().hasHeightForWidth())
        self.closequickLinkBtn.setSizePolicy(sizePolicy3)
        icon52 = QIcon()
        icon52.addFile(u":/icons/icons/x-octagon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closequickLinkBtn.setIcon(icon52)
        self.closequickLinkBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_79.addWidget(self.closequickLinkBtn, 0, Qt.AlignRight)

        self.frame_73 = QFrame(self.quickLinksSubContainer)
        self.frame_73.setObjectName(u"frame_73")
        self.frame_73.setStyleSheet(u"border-radius:10px;\n"
"")
        self.frame_73.setFrameShape(QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_73)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.mailBtn = QPushButton(self.frame_73)
        self.mailBtn.setObjectName(u"mailBtn")
        self.mailBtn.setMinimumSize(QSize(0, 30))
        self.mailBtn.setFont(font8)
        self.mailBtn.setStyleSheet(u"")
        self.mailBtn.setIcon(icon51)

        self.gridLayout_3.addWidget(self.mailBtn, 1, 1, 1, 1)

        self.twitterBtn = QPushButton(self.frame_73)
        self.twitterBtn.setObjectName(u"twitterBtn")
        self.twitterBtn.setMinimumSize(QSize(0, 30))
        self.twitterBtn.setFont(font8)
        self.twitterBtn.setStyleSheet(u"")
        icon53 = QIcon()
        icon53.addFile(u":/icons/icons/twitter.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.twitterBtn.setIcon(icon53)

        self.gridLayout_3.addWidget(self.twitterBtn, 2, 0, 1, 1)

        self.polkAPIBtn = QPushButton(self.frame_73)
        self.polkAPIBtn.setObjectName(u"polkAPIBtn")
        self.polkAPIBtn.setMinimumSize(QSize(0, 30))
        self.polkAPIBtn.setFont(font8)
        self.polkAPIBtn.setStyleSheet(u"")
        self.polkAPIBtn.setIcon(icon19)

        self.gridLayout_3.addWidget(self.polkAPIBtn, 0, 0, 1, 1)

        self.gitlabBtn = QPushButton(self.frame_73)
        self.gitlabBtn.setObjectName(u"gitlabBtn")
        self.gitlabBtn.setMinimumSize(QSize(0, 30))
        self.gitlabBtn.setFont(font8)
        self.gitlabBtn.setStyleSheet(u"")
        icon54 = QIcon()
        icon54.addFile(u":/icons/icons/gitlab.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.gitlabBtn.setIcon(icon54)

        self.gridLayout_3.addWidget(self.gitlabBtn, 1, 0, 1, 1)

        self.youtubetBtn = QPushButton(self.frame_73)
        self.youtubetBtn.setObjectName(u"youtubetBtn")
        self.youtubetBtn.setMinimumSize(QSize(0, 30))
        self.youtubetBtn.setFont(font8)
        self.youtubetBtn.setStyleSheet(u"")
        icon55 = QIcon()
        icon55.addFile(u":/icons/icons/youtube.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.youtubetBtn.setIcon(icon55)

        self.gridLayout_3.addWidget(self.youtubetBtn, 2, 1, 1, 1)

        self.githubBtn = QPushButton(self.frame_73)
        self.githubBtn.setObjectName(u"githubBtn")
        self.githubBtn.setMinimumSize(QSize(0, 30))
        self.githubBtn.setFont(font8)
        self.githubBtn.setStyleSheet(u"")
        self.githubBtn.setIcon(icon5)

        self.gridLayout_3.addWidget(self.githubBtn, 0, 1, 1, 1)


        self.verticalLayout_79.addWidget(self.frame_73)


        self.verticalLayout_78.addWidget(self.quickLinksSubContainer)


        self.verticalLayout_10.addWidget(self.quickLinksContainer)

        self.popupNotificationContainer = QCustomSlideMenu(self.mainBodyContainer)
        self.popupNotificationContainer.setObjectName(u"popupNotificationContainer")
        self.verticalLayout_19 = QVBoxLayout(self.popupNotificationContainer)
        self.verticalLayout_19.setSpacing(6)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.popupNotificationSubContainer = QWidget(self.popupNotificationContainer)
        self.popupNotificationSubContainer.setObjectName(u"popupNotificationSubContainer")
        self.verticalLayout_20 = QVBoxLayout(self.popupNotificationSubContainer)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.popupNotificationSubContainer)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font17)

        self.verticalLayout_20.addWidget(self.label_14)

        self.frame_9 = QFrame(self.popupNotificationSubContainer)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_13 = QLabel(self.frame_9)
        self.label_13.setObjectName(u"label_13")
        sizePolicy14 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy14.setHorizontalStretch(0)
        sizePolicy14.setVerticalStretch(0)
        sizePolicy14.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy14)
        self.label_13.setFont(font)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_13)

        self.closeNotificationBtn = QPushButton(self.frame_9)
        self.closeNotificationBtn.setObjectName(u"closeNotificationBtn")
        sizePolicy3.setHeightForWidth(self.closeNotificationBtn.sizePolicy().hasHeightForWidth())
        self.closeNotificationBtn.setSizePolicy(sizePolicy3)
        self.closeNotificationBtn.setIcon(icon52)
        self.closeNotificationBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_10.addWidget(self.closeNotificationBtn, 0, Qt.AlignRight)


        self.verticalLayout_20.addWidget(self.frame_9)


        self.verticalLayout_19.addWidget(self.popupNotificationSubContainer)


        self.verticalLayout_10.addWidget(self.popupNotificationContainer)

        self.footerContainer = QWidget(self.mainBodyContainer)
        self.footerContainer.setObjectName(u"footerContainer")
        self.horizontalLayout_11 = QHBoxLayout(self.footerContainer)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.bottomBar = QFrame(self.footerContainer)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFont(font3)
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        font18 = QFont()
        font18.setFamily(u"Segoe Print")
        font18.setBold(False)
        font18.setWeight(50)
        self.creditsLabel.setFont(font18)

        self.horizontalLayout_12.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.version)

        self.sizeGrip = QFrame(self.bottomBar)
        self.sizeGrip.setObjectName(u"sizeGrip")
        self.sizeGrip.setMinimumSize(QSize(20, 0))
        self.sizeGrip.setMaximumSize(QSize(20, 16777215))
        self.sizeGrip.setFrameShape(QFrame.StyledPanel)
        self.sizeGrip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_12.addWidget(self.sizeGrip, 0, Qt.AlignRight)


        self.horizontalLayout_11.addWidget(self.bottomBar)


        self.verticalLayout_10.addWidget(self.footerContainer)


        self.horizontalLayout.addWidget(self.mainBodyContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.centerMenuPages.setCurrentIndex(0)
        self.mainPages.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(1)
        self.rightMenuPages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        MainWindow.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.menuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.homeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
#if QT_CONFIG(tooltip)
        self.networksBtn.setToolTip(QCoreApplication.translate("MainWindow", u"View Available Blockchains", None))
#endif // QT_CONFIG(tooltip)
        self.networksBtn.setText(QCoreApplication.translate("MainWindow", u"Parachains", None))
#if QT_CONFIG(tooltip)
        self.tradeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"View ", None))
#endif // QT_CONFIG(tooltip)
        self.tradeBtn.setText(QCoreApplication.translate("MainWindow", u"Trading", None))
#if QT_CONFIG(tooltip)
        self.miningBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Mine Crypto", None))
#endif // QT_CONFIG(tooltip)
        self.miningBtn.setText(QCoreApplication.translate("MainWindow", u"Mining", None))
#if QT_CONFIG(tooltip)
        self.mintingBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Mint NFTs", None))
#endif // QT_CONFIG(tooltip)
        self.mintingBtn.setText(QCoreApplication.translate("MainWindow", u"Your NFTs", None))
#if QT_CONFIG(tooltip)
        self.nftMarketBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Buy and Sell NFTs", None))
#endif // QT_CONFIG(tooltip)
        self.nftMarketBtn.setText(QCoreApplication.translate("MainWindow", u"NFTs Marketplace", None))
        self.walletBtn.setText(QCoreApplication.translate("MainWindow", u"Wallet", None))
#if QT_CONFIG(tooltip)
        self.settingsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Go to Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsBtn.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
#if QT_CONFIG(tooltip)
        self.infoBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Information about the app", None))
#endif // QT_CONFIG(tooltip)
        self.infoBtn.setText(QCoreApplication.translate("MainWindow", u"Information", None))
#if QT_CONFIG(tooltip)
        self.helpBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Get Help", None))
#endif // QT_CONFIG(tooltip)
        self.helpBtn.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
#if QT_CONFIG(tooltip)
        self.closeCenterMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Menu", None))
#endif // QT_CONFIG(tooltip)
        self.closeCenterMenuBtn.setText("")
        self.securityBtn.setText(QCoreApplication.translate("MainWindow", u"Security", None))
        self.currency.setText(QCoreApplication.translate("MainWindow", u"Currency", None))
        self.verification.setText(QCoreApplication.translate("MainWindow", u"Verification", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"KYC", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Account Statement", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Referrals", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.pushButton_42.setText(QCoreApplication.translate("MainWindow", u"API", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.textEdit_3.setMarkdown(QCoreApplication.translate("MainWindow", u"**Parachronos**\n"
"\n"
"`Unleashing the Polkadot Potential`\n"
"\n"
"Get Help from us by getting in contact from any of our social media platform.\n"
"\n"
"MIT License\n"
"\n"
"**Telegram: @FawazUE5**\n"
"\n"
"**Github: UnrealFawaz**\n"
"\n"
"**Discord: @Fawaz23**\n"
"\n"
"**Email: oyebodefawaz2020@gmail.com**\n"
"\n"
"**Created by: Fawaz H. Oyebode**\n"
"\n"
"**Dot Mining PC App **\n"
"\n"
"", None))
        self.textEdit_3.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe Print'; font-size:16pt; font-weight:600; color:#ee208b;\">Parachronos</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','monospace'; font-size:9.8pt; color:#c9c9d1; background-color:#1d1d26;\">Unleashing the Polkadot Potential</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-in"
                        "dent:0px;\"><span style=\" font-family:'Segoe UI'; color:#ffffff;\">Get Help from us by getting in contact from any of our social media platform.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; color:#ffffff;\">MIT License</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:600; color:#432498;\">Telegram: @FawazUE5</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:600; color:#432498;\">Github: UnrealFawaz</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-in"
                        "dent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:600; color:#432498;\">Discord: @Fawaz23</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:600; color:#432498;\">Email: oyebodefawaz2020@gmail.com</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-weight:600; color:#bd93f9;\">Created by: Fawaz H. Oyebode</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ee208b;\">Dot Mining PC App </span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-rig"
                        "ht:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEdit.setMarkdown(QCoreApplication.translate("MainWindow", u"**Parachronos**\n"
"\n"
"`Unleashing the Polkadot Potential`\n"
"\n"
"An interface created using Python, PyQt5 and PySide (support for PyQt), and\n"
"with themes fitting the Polkadot Hackathon APAC 2023 Edition. The PC\n"
"Application has a lot of features ranging from Dot currency mining, NFTs\n"
"collection and more.. Dot mining is based on the PC CPU_processors and their\n"
"speed multiplied together to get the mining rate.\n"
"\n"
"MIT License\n"
"\n"
"**Created by: Fawaz H. Oyebode**\n"
"\n"
"**Dot Mining PC App **\n"
"\n"
"**NFTs Collection/Marketplace**\n"
"\n"
"", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe Print'; font-size:16pt; font-weight:600; color:#ee208b;\">Parachronos</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Consolas','monospace'; font-size:9.8pt; color:#c9c9d1; background-color:#1d1d26;\">Unleashing the Polkadot Potential</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-in"
                        "dent:0px;\"><span style=\" font-family:'Segoe UI'; color:#ffffff;\">An interface created using Python, PyQt5 and PySide (support for PyQt), and with themes fitting the Polkadot Hackathon APAC 2023 Edition. The PC Application has a lot of features ranging from Dot currency mining, NFTs collection and more.. Dot mining is based on the PC CPU_processors and their speed multiplied together to get the mining rate.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; color:#ffffff;\">MIT License</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-weight:600; color:#bd93f9;\">Created by: Fawaz H. Oyebode</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent"
                        ":0; text-indent:0px;\"><span style=\" font-weight:600; color:#ee208b;\">Dot Mining PC App </span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:600; color:#ff79c6;\">NFTs Collection/Marketplace</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.pushButton_41.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Parachronos", None))
#if QT_CONFIG(tooltip)
        self.notificationBtn.setToolTip(QCoreApplication.translate("MainWindow", u"view notification", None))
#endif // QT_CONFIG(tooltip)
        self.notificationBtn.setText("")
#if QT_CONFIG(tooltip)
        self.moreMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"More", None))
#endif // QT_CONFIG(tooltip)
        self.moreMenuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.profileMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Profile", None))
#endif // QT_CONFIG(tooltip)
        self.profileMenuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimize_window_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize Window", None))
#endif // QT_CONFIG(tooltip)
        self.minimize_window_btn.setText("")
#if QT_CONFIG(tooltip)
        self.restore_window_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Restore Window", None))
#endif // QT_CONFIG(tooltip)
        self.restore_window_btn.setText("")
#if QT_CONFIG(tooltip)
        self.close_window_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Window", None))
#endif // QT_CONFIG(tooltip)
        self.close_window_btn.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Home", None))
#if QT_CONFIG(tooltip)
        self.backBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Back", None))
#endif // QT_CONFIG(tooltip)
        self.backBtn.setText("")
#if QT_CONFIG(tooltip)
        self.forwardBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Forward", None))
#endif // QT_CONFIG(tooltip)
        self.forwardBtn.setText("")
#if QT_CONFIG(tooltip)
        self.reloadBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Reload", None))
#endif // QT_CONFIG(tooltip)
        self.reloadBtn.setText("")
#if QT_CONFIG(tooltip)
        self.polkBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.polkBtn.setText("")
#if QT_CONFIG(tooltip)
        self.quickLinksBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Quick links", None))
#endif // QT_CONFIG(tooltip)
        self.quickLinksBtn.setText("")
        self.addressBar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
#if QT_CONFIG(tooltip)
        self.searchAddressBar.setToolTip(QCoreApplication.translate("MainWindow", u"search", None))
#endif // QT_CONFIG(tooltip)
        self.searchAddressBar.setText("")
#if QT_CONFIG(tooltip)
        self.CertBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Page information", None))
#endif // QT_CONFIG(tooltip)
        self.CertBtn.setText("")
#if QT_CONFIG(tooltip)
        self.zoomOutBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Zoom out", None))
#endif // QT_CONFIG(tooltip)
        self.zoomOutBtn.setText("")
#if QT_CONFIG(tooltip)
        self.zoomInBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Zoom In", None))
#endif // QT_CONFIG(tooltip)
        self.zoomInBtn.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_17.setToolTip(QCoreApplication.translate("MainWindow", u"Bookmarks", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_17.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_19.setToolTip(QCoreApplication.translate("MainWindow", u"Snapshot", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_19.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Parachronos", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"DASHBOARD", None))
        self.balanceLabel.setText("")
#if QT_CONFIG(tooltip)
        self.checkBalanceBtn.setToolTip(QCoreApplication.translate("MainWindow", u"View balance", None))
#endif // QT_CONFIG(tooltip)
        self.checkBalanceBtn.setText("")
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#1f232a;\">Get Started</span></p></body></html>", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#1f232a;\">You can start trading DOT currency now</span></p></body></html>", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"For Beginners", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Earn", None))
        self.pushButton_22.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#1f232a;\">Futures</span></p></body></html>", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#1f232a;\">DOT-USDT</span></p></body></html>", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#55ff00;\">$4,333,256 +3.45%</span></p></body></html>", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Full range of crypto instruments", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#1f232a;\">Explore</span></p></body></html>", None))
        self.addressBar_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
#if QT_CONFIG(tooltip)
        self.searchAddressBar_2.setToolTip(QCoreApplication.translate("MainWindow", u"search", None))
#endif // QT_CONFIG(tooltip)
        self.searchAddressBar_2.setText("")
#if QT_CONFIG(tooltip)
        self.CertBtn_3.setToolTip(QCoreApplication.translate("MainWindow", u"Page information", None))
#endif // QT_CONFIG(tooltip)
        self.CertBtn_3.setText("")
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"You can search for trading pairs and crypto-currencies ", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Amount", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"Price", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"Gainers/Loosers", None))
        self.pushButton_34.setText(QCoreApplication.translate("MainWindow", u"DOT", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"198938000000", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"$4,657,483.90", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"+10.79 %", None))
        self.pushButton_35.setText(QCoreApplication.translate("MainWindow", u"BNB", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"380076462", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"$657,483.90", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"+3.79 %", None))
        self.pushButton_36.setText(QCoreApplication.translate("MainWindow", u"EOS", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"75669.23", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"$151.90", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"+1.79 %", None))
        self.pushButton_37.setText(QCoreApplication.translate("MainWindow", u"ETH", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"198938000000", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"$40,657,483.90", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"-2.34 %", None))
        self.pushButton_38.setText(QCoreApplication.translate("MainWindow", u"Polygon", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"3893892045", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"$7,483.90", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"-4.22 %", None))
        self.pushButton_39.setText(QCoreApplication.translate("MainWindow", u"USDT", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"4553758", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"$4,657,483.90", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"+5.62 %", None))
        self.pushButton_40.setText(QCoreApplication.translate("MainWindow", u"BTC", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"23564553758", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"$4,657,483.90", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"+3.62 %", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"DOT", None))
        self.pushButton_44.setText(QCoreApplication.translate("MainWindow", u"Buy", None))
        self.pushButton_45.setText(QCoreApplication.translate("MainWindow", u"Sell", None))
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"BTC", None))
        self.pushButton_54.setText(QCoreApplication.translate("MainWindow", u"Buy", None))
        self.pushButton_55.setText(QCoreApplication.translate("MainWindow", u"Sell", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"USDT", None))
        self.pushButton_52.setText(QCoreApplication.translate("MainWindow", u"Buy", None))
        self.pushButton_53.setText(QCoreApplication.translate("MainWindow", u"Sell", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"EOS", None))
        self.pushButton_50.setText(QCoreApplication.translate("MainWindow", u"Buy", None))
        self.pushButton_51.setText(QCoreApplication.translate("MainWindow", u"Sell", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"BNB", None))
        self.pushButton_48.setText(QCoreApplication.translate("MainWindow", u"Buy", None))
        self.pushButton_49.setText(QCoreApplication.translate("MainWindow", u"Sell", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"ETH", None))
        self.pushButton_46.setText(QCoreApplication.translate("MainWindow", u"Buy", None))
        self.pushButton_47.setText(QCoreApplication.translate("MainWindow", u"Sell", None))
        self.start_stopBtn.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.cpu_freq_label.setText("")
        self.cpu_processors_label.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Your NFTs", None))
        self.label_56.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_15.setToolTip(QCoreApplication.translate("MainWindow", u"Click to mint NFT", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"Mint", None))
        self.label_35.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_4.setToolTip(QCoreApplication.translate("MainWindow", u"Click to mint NFT", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Mint", None))
        self.label_34.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_7.setToolTip(QCoreApplication.translate("MainWindow", u"Click to mint NFT", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Mint", None))
        self.label_58.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_30.setToolTip(QCoreApplication.translate("MainWindow", u"Click to mint NFT", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_30.setText(QCoreApplication.translate("MainWindow", u"Mint", None))
        self.label_57.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_16.setToolTip(QCoreApplication.translate("MainWindow", u"Click to mint NFT", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"Mint", None))
        self.label_53.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_6.setToolTip(QCoreApplication.translate("MainWindow", u"Click to mint NFT", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Mint", None))
        self.label_36.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Mint", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"Marketplace", None))
        self.label_38.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_10.setToolTip(QCoreApplication.translate("MainWindow", u"Click to buy NFT", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"340", None))
        self.label_39.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_11.setToolTip(QCoreApplication.translate("MainWindow", u"Click to buy NFT", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"330", None))
        self.label_40.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_12.setToolTip(QCoreApplication.translate("MainWindow", u"Click to buy NFT", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"330", None))
        self.label_47.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_24.setToolTip(QCoreApplication.translate("MainWindow", u"Click to buy NFT", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"1100", None))
        self.label_48.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_25.setToolTip(QCoreApplication.translate("MainWindow", u"Click to buy NFT", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"1190", None))
        self.label_46.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_23.setToolTip(QCoreApplication.translate("MainWindow", u"Click to buy NFT", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"250", None))
        self.label_52.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_29.setToolTip(QCoreApplication.translate("MainWindow", u"Click to mint NFT", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_29.setText(QCoreApplication.translate("MainWindow", u"655", None))
        self.label_50.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_27.setToolTip(QCoreApplication.translate("MainWindow", u"Click to buy NFT", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"458", None))
        self.label_55.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_32.setToolTip(QCoreApplication.translate("MainWindow", u"Click to buy NFT", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_32.setText(QCoreApplication.translate("MainWindow", u"655", None))
        self.label_54.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_31.setToolTip(QCoreApplication.translate("MainWindow", u"Click to buy NFT", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_31.setText(QCoreApplication.translate("MainWindow", u"250", None))
        self.label_42.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_14.setToolTip(QCoreApplication.translate("MainWindow", u"Click to buy NFT", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"340", None))
        self.label_41.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_13.setToolTip(QCoreApplication.translate("MainWindow", u"Click to buy NFT", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"250", None))
        self.label_49.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_26.setToolTip(QCoreApplication.translate("MainWindow", u"Click to buy NFT", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"330", None))
        self.label_43.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_18.setToolTip(QCoreApplication.translate("MainWindow", u"Click to buy NFT", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"340", None))
        self.label_51.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_28.setToolTip(QCoreApplication.translate("MainWindow", u"Click to buy NFT", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_28.setText(QCoreApplication.translate("MainWindow", u"550", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"DASHBOARD", None))
        self.balanceLabel_2.setText("")
#if QT_CONFIG(tooltip)
        self.checkBalanceBtn_2.setToolTip(QCoreApplication.translate("MainWindow", u"View balance", None))
#endif // QT_CONFIG(tooltip)
        self.checkBalanceBtn_2.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Deposit", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Wallet Address", None))
#if QT_CONFIG(tooltip)
        self.addressLineEdit.setToolTip(QCoreApplication.translate("MainWindow", u"Paste wallet address here", None))
#endif // QT_CONFIG(tooltip)
        self.addressLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Paste wallet address Here", None))
        self.CertBtn_2.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Amount", None))
#if QT_CONFIG(tooltip)
        self.amountLineEdit.setToolTip(QCoreApplication.translate("MainWindow", u"Enter Amount", None))
#endif // QT_CONFIG(tooltip)
        self.amountLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Amount", None))
        self.pushButton_2.setText("")
#if QT_CONFIG(tooltip)
        self.receiveBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Click to Receive", None))
#endif // QT_CONFIG(tooltip)
        self.receiveBtn.setText(QCoreApplication.translate("MainWindow", u"RECEIVE", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Transfer", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Wallet Address", None))
#if QT_CONFIG(tooltip)
        self.addressLineEditT.setToolTip(QCoreApplication.translate("MainWindow", u"Paste wallet address here", None))
#endif // QT_CONFIG(tooltip)
        self.addressLineEditT.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Paste wallet address Here", None))
        self.CertBtn_4.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Amount", None))
#if QT_CONFIG(tooltip)
        self.amountLineEditT.setToolTip(QCoreApplication.translate("MainWindow", u"Enter Amount", None))
#endif // QT_CONFIG(tooltip)
        self.amountLineEditT.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Amount", None))
        self.pushButton_33.setText("")
#if QT_CONFIG(tooltip)
        self.sendAssetsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Click to Send", None))
#endif // QT_CONFIG(tooltip)
        self.sendAssetsBtn.setText(QCoreApplication.translate("MainWindow", u"SEND", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Parachronos", None))
#if QT_CONFIG(tooltip)
        self.closeRightMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Menu", None))
#endif // QT_CONFIG(tooltip)
        self.closeRightMenuBtn.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.addressLineEditT_2.setText("")
        self.addressLineEditT_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter First Name", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.addressLineEditT_3.setText("")
        self.addressLineEditT_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Last Name", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.addressLineEditT_4.setText("")
        self.addressLineEditT_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Phone Number", None))
        self.CertBtn_5.setText("")
        self.addressLineEditT_5.setText("")
        self.addressLineEditT_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Country or Region", None))
        self.CertBtn_6.setText("")
        self.addressLineEditT_6.setText("")
        self.addressLineEditT_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.CertBtn_7.setText("")
        self.addressLineEditT_7.setText("")
        self.addressLineEditT_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Email Address", None))
        self.CertBtn_8.setText("")
#if QT_CONFIG(tooltip)
        self.registerBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Click to Register", None))
#endif // QT_CONFIG(tooltip)
        self.registerBtn.setText(QCoreApplication.translate("MainWindow", u"REGISTER", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"More....", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"Quick Links", None))
#if QT_CONFIG(tooltip)
        self.closequickLinkBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Notification", None))
#endif // QT_CONFIG(tooltip)
        self.closequickLinkBtn.setText("")
        self.mailBtn.setText(QCoreApplication.translate("MainWindow", u"Mail", None))
        self.twitterBtn.setText(QCoreApplication.translate("MainWindow", u"Twitter", None))
        self.polkAPIBtn.setText(QCoreApplication.translate("MainWindow", u"Polkadot API", None))
        self.gitlabBtn.setText(QCoreApplication.translate("MainWindow", u"GitLab", None))
        self.youtubetBtn.setText(QCoreApplication.translate("MainWindow", u"Youtube", None))
        self.githubBtn.setText(QCoreApplication.translate("MainWindow", u"Github", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Notification", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Notification message", None))
#if QT_CONFIG(tooltip)
        self.closeNotificationBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Notification", None))
#endif // QT_CONFIG(tooltip)
        self.closeNotificationBtn.setText("")
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: Fawaz H. Oyebode", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.3", None))
    # retranslateUi

