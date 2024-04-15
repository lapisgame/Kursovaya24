from PyQt6.QtWidgets import QWidget, QGroupBox, QLabel, QTextBrowser, QPushButton, QVBoxLayout, QSpacerItem, QSizePolicy
from PyQt6.QtGui import QTextOption

import json
import os

class LectureWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('Лекции')
        self.setFixedSize(1150, 800)

        self.fontSize = self.getFontJson()

        self.groupBox = QGroupBox('Выбор Лекции', self)
        self.groupBox.setGeometry(10, 0, 200, 790)

        self.initLectureButtons()

        self.plainTextEdit = QTextBrowser(self)
        self.plainTextEdit.setWordWrapMode(QTextOption.WrapMode.WordWrap)
        self.plainTextEdit.setGeometry(210, 10, 930, 780)

    def closeEvent(self, event):
        self.parent().show()
        super().closeEvent(event)

    def initLectureButtons(self):
        layout = QVBoxLayout()
        # Путь к папке с лекциями
        lectures_path = os.path.join(os.getcwd(), 'Lectures')

        files = [''] * len(os.listdir(lectures_path))

        # Перебор всех файлов в папке Lectures
        for filename in os.listdir(lectures_path):
            if filename.endswith('.json'):
                file_path = os.path.join(lectures_path, filename)
                with open(file_path, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    index = data.get('index', '-1')
                    files[int(index)] = file_path

        # Перебор всех файлов в папке Lectures
        for file_path in files:
            if file_path != '':
                with open(file_path, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    title = data.get('title', 'No Title')
                    
                    # Создание кнопки для каждой лекции
                    button = QPushButton(title)
                    button.clicked.connect(lambda checked, path=file_path: self.openLecture(path))
                    layout.addWidget(button)

        # Добавление растягивающего элемента в конец макета, чтобы вытолкнуть кнопки вверх
        spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        layout.addItem(spacer)

        self.groupBox.setLayout(layout)
    
    def getFontJson(self):
        config_file_path = 'config.json'
        try:
            with open(config_file_path, 'r') as config_file:
                config = json.load(config_file)
                font_size = config.get('fontSize')
                return font_size
        except FileNotFoundError:
            print(f"Файл {config_file_path} не найден.")
        except json.JSONDecodeError:
            print(f"Ошибка при разборе JSON в файле {config_file_path}.")


    def openLecture(self, path):
        f = open(path, 'r', encoding='utf-8')
        data = json.load(f)

        style = """<style>
                        * {
                            font-size:""" + str(self.fontSize) + """pt;
                        } 
                        pre {
                            line-height: 1.25;
                            max-width: 760 px;
                            font-size:""" + str(self.fontSize) + """pt;
                            max-width: 760px;
                            white-space: pre-wrap;
                            word-wrap: break-word;
                            overflow-x: auto;
                        }
                </style>"""
    
        content = f"{style}{data['content']}"
        self.plainTextEdit.setHtml(content)
