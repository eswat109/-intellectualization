from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget

import sys

class CharTableWidget (QTableWidget):
    pass

def application():
    app = QApplication(sys.argv)
    window = QMainWindow()

    window.setWindowTitle("Sample title")
    window.setGeometry(300, 250, 600, 400)

    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    application()