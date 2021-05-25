# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editavch.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHeaderView
from dbserver.charmanager import CharManager
from dbserver.avtomanager import AvtoManager
from dbserver.avtocharmanager import AvtoCharManager
from dbserver.dbworker import DBWorker


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        self.dbwCM = DBWorker()
        self.dbwAM = DBWorker()
        self.dbwACM = DBWorker()
        self.manC = CharManager(self.dbwCM)
        self.manA = AvtoManager(self.dbwAM)
        self.manAC = AvtoCharManager(self.dbwACM)

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 401)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 80, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 120, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 160, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
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
        self.pushButton_2.setHidden(True)
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
        self.spinBoxInt = QtWidgets.QSpinBox(self.tabInt)
        self.spinBoxInt.setGeometry(QtCore.QRect(160, 20, 111, 22))
        self.spinBoxInt.setObjectName("spinBox")
        self.tabWidget.addTab(self.tabInt, "")
        self.tabLog = QtWidgets.QWidget()
        self.tabLog.setObjectName("tabLog")
        self.comboBoxLog = QtWidgets.QComboBox(self.tabLog)
        self.comboBoxLog.setGeometry(QtCore.QRect(110, 20, 181, 22))
        self.comboBoxLog.setObjectName("comboBoxValue")
        self.tabWidget.addTab(self.tabLog, "")
        self.tabEnum = QtWidgets.QWidget()
        self.tabEnum.setObjectName("tabEnum")
        self.comboBoxEnum = QtWidgets.QComboBox(self.tabEnum)
        self.comboBoxEnum.setGeometry(QtCore.QRect(110, 20, 181, 22))
        self.comboBoxEnum.setObjectName("comboBoxValue_2")
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

class EditAvtoCharWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def setComboAvto(self):
        self.avtodata = self.manA.findall()
        self.avtoids = [d['id'] for d in self.avtodata]
        self.avtoids.insert(0, '')
        for i in self.avtoids:
            self.comboBoxAvto.addItem(str(i))

    def clearAllWidgets(self):
        self.comboBoxAvto.clear()
        self.comboBoxChar.clear()
        self.comboBoxEnum.clear()
        self.comboBoxLog.clear()
        self.spinBoxInt.clear()
        self.tabWidget.setCurrentIndex(0)

    def changedComboAvto(self):
        ind = self.comboBoxAvto.currentIndex()
        self.curavtoobj = None
        if ind < 0:
            return
        elif ind:
            self.curavtoobj = self.manA.findbyid(int(self.avtoids[ind]))
        else:
            self.comboBoxChar.clear()
            self.comboBoxEnum.clear()
            self.comboBoxLog.clear()
            self.spinBoxInt.clear()
            self.tabWidget.setCurrentIndex(0)
            return
        self.setComboChar()

    def setComboChar(self):
        self.comboBoxChar.clear()
        avto_id = self.curavtoobj['id']
        self.chardata = self.manAC.findbyavto(avto_id)
        self.charnames = [self.manC.findbyid(cd['char'])['name'] for cd in self.chardata]
        self.charnames.insert(0, '')
        for i in self.charnames:
            self.comboBoxChar.addItem(str(i))

    def changedComboChar(self):
        ind = self.comboBoxChar.currentIndex()
        self.curcharobj = None
        if ind < 0:
            return
        elif ind:
            char_name = self.charnames[ind]
            self.curcharobj = self.manC.findbyname(char_name)[0]
        else:
            self.comboBoxEnum.clear()
            self.comboBoxLog.clear()
            self.spinBoxInt.clear()
            self.spinBoxInt.setEnabled(True)
            return
        self.setTabW()

    def setTabW(self):
        self.comboBoxEnum.clear()
        self.comboBoxLog.clear()
        self.spinBoxInt.clear()
        self.spinBoxInt.setEnabled(True)
        self.curavtocharobj = self.manAC.findbyavtochar(self.curavtoobj['id'], self.curcharobj['id'])[0]
        type = self.curcharobj['type']
        cvalues = self.manC.__splitvalues__(self.curcharobj['cvalues'])
        if not cvalues or (type in ['int', 'log'] and len(cvalues) == 1):
            self.tabWidget.setCurrentIndex(0)
            return
        value = self.curavtocharobj['value']
        if type == 'int':
            self.tabWidget.setCurrentIndex(1)
            if not cvalues[0] or not cvalues[1]:
                self.spinBoxInt.setEnabled(False)
                return
            self.spinBoxInt.setMinimum(int(cvalues[0]))
            self.spinBoxInt.setMaximum(int(cvalues[1]))
            if not value:
                value = cvalues[0]
            self.spinBoxInt.setValue(int(value))
        elif type == 'log':
            self.tabWidget.setCurrentIndex(2)
            for t in cvalues:
                self.comboBoxLog.addItem(t)
                if t == value:
                    self.comboBoxLog.setCurrentIndex(self.comboBoxLog.count()-1)
        elif type == 'enum':
            self.tabWidget.setCurrentIndex(3)
            for t in cvalues:
                self.comboBoxEnum.addItem(t)
                if t == value:
                    self.comboBoxEnum.setCurrentIndex(self.comboBoxEnum.count()-1)
        else:
            self.tabWidget.setCurrentIndex(0)

    def saveBtnClicked(self):
        value = ''
        itab = self.tabWidget.currentIndex()
        if itab == 0:
            return
        elif itab == 1:
            value = self.spinBoxInt.text()
        elif itab == 2:
            value = self.comboBoxLog.text()
        elif itab == 3:
            value = self.comboBoxEnum.text()
        self.manAC.updatevalue(self.curavtocharobj['id'], value)
        self.curavtocharobj = self.manAC.findbyid(self.curavtocharobj['id'])
        self.setTabW()



    def setConnect(self):
        self.pushButton.clicked.connect(self.saveBtnClicked)
        self.comboBoxAvto.currentIndexChanged.connect(self.changedComboAvto)
        self.comboBoxChar.currentIndexChanged.connect(self.changedComboChar)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setConnect()
        self.setComboAvto()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    #MainWindow = QtWidgets.QMainWindow()
    #ui = Ui_MainWindow()
    #ui.setupUi(MainWindow)
    addcharwin = EditAvtoCharWindow()
    addcharwin.show()
    sys.exit(app.exec_())