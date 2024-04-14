from PyQt6.QtWidgets import QWidget, QGroupBox, QTextBrowser, QPushButton, QVBoxLayout, QSpacerItem, QSizePolicy

import json
import os

class LectureWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('Лекции')
        self.setFixedSize(1150, 800)

        self.groupBox = QGroupBox('Выбор Лекции', self)
        self.groupBox.setGeometry(10, 0, 200, 790)

        self.initLectureButtons()

        self.plainTextEdit = QTextBrowser(self)
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
    
    def openLecture(self, path):
        f = open(path, 'r', encoding='utf-8')
        data = json.load(f)

        fontsize = 14
        style = """<style>
                        * {
                            font-size:" + str(fontsize) + "pt
                        } 
                        pre {
                            margin:0;
                            padding:0;
                            line-height: 0.8
                        }
                </style>"""
    
        content = f"{style}{data['content']}"
        # Установка HTML-контента
        self.plainTextEdit.setHtml(content)
