# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editavch.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 401)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 80, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 120, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 160, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.comboBoxAvto = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxAvto.setGeometry(QtCore.QRect(240, 80, 181, 22))
        self.comboBoxAvto.setObjectName("comboBoxAvto")
        self.comboBoxChar = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxChar.setGeometry(QtCore.QRect(240, 120, 181, 22))
        self.comboBoxChar.setObjectName("comboBoxChar")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 310, 91, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 310, 91, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 310, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(130, 160, 321, 91))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_Empty = QtWidgets.QWidget()
        self.tab_Empty.setObjectName("tab_Empty")
        self.tabWidget.addTab(self.tab_Empty, "")
        self.tabInt = QtWidgets.QWidget()
        self.tabInt.setObjectName("tabInt")
        self.spinBox = QtWidgets.QSpinBox(self.tabInt)
        self.spinBox.setGeometry(QtCore.QRect(160, 20, 111, 22))
        self.spinBox.setObjectName("spinBox")
        self.tabWidget.addTab(self.tabInt, "")
        self.tabLog = QtWidgets.QWidget()
        self.tabLog.setObjectName("tabLog")
        self.comboBoxValue = QtWidgets.QComboBox(self.tabLog)
        self.comboBoxValue.setGeometry(QtCore.QRect(110, 20, 181, 22))
        self.comboBoxValue.setObjectName("comboBoxValue")
        self.tabWidget.addTab(self.tabLog, "")
        self.tabEnum = QtWidgets.QWidget()
        self.tabEnum.setObjectName("tabEnum")
        self.comboBoxValue_2 = QtWidgets.QComboBox(self.tabEnum)
        self.comboBoxValue_2.setGeometry(QtCore.QRect(110, 20, 181, 22))
        self.comboBoxValue_2.setObjectName("comboBoxValue_2")
        self.tabWidget.addTab(self.tabEnum, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Значения характеристик"))
        self.label.setText(_translate("MainWindow", "Авто"))
        self.label_2.setText(_translate("MainWindow", "Характеристика"))
        self.label_3.setText(_translate("MainWindow", "Значение"))
        self.pushButton.setText(_translate("MainWindow", "Сохранить"))
        self.pushButton_2.setText(_translate("MainWindow", "Удалить"))
        self.pushButton_3.setText(_translate("MainWindow", "Назад"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Empty), _translate("MainWindow", "Empty"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabInt), _translate("MainWindow", "Int"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabLog), _translate("MainWindow", "Log"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabEnum), _translate("MainWindow", "Enum"))
