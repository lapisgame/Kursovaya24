from PyQt6.QtWidgets import QWidget, QLabel
from PyQt6.QtGui import QFont

class AboutWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('О приложении')
        self.setFixedSize(1150, 800)

        self.font = QFont('JetBrains Mono', 26)

        self.Label1 = QLabel("1", self)
        self.Label1.setFont(self.font)
        self.Label1.setGeometry()

        self.Label2 = QLabel("2", self)
        self.Label2.setFont(self.font)
        self.Label2.setGeometry()

        self.Label3 = QLabel("3", self)
        self.Label3.setFont(self.font)
        self.Label3.setGeometry()


    def closeEvent(self, event):
        self.parent().show()
        super().closeEvent(event)