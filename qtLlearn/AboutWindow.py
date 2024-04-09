from PyQt6.QtWidgets import QWidget

class AboutWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('О приложении')
        self.setFixedSize(1150, 800)

    def closeEvent(self, event):
        self.parent().show()
        super().closeEvent(event)