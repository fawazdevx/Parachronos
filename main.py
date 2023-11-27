import os
import sys
from PySide2.QtWebEngineWidgets import QWebEngineView
from PySide2.QtCore import QUrl
from PyQt5.QtWidgets import *
from PySide2.QtGui import QPainter, QIcon
from PySide2.QtCharts import QtCharts
from PySide2.QtWidgets import QSizePolicy
from random import randrange
from functools import partial
from custom_buttons import QPushButton
import csv
import psutil
import shutil
# IMPORT GUI FILE

# ==> SPLASH SCREEN
from ui_splash_screen import *
# ==> MAIN UI
from ui_interface_PK import *

# CUSTOM WIDGETS
from Custom_Widgets.Widgets import *

# Code to make the software create a directory / folder on the target system
make_dir = os.path.expanduser('~/')
os.makedirs(make_dir, exist_ok=True)
icon_to_path = "images/globe-africa.svg"
destination_path = os.path.expanduser(r'~/')
shutil.copy(icon_to_path, destination_path)


# ==> GLOBAL VARIABLES
counter = 0

shadow_elements = {
    "progressBar",
    "frame_11", "frame_12", "frame_15", "frame_16", "frame_17", "frame_18", "frame_19", "frame_20",
    "frame_21", "frame_22", "frame_23", "frame_24", "frame_25", "frame_26", "frame_27", "frame_28",
    "frame_30", "frame_48", "frame_49", "frame_50", "frame_51", "frame_54", "frame_52", "frame_53",
    "frame_56", "frame_58", "frame_59", "frame_60", "frame_61", "frame_63", "frame_64", "frame_65",
    "frame_66", "frame_67", "frame_68"
}
########################################################################
# MAIN WINDOW CLASS


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # set app icon
        icon_path = "images/parachronos.ico"
        self.ui.app_icon.setIcon(QIcon(icon_path))

        # REMOVE TITLE BAR
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.setMinimumSize(850, 600)

        self.create_trading_charts()

        # WEB VIEW
        self.webEngineView = QWebEngineView()  # SHOWING WEB VIEW
        self.ui.verticalLayout_53.addWidget(self.webEngineView)  # Add to a layout
        self.webEngineView.load(QUrl("https://polkadot.network/"))

        # SHADOW EFFECT
        for x in shadow_elements:
            effect = QtWidgets.QGraphicsDropShadowEffect(self)
            effect.setBlurRadius(18)
            effect.setXOffset(0)
            effect.setYOffset(0)
            effect.setColor(QColor(0, 0, 0, 255))
            getattr(self.ui, x).setGraphicsEffect(effect)

        # adding features to mining cycle progess
        self.ui.progressBar.rpb_setMaximumSize(400, 400)  #
        self.ui.progressBar.rpb_setMinimumSize(400, 400)  #
        self.ui.progressBar.rpb_setMaximum(100)
        self.ui.progressBar.rpb_setBarStyle("Donet")
        self.ui.progressBar.rpb_setLineColor((0, 170, 255))
        self.ui.progressBar.rpb_setPathColor((233, 30, 99))
        self.ui.progressBar.rpb_setTextColor((233, 30, 99))
        self.ui.progressBar.rpb_setInitialPos('West')
        self.ui.progressBar.rpb_setTextFormat('Value')
        self.ui.progressBar.rpb_setTextFont("Segoe Print")
        self.ui.progressBar.rpb_setTextWidth(15)
        self.ui.progressBar.rpb_setLineWidth(10)
        self.ui.progressBar.rpb_setPathWidth(15)
        self.ui.progressBar.rpb_setLineCap("RoundCap")
        self.ui.progressBar.rpb_setLineStyle("DotLine")

        ########################################################################
        loadJsonStyle(self, self.ui)  # APPLY JSON STYLESHEET
        #######################################################################

        # EXPAND CENTER MENU WIDGET SIZE

        self.ui.settingsBtn.clicked.connect(lambda: self.ui.centerMenuContainer.animateMenu())
        self.ui.infoBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.helpBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())

        # CLOSE CENTER MENU WIDGET SIZE
        self.ui.closeCenterMenuBtn.clicked.connect(lambda: self.ui.centerMenuContainer.collapseMenu())

        # EXPAND RIGHT MENU WIDGET SIZE
        self.ui.moreMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())
        self.ui.profileMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())

        # CLOSE RIGHT MENU WIDGET
        self.ui.closeRightMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.collapseMenu())

        # CLOSE NOTIFICATION MENU WIDGET
        self.ui.closeNotificationBtn.clicked.connect(lambda: self.ui.popupNotificationContainer.collapseMenu())

        # CLOSE QUICK LINKS CONTAINER
        self.ui.closequickLinkBtn.clicked.connect(lambda: self.ui.quickLinksContainer.collapseMenu())

        # ==> LEFT MENU THEMING
        self.ui.menuBtn.setObjectTheme(10)
        self.ui.homeBtn.setObjectTheme(10)
        self.ui.networksBtn.setObjectTheme(10)
        self.ui.tradeBtn.setObjectTheme(10)
        self.ui.miningBtn.setObjectTheme(10)
        self.ui.nftMarketBtn.setObjectTheme(10)
        self.ui.walletBtn.setObjectTheme(10)
        self.ui.mintingBtn.setObjectTheme(10)
        self.ui.walletBtn.setObjectTheme(10)
        self.ui.settingsBtn.setObjectTheme(10)
        self.ui.infoBtn.setObjectTheme(10)
        self.ui.helpBtn.setObjectTheme(10)
        self.ui.closeRightMenuBtn.setObjectTheme(10)
        self.ui.closeCenterMenuBtn.setObjectTheme(10)

        # ==> CENTER TOP MENU THEMING
        self.ui.notificationBtn.setObjectTheme(10)
        self.ui.closeNotificationBtn.setObjectTheme(10)
        self.ui.profileMenuBtn.setObjectTheme(10)
        self.ui.moreMenuBtn.setObjectTheme(10)

        self.ui.minimize_window_btn.setObjectTheme(10)
        self.ui.restore_window_btn.setObjectTheme(10)
        self.ui.close_window_btn.setObjectTheme(10)

    ################################################################################
        # PARA_BROWSER
    ################################################################################

        self.ui.sizeGrip.setVisible(True)
        self.ui.backBtn.clicked.connect(self.webEngineView.back)
        self.ui.forwardBtn.clicked.connect(self.webEngineView.forward)
        self.ui.reloadBtn.clicked.connect(self.webEngineView.reload)
        self.ui.polkBtn.clicked.connect(self.goto_home)
        self.ui.zoomInBtn.clicked.connect(self.decrease_zoom)
        self.ui.zoomOutBtn.clicked.connect(self.increase_zoom)

        # ==> QUICK LINKS THEMING
        self.ui.polkAPIBtn.setObjectTheme(10)
        self.ui.githubBtn.setObjectTheme(10)
        self.ui.gitlabBtn.setObjectTheme(10)
        self.ui.youtubetBtn.setObjectTheme(10)
        self.ui.mailBtn.setObjectTheme(10)
        self.ui.twitterBtn.setObjectTheme(10)
        self.ui.closequickLinkBtn.setObjectTheme(10)

        # Quick Links
        self.ui.polkAPIBtn.clicked.connect(self.goto_polkadot_API)
        self.ui.githubBtn.clicked.connect(self.goto_github)
        self.ui.gitlabBtn.clicked.connect(self.goto_gitlab)
        self.ui.youtubetBtn.clicked.connect(self.goto_youtube)
        self.ui.mailBtn.clicked.connect(self.goto_mail)
        self.ui.twitterBtn.clicked.connect(self.goto_twitter)

        self.ui.addressBar.returnPressed.connect(self.on_lineEdit_returnPressed)
        self.ui.searchAddressBar.clicked.connect(self.on_lineEdit_returnPressed)

        self.webEngineView.urlChanged.connect(self.getcurrent_url)

        self.zoom_factor = 1.0
        self.webEngineView.setZoomFactor(self.zoom_factor)

        ######################################################
        # Setting Balance view label
        #####################################################
        self.is_balance_visible = False
        self.is_not_balance_visible = True
        self.update_balance()

        self.ui.sendAssetsBtn.setObjectTheme(10)
        self.ui.receiveBtn.setObjectTheme(10)
        self.ui.checkBalanceBtn.setObjectTheme(10)
        self.ui.checkBalanceBtn_2.setObjectTheme(10)

        self.ui.checkBalanceBtn.clicked.connect(self.toggle_balance)
        self.ui.checkBalanceBtn_2.clicked.connect(self.toggle_balance)
        self.ui.sendAssetsBtn.clicked.connect(self.send_tokens)
        self.ui.receiveBtn.clicked.connect(self.receive_tokens)

    def toggle_balance(self):
        self.is_balance_visible = not self.is_balance_visible
        self.update_balance()

    def update_balance(self):
        self.ui.balanceLabel.setVisible(self.is_balance_visible)
        self.ui.balanceLabel_2.setVisible(self.is_balance_visible)

        # Changing the icon based on the visibility state
        icon_path = "icons/eye-off.svg" if self.is_balance_visible else "icons/eye.svg"
        self.ui.checkBalanceBtn.setIcon(QIcon(icon_path))
        self.ui.checkBalanceBtn_2.setIcon(QIcon(icon_path))

        # Updating the text of the label based on the visibility state
        balance_text = "100.00 DOT" if self.is_not_balance_visible else ""
        self.ui.balanceLabel.setText(balance_text)
        self.ui.balanceLabel_2.setText(balance_text)

    def check_balance(self):
        # Replace this method with your actual implementation to check the account balance
        account_balance = "34353450.79 DOT"  # Sample balance for demonstration purposes
        self.ui.balanceLabel.setText(account_balance)
        self.ui.balanceLabel_2.setText(account_balance)

    def send_tokens(self):
        # send token function
        recipient_address = self.ui.addressLineEditT.text()
        amount_to_send = self.ui.amountLineEditT.text()
        # Adding logic to send DOT tokens to the recipient address with the specified amount
        QMessageBox.information(self, "Send Tokens", f"Sent {amount_to_send} DOT to {recipient_address}")

    def receive_tokens(self):
        # Adding logic to receive DOT tokens to the user's account
        deposit_address = self.ui.addressLineEdit.text()
        amount_to_receive = self.ui.amountLineEdit.text()
        QMessageBox.information(self, "Receive Tokens", f"You received {amount_to_receive} DOT from {deposit_address}.")

    # ZoomOut WebView page
    def increase_zoom(self):
        self.zoom_factor += 0.1
        self.webEngineView.setZoomFactor(self.zoom_factor)

    # ZoomIn WebView page
    def decrease_zoom(self):
        self.zoom_factor -= 0.1
        self.webEngineView.setZoomFactor(self.zoom_factor)

    # Set Home Page for WebView
    def goto_home(self):
        self.webEngineView.setUrl(QUrl("https://polkadot.network"))

    def on_lineEdit_returnPressed(self):
        url = self.ui.addressBar.text()
        validated_url = QUrl(url)

        if validated_url.isValid():
            self.webEngineView.setUrl(validated_url)
        else:
            print("Invalid URL")

    # goto Quick links
    def goto_polkadot_API(self):
        self.webEngineView.setUrl(QUrl("https://polkadot.js.org"))

    def goto_github(self):
        self.webEngineView.setUrl(QUrl("https://www.github.com"))

    def goto_gitlab(self):
        self.webEngineView.setUrl(QUrl("https://www.gitlab.com"))

    def goto_mail(self):
        self.webEngineView.setUrl(QUrl("https://www.gmail.com"))

    def goto_twitter(self):
        self.webEngineView.setUrl(QUrl("https://www.twitter.com"))

    def goto_youtube(self):
        self.webEngineView.setUrl(QUrl("https://www.youtube.com"))

    def getcurrent_url(self, q):
        self.ui.addressBar.setText(q.toString())
    #################################################################################
    # trading chart function
    #####################################################################################

    def create_trading_charts(self):
        self.highTradeSeries = QtCharts.QLineSeries()
        self.lowTradeSeries = QtCharts.QLineSeries()
        self.high2TradeSeries = QtCharts.QLineSeries()
        self.low2TradeSeries = QtCharts.QLineSeries()

        rowCount = 0

        with open('trading_data/trading_reports.csv') as csvFile:
            csvReader = csv.reader(csvFile, delimiter=',')
            for row in csvReader:

                if rowCount > 0:

                    self.highTradeSeries.append(float(rowCount), float(row[0]))
                    self.lowTradeSeries.append(float(rowCount), float(row[1]))
                    self.high2TradeSeries.append(float(rowCount), float(row[2]))
                    self.low2TradeSeries.append(float(rowCount), float(row[3]))

                rowCount += 1

        ####################################################################################
        # Trading Charts
        ####################################################################################
        self.chart = QtCharts.QChart()
        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignBottom)
        self.chart.addSeries(self.highTradeSeries)
        self.chart.addSeries(self.lowTradeSeries)
        self.chart.addSeries(self.low2TradeSeries)
        self.chart.addSeries(self.high2TradeSeries)
        self.chart.createDefaultAxes()
        self.chart.setTitle("Statistics")

        self.chartView = QtCharts.QChartView(self.chart)
        self.chartView.setRenderHint(QPainter.Antialiasing)
        self.chart.setAnimationOptions(QtCharts.QChart.AllAnimations)
        self.chartView.chart().setTheme(QtCharts.QChart.ChartThemeDark)

        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(self.chartView.sizePolicy().hasHeightForWidth())
        self.chartView.setSizePolicy(sizePolicy)
        self.chartView.setMinimumSize(QSize(250, 350))

        self.ui.trading_charts_cont.addWidget(self.chartView)
        self.ui.frame_12.setStyleSheet(u"background-color: transparent")
        ##################################################################################
        # taking data from cpu_processors

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_progress)
        self.num_cpu_processors = psutil.cpu_count(logical=True)
        self.total_mining_cycles = 24 * 60 * 60  # Total mining cycles (24 hours)
        self.current_mining_cycle = 0
        self.mining_rate_per_processors = 0.5  # Mining rate per processors
        self.cpu_processors_speeds = self.get_cpu_processors_speeds()

        self.print_cpu_processors()

        self.ui.progressBar.rpb_setValue(0)
        self.ui.start_stopBtn.clicked.connect(self.toggle_mining)

    def print_cpu_processors(self):
        num_processors = psutil.cpu_count(logical=True)
        print(f"Number of CPU processors: {num_processors}")
        self.ui.cpu_processors_label.setText(f"CPU processors: {num_processors}")

    def toggle_mining(self):
        if not self.timer.isActive():
            self.timer.start(1000)  # Starting the timer for updating progress
            self.ui.start_stopBtn.setText("Stop Mining")
        else:
            self.timer.stop()  # Stopping the timer for updating progress
            self.ui.start_stopBtn.setText("Start Mining")

    def get_cpu_processors_speeds(self):
        cpu_processors_speeds = []
        try:
            cpu_freq = psutil.cpu_freq(percpu=True)
            cpu_processors_speeds = [freq.current for freq in cpu_freq]
            print(f"Number of CPU Speed: {cpu_freq}")
            self.ui.cpu_freq_label.setText(f"CPU Speed: {cpu_freq}")
        except Exception as e:
            print(f"Error retrieving CPU processors speeds: {str(e)}")
        return cpu_processors_speeds

    def update_progress(self):
        self.current_mining_cycle += 1
        mining_rate_per_processors = sum(self.cpu_processors_speeds) / len(self.cpu_processors_speeds) * self.mining_rate_per_processors

        mining_rate_total = mining_rate_per_processors * self.num_cpu_processors

        mining_rate_per_cycle = mining_rate_total / self.total_mining_cycles

        mined_amount = mining_rate_per_cycle * self.current_mining_cycle

        total_mined_amount = mined_amount / self.num_cpu_processors  # Total mined amount for number of CPU processors

        print(f"Mined Amount: {mined_amount:.2f} per cycle")  # Printing the current mined amountS

        self.ui.progressBar.rpb_setValue(total_mined_amount)
        self.ui.cpu_processors_label.setText(f"CPU processors: {psutil.cpu_count(logical=True)}")

        if self.current_mining_cycle >= self.total_mining_cycles:
            self.timer.stop()
            self.current_mining_cycle = 0


class SplashScreen(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        # REMOVE TITLE BAR
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 255))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        # QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.splash_screen_progress)
        self.timer.start(35)

        # CHANGE SPLASH DESCRIPTION
        # INITIAL TEXT
        self.ui.description.setText("<strong>WELCOME</strong> TO PARACHRONOS")

        # CHANGE TEXT
        QtCore.QTimer.singleShot(1500, lambda: self.ui.description.setText("<strong>LOADING</strong> DATABASE"))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.description.setText("<strong>INITIALIZING</strong> APPLICATION"))

        # SHOW WINDOW
        self.show()

    # SPLASH SCREEN FUNCTION
    def splash_screen_progress(self):
        global counter

        # SETTING VALUE TO PROGRESSBAR
        self.ui.progressBar.setValue(counter)

        # CLOSING SPLASH SCREEN AND OPENING MAIN UI
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN UI
            self.main = MainWindow()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE PROGRESS BAR COUNTER
        counter += 1


# EXECUTE APP
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ########################################################################
    window = SplashScreen()
    window.show()
    sys.exit(app.exec_())
