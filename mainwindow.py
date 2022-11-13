import time

from PyQt5 import QtCore, QtGui, QtWidgets

from drawing import Drawing

class Ui_MatplotlibWindow(object):
    def setupUi(self, MatplotlibWindow):
        MatplotlibWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        MatplotlibWindow.setObjectName("MatplotlibWindow")
        MatplotlibWindow.setEnabled(True)
        MatplotlibWindow.resize(1043, 506)
        MatplotlibWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MatplotlibWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.backgorund = QtWidgets.QLabel(self.centralwidget)
        self.backgorund.setEnabled(True)
        self.backgorund.setGeometry(QtCore.QRect(0, 0, 1051, 511))
        font = QtGui.QFont()
        self.backgorund.setFont(font)
        self.backgorund.setAutoFillBackground(False)
        self.backgorund.setText("")
        self.backgorund.setPixmap(QtGui.QPixmap(":/stockes/resources/whiteBackground.png"))
        self.backgorund.setObjectName("backgorund")
        self.closeBtn = QtWidgets.QPushButton(self.centralwidget)
        self.closeBtn.setGeometry(QtCore.QRect(1000, 30, 20, 21))
        self.closeBtn.setIcon(QtGui.QIcon('./resources/close.png'))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closeBtn.sizePolicy().hasHeightForWidth())
        self.closeBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("IROicons")
        font.setPointSize(21)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.closeBtn.setFont(font)
        self.closeBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.closeBtn.setToolTip("")
        self.closeBtn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.closeBtn.setStyleSheet("border-radius:10px;\n"
                                    "color: #710101;\n"
                                    "text-align: left;\n"
                                    "font: 21pt \"IROicons\";")
        self.closeBtn.setCheckable(False)
        self.closeBtn.setDefault(False)
        self.closeBtn.setFlat(False)
        self.closeBtn.setObjectName("closeBtn")
        self.miniBtn = QtWidgets.QPushButton(self.centralwidget)
        self.miniBtn.setGeometry(QtCore.QRect(970, 30, 20, 21))
        self.miniBtn.setIcon(QtGui.QIcon('./resources/Minimize.png'))
        font = QtGui.QFont()
        font.setFamily("IROicons")
        font.setPointSize(21)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.miniBtn.setFont(font)
        self.miniBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.miniBtn.setStyleSheet("border-radius:10px;\n"
                                    "color: #000;\n"
                                    "text-align: left;\n"
                                    "font: 21pt \"IROicons\";")
        self.miniBtn.setObjectName("miniBtn")
        self.lineWVal = QtWidgets.QLabel(self.centralwidget)
        self.lineWVal.setGeometry(QtCore.QRect(1060, 829, 111, 16))
        font = QtGui.QFont()
        self.lineWVal.setFont(font)
        self.lineWVal.setObjectName("lineWVal")
        self.menu = QtWidgets.QGroupBox(self.centralwidget)
        self.menu.setGeometry(QtCore.QRect(50, -115, 121, 111))
        self.menu.setStyleSheet("background-color:  #fff;\n"
                                "border-radius: 15px;")
        self.menu.setTitle("")
        self.menu.setObjectName("menu")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.menu)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 121, 111))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.menuNew = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.menuNew.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "color: rgb(0, 0, 0);\n"
                                    "font: 9pt \"Montserrat\";")
        self.menuNew.setObjectName("menuNew")
        self.verticalLayout.addWidget(self.menuNew)
        self.menuOpen = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.menuOpen.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "color: rgb(0, 0, 0);\n"
                                    "font: 9pt \"Montserrat\";")
        self.menuOpen.setObjectName("menuOpen")
        self.verticalLayout.addWidget(self.menuOpen)
        self.menuSave = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.menuSave.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "color: rgb(0, 0, 0);\n"
                                    "font: 9pt \"Montserrat\";")
        self.menuSave.setObjectName("menuSave")
        self.verticalLayout.addWidget(self.menuSave)
        self.graph_widget = MpWidget(self.centralwidget)
        self.graph_widget.setGeometry(QtCore.QRect(318, 60, 711, 431))
        self.graph_widget.setStyleSheet("background-color: #ffffff;\n"
                                        "border-radius: 20px;\n"
                                        "border-top-right-radius: 0px;\n"
                                        "border-bottom-right-radius: 0px;")
        self.graph_widget.setObjectName("graph_widget")
        self.max_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.max_label_2.setGeometry(QtCore.QRect(20, 30, 841, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setWeight(75)
        self.max_label_2.setFont(font)
        self.max_label_2.setTextFormat(QtCore.Qt.PlainText)
        self.max_label_2.setObjectName("max_label_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 70, 300, 410))
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet("background-color: #ffffff;\n")
        self.widget.setObjectName("widget")
        self.signal3Checkbox = QtWidgets.QRadioButton(self.widget)
        self.signal3Checkbox.setGeometry(QtCore.QRect(40, 125, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        self.signal3Checkbox.setFont(font)
        self.signal3Checkbox.setIconSize(QtCore.QSize(20, 20))
        self.signal3Checkbox.setObjectName("signal3Checkbox")
        self.signal2Checkbox = QtWidgets.QRadioButton(self.widget)
        self.signal2Checkbox.setGeometry(QtCore.QRect(40, 90, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        self.signal2Checkbox.setFont(font)
        self.signal2Checkbox.setIconSize(QtCore.QSize(20, 20))
        self.signal2Checkbox.setObjectName("signal2Checkbox")
        self.signal1Checkbox = QtWidgets.QRadioButton(self.widget)
        self.signal1Checkbox.setGeometry(QtCore.QRect(40, 55, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        self.signal1Checkbox.setFont(font)
        self.signal1Checkbox.setIconSize(QtCore.QSize(20, 20))
        self.signal1Checkbox.setChecked(True)
        self.signal1Checkbox.setObjectName("signal1Checkbox")
        self.max_label_3 = QtWidgets.QLabel(self.widget)
        self.max_label_3.setGeometry(QtCore.QRect(20, 20, 261, 31))
        self.graph_type = QtWidgets.QLabel(self.widget)
        self.graph_type.setGeometry(QtCore.QRect(20, 180, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setWeight(75)
        self.max_label_3.setFont(font)
        self.max_label_3.setTextFormat(QtCore.Qt.PlainText)
        self.max_label_3.setObjectName("max_label_3")
        self.graph_type.setFont(font)
        self.graph_type.setTextFormat(QtCore.Qt.PlainText)
        self.graph_type.setObjectName("graph_type")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(60, 300, 180, 40))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        MatplotlibWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MatplotlibWindow)
        self.closeBtn.clicked.connect(MatplotlibWindow.close)
        self.miniBtn.clicked.connect(MatplotlibWindow.showMinimized)
        QtCore.QMetaObject.connectSlotsByName(MatplotlibWindow)

    def retranslateUi(self, MatplotlibWindow):
        _translate = QtCore.QCoreApplication.translate
        MatplotlibWindow.setWindowTitle(_translate("MatplotlibWindow", "MainWindow"))
        self.closeBtn.setText(_translate("MatplotlibWindow", "x"))
        self.miniBtn.setText(_translate("MatplotlibWindow", "y"))
        self.lineWVal.setText(_translate("MatplotlibWindow", "Line Weight: 0"))
        self.menuNew.setToolTip(_translate("MatplotlibWindow", "<html><head/><body><p>Make a New Draw</p></body></html>"))
        self.menuNew.setText(_translate("MatplotlibWindow", "New"))
        self.menuOpen.setToolTip(_translate("MatplotlibWindow", "<html><head/><body><p>Open a Draw</p></body></html>"))
        self.menuOpen.setText(_translate("MatplotlibWindow", "Open"))
        self.menuSave.setToolTip(_translate("MatplotlibWindow", "<html><head/><body><p>Save a Draw</p></body></html>"))
        self.menuSave.setText(_translate("MatplotlibWindow", "Save"))
        self.max_label_2.setText(_translate("MatplotlibWindow", "Welcome to Multi-signals Monitor"))
        self.signal3Checkbox.setText(_translate("MatplotlibWindow", "Signal 3"))
        self.signal2Checkbox.setText(_translate("MatplotlibWindow", "Signal 2"))
        self.signal1Checkbox.setText(_translate("MatplotlibWindow", "Signal 1"))
        self.max_label_3.setText(_translate("MatplotlibWindow", "Select Your Signal:"))
        self.graph_type.setText(_translate("MatplotlibWindow", "Select Graph Type:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "X-bar Chart"))
        self.comboBox.setItemText(1, _translate("MainWindow", "R Chart"))

        self._percentage = 0
        timer = QtCore.QTimer(MatplotlibWindow, interval=100, timeout=self.handle_timeout)
        timer.start()
        self.handle_timeout()

    @property
    def percentage(self):
        return self._percentage

    def handle_timeout(self):
        self.update_graph()

    def update_graph(self):
        selectedSignal = 1
        selectedGraph = 2

        # Get The Graph Type
        graphType = self.comboBox.currentText()
        if graphType == "R Chart":
            selectedGraph = 2
        else:
            selectedGraph = 1

        # Get The Signal Type
        if self.signal1Checkbox.isChecked():
            selectedSignal = 1

        if self.signal2Checkbox.isChecked():
            selectedSignal = 2

        if self.signal3Checkbox.isChecked():
            selectedSignal = 3

        drawing = Drawing()

        signal, upper_limit, mean_line,lower_limit, alarm_flag = drawing.get_data_frame(graph_type = selectedGraph, 
                                                                    signal_type = selectedSignal)
        self.graph_widget.canvas.axes.clear()
        self.graph_widget.canvas.axes.plot(signal,linestyle='-', marker='o')
        self.graph_widget.canvas.axes.axhline(upper_limit,color="red")
        self.graph_widget.canvas.axes.axhline(mean_line,color="green")
        self.graph_widget.canvas.axes.axhline(lower_limit,color="red")
        self.graph_widget.canvas.axes.set_ylim(-0.5,1.6)


        self.graph_widget.canvas.draw()

from mpwidget import MpWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MatplotlibWindow = QtWidgets.QMainWindow()
    ui = Ui_MatplotlibWindow()
    ui.setupUi(MatplotlibWindow)
    MatplotlibWindow.show()
    sys.exit(app.exec_())
