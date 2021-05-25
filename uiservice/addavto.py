# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addavto.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QHeaderView
from PyQt5.QtCore import Qt
from dbserver.avtomanager import AvtoManager


class Ui_MainWindow(object):

    def setuptable(self):
        data = self.AM.findall()
        titles = self.AM.gettitles()
        titles_ = ['Номер', 'Цена']
        self.tableWidget.setColumnCount(len(titles))
        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setHorizontalHeaderLabels(titles_)
        titles = self.AM.gettitles()
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        for i, d in enumerate(data):
            for j in range(len(titles)):
                value = str(d[titles[j]])
                item = QtWidgets.QTableWidgetItem(value)
                item.setTextAlignment(Qt.AlignCenter)
                item.setFlags(item.flags() & ~QtCore.Qt.ItemFlag.ItemIsEditable)
                self.tableWidget.setItem(i, j, item)

        #self.tableWidget.setColumnHidden(0, True)
        self.tableWidget.setColumnHidden(2, True)

    def isInt(self, s: str):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def addrowtable(self, id: str, value: str):
        if not(self.isInt(id) and self.isInt(value)):
            return
        self.AM.addbyidprice(int(id), int(value))
        self.setuptable()

    def delrowtable(self):
        row = self.tableWidget.currentRow()
        item = self.tableWidget.item(row, 0)
        id = item.text()
        self.AM.deletebyid(int(id))
        self.setuptable()

    def setupUi(self, MainWindow):
        self.AM = AvtoManager()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(60, 420, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(390, 20, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(390, 110, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(220, 20, 131, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(60, 110, 321, 301))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label_Type = QtWidgets.QLabel(self.centralwidget)
        self.label_Type.setGeometry(QtCore.QRect(50, 70, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_Type.setFont(font)
        self.label_Type.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_Type.setObjectName("label_Type")
        self.label_Char = QtWidgets.QLabel(self.centralwidget)
        self.label_Char.setGeometry(QtCore.QRect(50, 30, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_Char.setFont(font)
        self.label_Char.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_Char.setObjectName("label_Char")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(220, 60, 131, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_3.setText(_translate("MainWindow", "Назад"))
        self.pushButton.setText(_translate("MainWindow", "Добавить"))
        self.pushButton_2.setText(_translate("MainWindow", "Удалить"))
        self.label_Type.setText(_translate("MainWindow", "Цена"))
        self.label_Char.setText(_translate("MainWindow", "Номер"))

        self.pushButton.clicked.connect(lambda: self.addrowtable(self.lineEdit.text(), self.lineEdit_2.text()))
        self.pushButton_2.clicked.connect(lambda: self.delrowtable())


class AddAvtoWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setuptable()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    #MainWindow = QtWidgets.QMainWindow()
    #ui = Ui_MainWindow()
    #ui.setupUi(MainWindow)
    addavtowin = AddAvtoWindow()
    addavtowin.show()
    sys.exit(app.exec_())