from PyQt6.QtWidgets import QWidget

class TaskWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('Задачи')
        self.setFixedSize(1150, 800)

    def closeEvent(self, event):
        self.parent().show()
        super().closeEvent(event)