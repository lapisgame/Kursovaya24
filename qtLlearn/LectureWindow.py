from PyQt6.QtWidgets import QWidget, QGroupBox, QTextBrowser, QPushButton, QVBoxLayout

import json
import os

class LectureWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('Лекции')
        self.setFixedSize(1150, 800)

        self.groupBox = QGroupBox('Моя GroupBox', self)
        self.groupBox.setGeometry(10, 0, 200, 790)

        self.initLectureButtons()

        # self.button = QPushButton('Моя кнопка', self.groupBox)
        # self.button.setGeometry(10, 20, 100, 30)

        self.plainTextEdit = QTextBrowser(self)
        self.plainTextEdit.setGeometry(210, 10, 930, 780)

        # # Разбор JSON
        # title = "Основы Python"
        # fontsize = 14
        # style = "<style>*{font-size:" + str(fontsize) + "pt}</style>"
        # content = f"{style}<p>Установка</p><p>Для начала нам потребуется скачать питон с официального сайта. Важно (!) поставить галочку add python __ to PATH. Затем нажать Install now. После чего запустить скаченный файл.</p><p>Можно работать с питоновскими файлами и без среды разработки (IDE), но это не совсем удобно, так как для запуска файла с расширение .py в терминале (это командная строка или же cmd) придется после перехода в директорию с файлом написать python ___.py, после чего в консоли появится результат выполнения программы.</p><p>Более легкий способ потребует для запуска нажать на одну кнопку. И вариант этот называется PyCharm. Скачать можно с сайта https://www.jetbrains.com/pycharm/download/ . Нужна Community версия, она полностью бесплатна и почти не имеет обрезанного функционала, так как программировать мы будем только на Питоне. А профессиональная версия включает в себя еще расширенные инструменты для разработки на HTML, JS и баз данных SQL.</p><p>Арифметические операции </p><p>Рассмотрим простейшие арифметические операции и как они выглядят на Питоне:</p><p>Переменные и синтаксис</p><p>Python может определить тип переменной: для x = 1.35 будет выведен тип FLOAT. </p><p>Что будет выведено, если</p><p>x = input()   </p><p>y = input()   </p><p>print(x+y) при введении чисел 123 и 354. Должно быть 477? Нет, 123354. Всё это связанно с динамической типизацией и тем, что input выдает строковое значение. Чтобы преобразовать переменную одного типа в другой, мы можем использовать следующие функции:</p><p>str(х) - переводит переменную х в строковую</p><p>int(х) – переводит переменную х в целочисленную</p><p>float(х) – переводит переменную х в переменную с плавающей точкой</p><p>Тип bool – это  логические переменные, то есть принимающие значение True (истина) или False (ложь).</p><p>Ко всем переменным можно просто обращаться по имени и получать их значение. Но строковые переменные – особенные, и к ним можно обращаться по индексу символа. Индексация в строке происходит с нуля. Вывести длину строковой переменной можно командой len(s). Пример обращения к строке по индексу:</p><p>S=’spam’</p><p>print(S[0])  >> s</p><p>print(S[2])  >> a</p><p>print(S[-2]) >>a</p><p>Строки можно умножать на числа, складывать между собой.</p><p>S1 = 'spam'</p><p>S2 = 'eggs'</p><p>print(S1 + S2)&emsp;>>'spameggs'</p><p>print('spam' * 3)  >>spamspamspam</p><p>Строковые переменные можно доставать «срезами», делается это так:</p><p>название_переменной[X:Y], где X – начало среза, а Y – окончание;</p><p>символ с номером Y в срез не входит. По умолчанию первый индекс равен 0, а второй - длине строки.</p><p>s = 'spameggs'</p><p>>>> s[3:5]&emsp;>>'me'</p><p>>>> s[2:-2]&emsp;>>'ameg'</p><p>>>> s[:6]&emsp;>>'spameg'</p><p>>>> s[1:]&emsp;>>'pameggs'</p><p>Функции для перевода всей строки в верхний регистр _.upper(), а для перевода всей строки в нижний регистр _.lower(), _.title() это перевод начальных символов всех слов в верхний регистр, _.capitalize() только первый символ заглавный. </p><p>Сбор строки из массива осуществляется так</p><p> переменная = “способ связи”.join (название массива) или вместо массива можно указать название строковой переменной для разделения между каждым символом указанным способом связи.</p><p>Условные операторы</p><p>Синтаксис условных операторов if elif else:</p><p>if условия 1: </p><p>&emsp;действие 1</p><p>elif условие 2:</p><p>&emsp;действие 2</p><p>else:</p><p>&emsp;действие 3</p><p>Блок elif является необязательным и конструкцию if elif else можно построить обычным образом если иначе –  if else. Elif может быть сколько угодно.</p><p>Укороченная версия if-else:</p><p>if X:</p><p>&emsp;A=Y</p><p>else:</p><p>&emsp;A=Z</p><p>Можно также написать A=Y if X else Z. В литературе этот прием называется трехместное выражение if-else.</p><p>Логические операции</p><p>Сравнение возвращает логическое значение.</p><p>Рассмотрим основные логические операторы: X and Y – логическое И (выдает истину только когда Х И Y истинны), X or Y – логическое ИЛИ (выдает истину, если хотя бы 1 из двух истинно), X xor Y – взаимоисключающее ИЛИ (является истиной, если только одно из двух истина), not X – логическое отрицание (инверсия).</p>"
        # # Установка HTML-контента
        # self.plainTextEdit.setHtml(content)

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
