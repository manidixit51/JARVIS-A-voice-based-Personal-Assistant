from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_jarvisUi(object):
    def setupUi(self, jarvisUi):
        jarvisUi.setObjectName("jarvisUi")
        jarvisUi.resize(984, 572)
        self.centralwidget = QtWidgets.QWidget(jarvisUi)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, -10, 1021, 601))
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        # Additional UI Components
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(290, 330, 391, 201))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("Material/path.gif"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(720, 20, 261, 221))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("Material/logo.gif"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")

        # TextBrowsers
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 510, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Sitka Subheading")
        font.setPointSize(16)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background:transparent;\nborder-radius:none;")
        self.textBrowser.setObjectName("textBrowser")

        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(190, 510, 191, 41))
        font.setPointSize(16)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setStyleSheet("background:transparent;\nborder-radius:none;")
        self.textBrowser_2.setObjectName("textBrowser_2")

        # Start Button
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(710, 510, 91, 31))
        self.pushButton.setStyleSheet("font: 8pt \"Segoe Print\"; color: yellow;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Start")
        self.pushButton.clicked.connect(self.start_action)

        # Stop Button
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(840, 510, 81, 31))
        self.pushButton_2.setStyleSheet("font: 8pt \"Verdana\"; color: red;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setText("Stop")
        self.pushButton_2.clicked.connect(self.stop_action)

        jarvisUi.setCentralWidget(self.centralwidget)
        self.retranslateUi(jarvisUi)
        QtCore.QMetaObject.connectSlotsByName(jarvisUi)

    def retranslateUi(self, jarvisUi):
        _translate = QtCore.QCoreApplication.translate
        jarvisUi.setWindowTitle(_translate("jarvisUi", "JARVIS UI"))

    def start_action(self):
        self.textBrowser.setText("Starting JARVIS...")
        # Add any additional start functionality here

    def stop_action(self):
        self.textBrowser.setText("Stopping JARVIS...")
        # Add any additional stop functionality here


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    jarvisUi = QtWidgets.QMainWindow()
    ui = Ui_jarvisUi()
    ui.setupUi(jarvisUi)
    jarvisUi.show()
    sys.exit(app.exec_())
