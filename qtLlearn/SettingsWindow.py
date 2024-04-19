from PyQt6.QtWidgets import QWidget, QLabel, QComboBox
from PyQt6.QtGui import QFont

import json

class SettingsWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('Настройки')
        self.setFixedSize(1150, 800)
        
        self.Label1 = QLabel(self)
        self.Label1.setText('Размер шрифта')

        font = QFont()
        font.setPointSize(20)
        self.Label1.setFont(font)
        self.Label1.setGeometry(30, 30, 200, 35)

        self.comboBoxFontSize = QComboBox(self)
        self.comboBoxFontSize.addItems(['12','14','15','16','17','18','19','20','21','22','23','24'])
        self.comboBoxFontSize.setGeometry(250, 40, 40, 20)

        # Загрузка начального значения fontSize из config.json
        self.load_font_size()

        self.comboBoxFontSize.currentTextChanged.connect(self.update_font_size)

    def closeEvent(self, event):
        self.parent().show()
        super().closeEvent(event)

    # Получение данных из json
    def load_font_size(self):
        try:
            with open('config.json', 'r') as config_file:
                config = json.load(config_file)
                font_size = config.get('fontSize')
                index = self.comboBoxFontSize.findText(font_size)
                if index != -1:
                    self.comboBoxFontSize.setCurrentIndex(index)
        except FileNotFoundError:
            print("Файл config.json не найден.")
        except json.JSONDecodeError:
            print("Ошибка при разборе JSON в файле config.json.")

    # Запись новых данных в json
    def update_font_size(self, font_size):
        try:
            with open('config.json', 'w') as config_file:
                json.dump({'fontSize': font_size}, config_file)

        except Exception as e:
            print(f"Ошибка при записи в файл config.json: {e}")