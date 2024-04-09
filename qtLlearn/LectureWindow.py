from PyQt6.QtWidgets import QWidget, QGroupBox, QTextBrowser, QPushButton

class LectureWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('Лекции')
        self.setFixedSize(1150, 800)

        self.groupBox = QGroupBox('Моя GroupBox', self)  # Создаем GroupBox
        self.groupBox.setGeometry(10, 0, 200, 790)

        self.button = QPushButton('Моя кнопка', self.groupBox)
        self.button.setGeometry(10, 20, 100, 30)

        self.plainTextEdit = QTextBrowser(self)
        self.plainTextEdit.setGeometry(210, 10, 930, 780)

    def closeEvent(self, event):
        self.parent().show()
        super().closeEvent(event)