from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QTextEdit
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtGui import QFont
import contextlib
import io
import json

class SandboxWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('Песочница')
        self.setFixedSize(1150, 800)
        self.FontSize = self.getFontJson()
        self.font = QFont('JetBrains Mono', int(self.FontSize))
        self.initUI()
        
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

    def initUI(self):
        # Вертикальное расположение виджетов
        layout = QVBoxLayout()

        # Текстовое поле для ввода кода
        self.code_input = QTextEdit()
        self.code_input.setFont(self.font)
        self.code_input.setPlaceholderText("Введите ваш Python код здесь...")
        
        # Устанавливаем размер табуляции в 4 пробела
        font_metrics = self.code_input.fontMetrics()
        spaces_per_tab = 4  # Количество пробелов в одной табуляции
        self.code_input.setTabStopDistance(font_metrics.horizontalAdvance(' ') * spaces_per_tab)
        
        layout.addWidget(self.code_input)

        # Кнопка для выполнения кода
        self.run_button = QPushButton('Выполнить код')
        self.run_button.setFont(self.font)
        self.run_button.clicked.connect(self.execute_code)
        layout.addWidget(self.run_button)

        # Текстовое поле для вывода результата
        self.result_output = QTextEdit()
        self.result_output.setFont(self.font)
        self.result_output.setReadOnly(True)
        self.result_output.setPlaceholderText("Результат выполнения кода будет здесь...")
        layout.addWidget(self.result_output)

        self.setLayout(layout)
        self.setWindowTitle('Python Code Executor')

    @pyqtSlot()
    def execute_code(self):
        # Получаем код из текстового поля
        code = self.code_input.toPlainText()
        # Создаем поток для захвата вывода
        output = io.StringIO()
        try:
            # Перенаправляем стандартный вывод в наш поток
            with contextlib.redirect_stdout(output):
                exec(code, {"__builtins__": __builtins__}, {})
            # Получаем содержимое потока и выводим его в текстовое поле для результатов
            self.result_output.setPlainText(output.getvalue())
        except Exception as e:
            # В случае ошибки выводим информацию об ошибке
            self.result_output.setPlainText(str(e))

    def closeEvent(self, event):
        self.parent().show()
        super().closeEvent(event)