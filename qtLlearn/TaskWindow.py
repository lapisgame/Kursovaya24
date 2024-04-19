import sys
import json
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QRadioButton, QCheckBox, QLineEdit, QPushButton, QMessageBox, QApplication, QHBoxLayout
)
from PyQt6.QtCore import Qt, QMimeData, pyqtSignal
from PyQt6.QtGui import QDrag, QPixmap

class DragTargetIndicator(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setContentsMargins(25, 5, 25, 5)
        self.setStyleSheet(
            "QLabel { background-color: #ccc; border: 1px solid black; }"
        )

class DragItem(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setContentsMargins(25, 5, 25, 5)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setStyleSheet("border: 1px solid black;")
        # Store data separately from display label, but use label for default.
        self.data = self.text()

    def mouseMoveEvent(self, e):
        if e.buttons() == Qt.MouseButton.LeftButton:
            drag = QDrag(self)
            mime = QMimeData()
            drag.setMimeData(mime)

            pixmap = QPixmap(self.size())
            self.render(pixmap)
            drag.setPixmap(pixmap)

            drag.exec(Qt.DropAction.MoveAction)

class DragWidget(QWidget):
    orderChanged = pyqtSignal(list)

    def __init__(self, *args, orientation=Qt.Orientation.Horizontal, **kwargs):
        super().__init__()
        self.setAcceptDrops(True)

        # Store the orientation for drag checks later.
        self.orientation = orientation

        if self.orientation == Qt.Orientation.Vertical:
            self.blayout = QVBoxLayout()
        else:
            self.blayout = QHBoxLayout()

        # Add the drag target indicator. This is invisible by default,
        # we show it and move it around while the drag is active.
        self._drag_target_indicator = DragTargetIndicator()
        self.blayout.addWidget(self._drag_target_indicator)
        self._drag_target_indicator.hide()

        self.setLayout(self.blayout)

    def get_drag_items_values(self):
        values = []
        for i in range(self.blayout.count()):
            item = self.blayout.itemAt(i).widget()
            # Проверяем, является ли виджет экземпляром DragItem
            if isinstance(item, DragItem):
                # Получаем значение DragItem и добавляем его в список
                values.append(item.data)
        return values

    def dragEnterEvent(self, e):
        e.accept()

    def dragLeaveEvent(self, e):
        self._drag_target_indicator.hide()
        e.accept()

    def dragMoveEvent(self, e):
        # Find the correct location of the drop target, so we can move it there.
        index = self._find_drop_location(e)
        if index is not None:
            # Inserting moves the item if its alreaady in the layout.
            self.blayout.insertWidget(index, self._drag_target_indicator)
            # Hide the item being dragged.
            e.source().hide()
            # Show the target.
            self._drag_target_indicator.show()
        e.accept()

    def dropEvent(self, e):
        widget = e.source()
        # Use drop target location for destination, then remove it.
        self._drag_target_indicator.hide()
        index = self.blayout.indexOf(self._drag_target_indicator)
        if index is not None:
            self.blayout.insertWidget(index, widget)
            self.orderChanged.emit(self.get_item_data())
            widget.show()
            self.blayout.activate()
        e.accept()

    def _find_drop_location(self, e):
        pos = e.position()
        spacing = self.blayout.spacing() / 2

        for n in range(self.blayout.count()):
            # Get the widget at each index in turn.
            w = self.blayout.itemAt(n).widget()

            if self.orientation == Qt.Orientation.Vertical:
                # Drag drop vertically.
                drop_here = (
                    pos.y() >= w.y() - spacing
                    and pos.y() <= w.y() + w.size().height() + spacing
                )
            else:
                # Drag drop horizontally.
                drop_here = (
                    pos.x() >= w.x() - spacing
                    and pos.x() <= w.x() + w.size().width() + spacing
                )

            if drop_here:
                # Drop over this target.
                break

        return n

    def add_item(self, item):
        self.blayout.addWidget(item)

    def get_item_data(self):
        data = []
        for n in range(self.blayout.count()):
            # Get the widget at each index in turn.
            w = self.blayout.itemAt(n).widget()
            if hasattr(w, "data"):
                # The target indicator has no data.
                data.append(w.text())
        return data
    
# Основной класс окна с задачами
class TaskWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('Задачи')
        self.setFixedSize(1150, 800)
        tasks = self.load_tasks('Tasks/test.json')
        self.tasks = tasks
        self.current_task_index = 0
        self.layout = QVBoxLayout(self)
        self.updateUI()

        # Получение данных из json
    def load_tasks(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            tasks = json.load(file)
        return tasks

    # Ивент закрытия окна
    def closeEvent(self, event):
        self.parent().show()
        super().closeEvent(event)

    def updateUI(self):
        # Очистка текущего содержимого layout
        for i in reversed(range(self.layout.count())): 
            self.layout.itemAt(i).widget().setParent(None)

        # Проверка на наличие заданий
        if self.current_task_index < len(self.tasks):
            task = self.tasks[self.current_task_index]
            self.question_label = QLabel(task['question'], self)
            self.layout.addWidget(self.question_label)

            self.answers_widgets = []

            if task['type'] in ['single_choice', 'multiple_choice']:
                for option in task['options']:
                    if task['type'] == 'single_choice':
                        rb = QRadioButton(option, self)
                        self.answers_widgets.append(rb)
                        self.layout.addWidget(rb)
                    elif task['type'] == 'multiple_choice':
                        cb = QCheckBox(option, self)
                        self.answers_widgets.append(cb)
                        self.layout.addWidget(cb)
            
            elif task['type'] == 'text_input':
                self.text_input = QLineEdit(self)
                self.answers_widgets.append(self.text_input)
                self.layout.addWidget(self.text_input)
            
            elif task['type'] == 'drag_and_drop':
                self.drag_widget = DragWidget()
                for item in task['options']:
                    drag_item = DragItem(item)
                    self.drag_widget.add_item(drag_item)
                self.layout.addWidget(self.drag_widget)

            self.next_button = QPushButton("Далее", self)
            self.next_button.clicked.connect(self.checkAnswer)
            self.layout.addWidget(self.next_button)
        
        # Если задания закончились
        else:
            self.question_label = QLabel("Конец викторины!", self)
            self.layout.addWidget(self.question_label)

    def checkAnswer(self):
        task = self.tasks[self.current_task_index]
        if task['type'] == 'single_choice':
            selected_option = [rb.text() for rb in self.answers_widgets if rb.isChecked()]
            if selected_option and selected_option[0] == task['correct_answer']:
                self.current_task_index += 1
            else:
                QMessageBox.warning(self, "Неверно", "Попробуйте снова.")
                return
        
        elif task['type'] == 'multiple_choice':
            selected_options = [cb.text() for cb in self.answers_widgets if cb.isChecked()]
            if set(selected_options) == set(task['correct_answers']):
                self.current_task_index += 1
            else:
                QMessageBox.warning(self, "Неверно", "Попробуйте снова.")
                return
        
        elif task['type'] == 'text_input':
            if self.text_input.text() == task['correct_answer']:
                self.current_task_index += 1
            else:
                QMessageBox.warning(self, "Неверно", "Попробуйте снова.")
                return
        
        elif task['type'] == 'drag_and_drop':
            current_order = [item for item in self.drag_widget.get_drag_items_values()]
            correct_order = task['correct_order']
            if current_order == correct_order:
                self.current_task_index += 1
            else:
                QMessageBox.warning(self, "Неверно", "Попробуйте снова.")
                return
        
        self.updateUI()