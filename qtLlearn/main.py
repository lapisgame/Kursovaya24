from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget
from MainWindow import Ui_MainWindow  # импорт нашего сгенерированного файла9
import sys
 
class SecondaryWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Второе окно')
        # Здесь можно добавить дополнительные виджеты и настройки для второго окна

    def closeEvent(self, event):
        self.parent().show()  # При закрытии второго окна основное окно становится активным
        super().closeEvent(event)

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.LectureButton.clicked.connect(self.setupLectureWindow)
        self.ui.TaskButton.clicked.connect(self.setupTaskWindow)
        self.ui.SandboxButton.clicked.connect(self.setupSandboxWindow)
        self.ui.SettingsButton.clicked.connect(self.setupSettingsWindow)
        self.ui.AboutButton.clicked.connect(self.setupAboutWindow)

    def setupLectureWindow(self):
        self.secondary_window = SecondaryWindow()
        self.secondary_window.setParent(self, self.secondary_window.windowFlags())
        self.secondary_window.show()
        self.hide()  # Отключаем основное окно


    def setupTaskWindow(self):
        pass

    def setupSandboxWindow(self):
        pass

    def setupSettingsWindow(self):
        pass

    def setupAboutWindow(self):
        pass
        


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