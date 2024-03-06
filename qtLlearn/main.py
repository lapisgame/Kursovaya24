from PyQt5.QtWidgets import QMainWindow, QApplication
from MainWindow import Ui_MainWindow  # импорт нашего сгенерированного файла9
import sys
 

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
        pass

    def setupTaskWindow(self):
        pass

    def setupSandboxWindow(self):
        pass

    def setupSettingsWindow(self):
        pass

    def setupAboutWindow(self):
        pass

    
 
app = QApplication([])
application = MainWindow()
application.show()
 
sys.exit(app.exec())