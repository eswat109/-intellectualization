
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHeaderView
from dbserver.charmanager import CharManager
from dbserver.avtomanager import AvtoManager
from dbserver.avtocharmanager import AvtoCharManager
from dbserver.classmanager import ClassManager
from dbserver.dbworker import DBWorker


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 20, 431, 251))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 280, 151, 16))
        self.label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 300, 151, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 280, 55, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(190, 300, 55, 16))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(320, 280, 131, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 420, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 320, 431, 91))
        self.textBrowser.setObjectName("textBrowser")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "??????????????????????????"))
        """self.label.setText(_translate("MainWindow", "???????????????????????????? ???????? ????"))
        self.label_2.setText(_translate("MainWindow", "????"))
        self.label_3.setText(_translate("MainWindow", "None"))
        self.label_4.setText(_translate("MainWindow", "None"))"""
        self.pushButton.setText(_translate("MainWindow", "????????????????????????????????"))
        self.pushButton_2.setText(_translate("MainWindow", "??????????"))

class ClassDetWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.dbwC = DBWorker()
        self.manC = CharManager(self.dbwC)
        self.setupUi(self)
        self.setTable()
        self.connection()

    def connection(self):
        self.pushButton_2.clicked.connect(self.returnM)
        self.pushButton.clicked.connect(lambda: self.doClass())

    def setTable(self):
        self.chardata = self.manC.findall()
        titles = ['??????????????', '??????????????????????', '????????????????']
        self.tableWidget.setColumnCount(len(titles))
        self.tableWidget.setRowCount(len(self.chardata))
        self.tableWidget.setHorizontalHeaderLabels(titles)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        for i, d in enumerate(self.chardata):
            name = str(d['name'])
            cvalue = self.manC.__splitvalues__(d['cvalues'])
            type = d['type']
            item = QtWidgets.QTableWidgetItem(name)
            item.setTextAlignment(Qt.AlignCenter)
            item.setFlags(item.flags() & ~QtCore.Qt.ItemFlag.ItemIsEditable)
            self.tableWidget.setItem(i, 0, item)

            checkBox = QtWidgets.QCheckBox()
            checkBox.index = i
            if not type or not cvalue:
                checkBox.setChecked(True)
                checkBox.setEnabled(False)
            checkBox.stateChanged.connect(lambda: self.chbIsChanged(int(i)))
            self.tableWidget.setCellWidget(i, 1, checkBox)

            if not type:
                item = QtWidgets.QTableWidgetItem('?????? ????????')
                item.setFlags(item.flags() & ~QtCore.Qt.ItemFlag.ItemIsEditable)
                self.tableWidget.setItem(i, 2, item)
            elif type == 'int':
                spinBox = QtWidgets.QSpinBox()
                if len(cvalue) < 2 or not cvalue[0] or not cvalue[1]:
                    checkBox.setChecked(True)
                    checkBox.setEnabled(False)
                    spinBox.setEnabled(False)
                else:
                    spinBox.setMinimum(int(cvalue[0]))
                    spinBox.setMaximum(int(cvalue[1]))
                self.tableWidget.setCellWidget(i, 2, spinBox)
            elif type == 'log':
                comboBoxLog = QtWidgets.QComboBox()
                comboBoxLog.index = i
                if not cvalue:
                    checkBox.setChecked(True)
                    checkBox.setEnabled(False)
                    comboBoxLog.setEnabled(False)
                else:
                    for val in cvalue:
                        comboBoxLog.addItem(val)
                self.tableWidget.setCellWidget(i, 2, comboBoxLog)
            elif type == 'enum':
                comboBoxEnum = QtWidgets.QComboBox()
                comboBoxEnum.index = i
                if not cvalue:
                    checkBox.setChecked(True)
                    checkBox.setEnabled(False)
                    comboBoxEnum.setEnabled(False)
                else:
                    for val in cvalue:
                        comboBoxEnum.addItem(val)
                self.tableWidget.setCellWidget(i, 2, comboBoxEnum)

    def chbIsChanged(self, ind: int):
        chb = self.sender()
        row = chb.index
        widget = self.tableWidget.cellWidget(row, 2)
        if widget:
            if chb.isChecked():
                widget.setEnabled(False)
            else:
                widget.setEnabled(True)

    def getObjFTable(self) -> dict:
        tmpdict = {}
        for i in range(self.tableWidget.rowCount()):
            name = self.tableWidget.item(i, 0).text()
            cbx = self.tableWidget.cellWidget(i, 1)
            widget = self.tableWidget.cellWidget(i, 2)
            if cbx.isChecked():
                tmpdict[name] = 'None'
            else:
                try:
                    tmpdict[name] = widget.text()
                except:
                    tmpdict[name] = widget.currentText()
        return tmpdict

    def doClass(self):
        obj = self.getObjFTable()
        all = self.dbwC.getall()
        pchars = self.dbwC.pricechars(all)
        prices = self.dbwC.getprices(obj, pchars)
        logs = ''
        if not prices:
            logs = '???????????????????????????? ???????? ????????????????????????.\n'
            '''self.label_3.setText("None")
            self.label_4.setText("None")'''
        else:
            mn = min(prices)
            mx = max(prices)
            logs = '???????????????????????????? ???????? ???? {} ???? {}.\n'.format(mn, mx)
            logs += '???????????????????? ????????????:\n'
            classes = ClassManager(DBWorker()).findall()
            for cl in classes:
                if not cl.get('bordlow') and not cl.get('bordhigh'):
                    logs += '{}: ???????? ?? ?????????????????? ???? 0 ???? ??????????????????????????'.format(cl['name'])
                elif cl.get('bordlow') and not cl.get('bordhigh'):
                    if mn >= cl.get('bordlow') or mx >= cl.get('bordlow'):
                        logs += '{}: ???????? ?? ?????????????????? ???? {} ???? ??????????????????????????'.format(cl['name'], cl.get('bordlow'))
                elif not cl.get('bordlow') and cl.get('bordhigh'):
                    if mn <= cl.get('bordhigh') or mx <= cl.get('bordhigh'):
                        logs += '{}: ???????? ?? ?????????????????? ???? 0 ???? {}'.format(cl['name'], cl.get('bordhigh'))
                elif cl.get('bordlow') and cl.get('bordhigh'):
                    if mn >= cl.get('bordlow') and mx <= cl.get('bordhigh'):
                        logs += '{}: ???????? ?? ?????????????????? ???? {} ???? {}'.format(cl['name'], cl.get('bordlow'), cl.get('bordhigh'))
            '''self.label_3.setText(str(mn))
            self.label_4.setText(str(mx))'''
        self.textBrowser.setText(logs)
        #print(prices)


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
    addcharwin = ClassDetWindow()
    addcharwin.show()
    sys.exit(app.exec_())