# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editclass.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QHeaderView
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator
from dbserver.dbworker import DBWorker
from dbserver.classmanager import ClassManager


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.saveBtn = QtWidgets.QPushButton(self.centralwidget)
        self.saveBtn.setGeometry(QtCore.QRect(310, 360, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.saveBtn.setFont(font)
        self.saveBtn.setObjectName("saveBtn")
        self.backBtn = QtWidgets.QPushButton(self.centralwidget)
        self.backBtn.setGeometry(QtCore.QRect(50, 360, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.backBtn.setFont(font)
        self.backBtn.setObjectName("backBtn")
        self.classComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.classComboBox.setGeometry(QtCore.QRect(200, 40, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.classComboBox.setFont(font)
        self.classComboBox.setObjectName("classComboBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 40, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(80, 200, 331, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.highCheckBox = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.highCheckBox.setFont(font)
        self.highCheckBox.setText("")
        self.highCheckBox.setObjectName("highCheckBox")
        self.horizontalLayout.addWidget(self.highCheckBox)
        self.highLineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.highLineEdit.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.highLineEdit.setFont(font)
        self.highLineEdit.setObjectName("highLineEdit")
        self.horizontalLayout.addWidget(self.highLineEdit)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(80, 140, 331, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lowCheckBox = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lowCheckBox.setFont(font)
        self.lowCheckBox.setText("")
        self.lowCheckBox.setObjectName("lowCheckBox")
        self.horizontalLayout_2.addWidget(self.lowCheckBox)
        self.lowLineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lowLineEdit.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lowLineEdit.setFont(font)
        self.lowLineEdit.setObjectName("lowLineEdit")
        self.horizontalLayout_2.addWidget(self.lowLineEdit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.lowCheckBox.toggled['bool'].connect(self.lowLineEdit.setEnabled)
        self.highCheckBox.toggled['bool'].connect(self.highLineEdit.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Редактирование классов"))
        self.saveBtn.setText(_translate("MainWindow", "Сохранить"))
        self.backBtn.setText(_translate("MainWindow", "Назад"))
        self.label.setText(_translate("MainWindow", "Класс:"))
        self.label_3.setText(_translate("MainWindow", "Конечная цена:"))
        self.label_2.setText(_translate("MainWindow", "Начальная цена:"))
        self.onlyInt = QIntValidator()
        self.lowLineEdit.setValidator(self.onlyInt)
        self.highLineEdit.setValidator(self.onlyInt)

class EditClassWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def refreshData(self):
        self.classdata = self.CM.findall()
        self.classnames = [d['name'] for d in self.classdata]
        self.classnames.insert(0, '')

    def setClassCombo(self):
        self.refreshData()
        for i in self.classnames:
            self.classComboBox.addItem(str(i))

    def setWorkPlace(self, index):
        #if not self.classComboBox.currentIndex():
        self.lowLineEdit.setText('')
        self.highLineEdit.setText('')
        if not index:
            self.lowCheckBox.setChecked(False)
            self.lowCheckBox.setEnabled(False)
            self.highCheckBox.setChecked(False)
            self.highCheckBox.setEnabled(False)
        else:
            self.lowCheckBox.setEnabled(True)
            self.highCheckBox.setEnabled(True)
            bordlow = self.classdata[index-1]['bordlow']
            if bordlow:
                self.lowCheckBox.setChecked(True)
                self.lowLineEdit.setText(str(bordlow))
            else:
                self.lowCheckBox.setChecked(False)

            bordhigh = self.classdata[index - 1]['bordhigh']
            if bordhigh:
                self.highCheckBox.setChecked(True)
                self.highLineEdit.setText(str(bordhigh))
            else:
                self.highCheckBox.setChecked(False)

    def saveAll(self):
        obj = self.classdata[self.classComboBox.currentIndex()-1]
        id = obj['id']
        bordlow = -1
        if self.lowCheckBox.isChecked():
            textbordlow = self.lowLineEdit.text()
            try:
                bordlow = int(textbordlow)
                if bordlow < 0:
                    raise Exception('int under zero')
            except:
                bordlow = -1
        self.CM.updatebordlow(id, bordlow)
        bordhigh = -1
        if self.highCheckBox.isChecked():
            textbordhigh = self.highLineEdit.text()
            try:
                bordhigh = int(textbordhigh)
                if bordhigh < 0:
                    raise Exception('int under zero')
            except:
                bordhigh = -1
        self.CM.updatebordhigh(id, bordhigh)
        self.refreshData()
        self.setWorkPlace(self.classComboBox.currentIndex())

    def setConnect(self):
        self.classComboBox.currentIndexChanged.connect(self.setWorkPlace)
        self.saveBtn.clicked.connect(self.saveAll)
        self.backBtn.clicked.connect(self.returnM)

    def returnM(self):
        self.close()
        if self.parent():
            self.parent().show()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.dbw = DBWorker()
        self.CM = ClassManager(self.dbw)

        self.setupUi(self)
        self.setConnect()
        self.setClassCombo()
        self.setWorkPlace(0)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    #MainWindow = QtWidgets.QMainWindow()
    #ui = Ui_MainWindow()
    #ui.setupUi(MainWindow)
    editcharwin = EditClassWindow()
    editcharwin.show()
    sys.exit(app.exec_())
