from PyQt5 import QtCore, QtGui, QtWidgets
from uiservice.addchar import AddCharWindow
from uiservice.editchar import EditCharWindow
from uiservice.addavto import AddAvtoWindow
from uiservice.addavch import AddAvtoCharWindow
from uiservice.editavch_ import EditAvtoCharWindow
from uiservice.classdet import ClassDetWindow
from uiservice.addclass import AddClassWindow
from uiservice.editclass import EditClassWindow
from uiservice.checkdb import CheckWindow


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 120, 251, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 160, 251, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(130, 200, 251, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(130, 240, 251, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(130, 280, 251, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(130, 320, 251, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(130, 360, 251, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(130, 80, 251, 31))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(130, 40, 251, 31))
        self.pushButton_9.setObjectName("pushButton_9")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "?????????????????????????? ??????????????????????"))
        self.pushButton.setText(_translate("MainWindow", "???????????????????? ??????????????????????????"))
        self.pushButton_2.setText(_translate("MainWindow", "?????????????????? ??????????????????????????"))
        self.pushButton_3.setText(_translate("MainWindow", "???????????????????? ??????????????????????"))
        self.pushButton_4.setText(_translate("MainWindow", "???????????????????? ?????????????????????????? ??????????????????"))
        self.pushButton_5.setText(_translate("MainWindow", "???????????????????? ???????????????? ???????????????????? "))
        self.pushButton_6.setText(_translate("MainWindow", "???????????????? ??????????????????????"))
        self.pushButton_7.setText(_translate("MainWindow", "??????????????????????????"))
        self.pushButton_8.setText(_translate("MainWindow", "?????????????????? ??????????????"))
        self.pushButton_9.setText(_translate("MainWindow", "???????????????????? ??????????????"))

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.openAddChar)
        self.pushButton_2.clicked.connect(self.openEditChar)
        self.pushButton_3.clicked.connect(self.openAddAvto)
        self.pushButton_4.clicked.connect(self.openAddAvtoChar)
        self.pushButton_5.clicked.connect(self.openEditAvtoChar)
        self.pushButton_7.clicked.connect(self.openClassDet)
        self.pushButton_8.clicked.connect(self.openEditClass)
        self.pushButton_9.clicked.connect(self.openAddClass)
        self.pushButton_6.clicked.connect(self.openCheck)

    def openAddChar(self):
        self.close()
        self.AddCharW = AddCharWindow(self)
        self.AddCharW.show()

    def openEditChar(self):
        self.close()
        self.EditCharW = EditCharWindow(self)
        self.EditCharW.show()

    def openAddAvto(self):
        self.close()
        self.AddAvtoW = AddAvtoWindow(self)
        self.AddAvtoW.show()

    def openAddAvtoChar(self):
        self.close()
        self.AddAvtoCharW = AddAvtoCharWindow(self)
        self.AddAvtoCharW.show()

    def openEditAvtoChar(self):
        self.close()
        self.EditAvtoCharW = EditAvtoCharWindow(self)
        self.EditAvtoCharW.show()

    def openClassDet(self):
        self.close()
        self.ClassDetW = ClassDetWindow(self)
        self.ClassDetW.show()

    def openAddClass(self):
        self.close()
        self.AddClassW = AddClassWindow(self)
        self.AddClassW.show()

    def openEditClass(self):
        self.close()
        self.EditClassW = EditClassWindow(self)
        self.EditClassW.show()

    def openCheck(self):
        self.close()
        self.CheckW = CheckWindow(self)
        self.CheckW.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    #MainWindow = QtWidgets.QMainWindow()
    #ui = Ui_MainWindow()
    #ui.setupUi(MainWindow)
    mainwin = MainWindow()
    mainwin.show()
    sys.exit(app.exec_())