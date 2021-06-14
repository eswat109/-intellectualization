from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QHeaderView
from PyQt5.QtCore import Qt
from dbserver.classmanager import ClassManager
from dbserver.dbworker import DBWorker


class Ui_MainWindow(object):
    def addtotable(self, value: str):
        pass

    def setuptable(self):
        data = self.CM.findall()
        titles = self.CM.gettitles()
        self.tableWidget.setColumnCount(len(titles))
        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setHorizontalHeaderLabels(titles)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        for i, d in enumerate(data):
            for j in range(len(titles)):
                value = str(d[titles[j]])
                item = QtWidgets.QTableWidgetItem(value)
                item.setTextAlignment(Qt.AlignCenter)
                item.setFlags(item.flags() & ~QtCore.Qt.ItemFlag.ItemIsEditable)
                self.tableWidget.setItem(i, j, item)

        self.tableWidget.setColumnHidden(0, True)
        self.tableWidget.setColumnHidden(2, True)
        self.tableWidget.setColumnHidden(3, True)

    def addrowtable(self, value: str):
        self.CM.addbyname(value)
        self.setuptable()

    def delrowtable(self):
        row = self.tableWidget.currentRow()
        item = self.tableWidget.item(row, 0)
        id = item.text()
        self.CM.deletebyid(int(id))
        self.setuptable()

    def setupUi(self, MainWindow):
        dbw = DBWorker()
        self.CM = ClassManager(dbw)
        self.__data = self.CM.findall()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(492, 492)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(40, 90, 321, 281))
        self.tableWidget.setObjectName("tableWidget")
        self.setuptable()

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(40, 30, 291, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(370, 30, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 90, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 400, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 492, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Классы"))
        self.pushButton.setText(_translate("MainWindow", "Добавить"))
        self.pushButton.clicked.connect(lambda: self.addrowtable(self.lineEdit.text()))
        self.pushButton_2.setText(_translate("MainWindow", "Удалить"))
        self.pushButton_2.clicked.connect(lambda: self.delrowtable())
        self.pushButton_3.setText(_translate("MainWindow", "Назад"))



class AddCharWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButton_3.clicked.connect(self.returnM)

    def returnM(self):
        self.close()
        if self.parent():
            self.parent().show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    #MainWindow = QtWidgets.QMainWindow()
    #ui = Ui_MainWindow()
    #ui.setupUi(MainWindow)
    addcharwin = AddCharWindow()
    addcharwin.show()
    sys.exit(app.exec_())