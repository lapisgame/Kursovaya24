from Scripts.DragAndDropLabel import *
from Scripts.DragTask import *
from Scripts.DragTaskModalWindow import *

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QPushButton
from Scripts.DragTaskModalWindow import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Main Window')

        self.second_window = None

        self.button = QPushButton('Open Dialog', self)
        self.button.setGeometry(150, 150, 100, 30)
        self.button.clicked.connect(self.openDialog)

    def openDialog(self):
        if self.second_window is None:
            self.second_window = DialogWindow()
        self.second_window.show()

app = QApplication([])
w = MainWindow()
w.show()

app.exec_()