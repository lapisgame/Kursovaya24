from PyQt6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QLabel, QDialog

from MainWindow import Ui_MainWindow
from LectureWindow import LectureWindow
from TaskWindow import TaskWindow
from SandboxWindow import SandboxWindow
from SettingsWindow import SettingsWindow
from AboutWindow import AboutWindow

import sys
import time
import subprocess

class WaitDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Пожалуйста, подождите...')
        self.setFixedSize(200, 100)
        layout = QVBoxLayout()
        self.label = QLabel("Создаём лекции...")
        layout.addWidget(self.label)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        
        dialog = WaitDialog()
        dialog.show()

        result = subprocess.run(['python', 'transform.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        time.sleep(1)
        dialog.close()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.LectureButton.clicked.connect(self.setupLectureWindow)
        self.ui.TaskButton.clicked.connect(self.setupTaskWindow)
        self.ui.SandboxButton.clicked.connect(self.setupSandboxWindow)
        self.ui.SettingsButton.clicked.connect(self.setupSettingsWindow)
        self.ui.AboutButton.clicked.connect(self.setupAboutWindow)

    def setupLectureWindow(self):
        self.lecture_window = LectureWindow()
        self.lecture_window.setParent(self, self.lecture_window.windowFlags())
        self.lecture_window.show()
        self.hide()  # Отключаем основное окно


    def setupTaskWindow(self):
        self.task_window = TaskWindow()
        self.task_window.setParent(self, self.task_window.windowFlags())
        self.task_window.show()
        self.hide()  # Отключаем основное окно

    def setupSandboxWindow(self):
        self.sandbox_window = SandboxWindow()
        self.sandbox_window.setParent(self, self.sandbox_window.windowFlags())
        self.sandbox_window.show()
        self.hide()  # Отключаем основное окно

    def setupSettingsWindow(self):
        self.settings_window = SettingsWindow()
        self.settings_window.setParent(self, self.settings_window.windowFlags())
        self.settings_window.show()
        self.hide()  # Отключаем основное окно

    def setupAboutWindow(self):
        self.about_window = AboutWindow()
        self.about_window.setParent(self, self.about_window.windowFlags())
        self.about_window.show()
        self.hide()  # Отключаем основное окно
        


class NewWindow(QMainWindow):
    def __init__(self, main_window):
        super().__init__()
        self.setWindowTitle("Новое окно")
        self.main_window = main_window

    def closeEvent(self, event):
        # Включаем снова основное окно
        self.main_window.setEnabled(True)
        event.accept()

    
 
app = QApplication([])
application = MainWindow()
application.show()
 
sys.exit(app.exec())