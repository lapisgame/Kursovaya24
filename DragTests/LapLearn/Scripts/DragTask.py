from PyQt5.QtCore import Qt
from Scripts.DragAndDropLabel import DragItem, DragWidget
from random import shuffle

from PyQt5.QtWidgets import QPushButton, QWidget, QVBoxLayout

class DragTaskWidget(QWidget):
    def __init__(self, parent: QWidget | None = None, flags: Qt.WindowFlags | Qt.WindowType = Qt.WindowFlags()) -> None:
        super().__init__(parent, flags)
        self.createDragTaskCentralWidget()
        self.container.setLayout(self.layout_drag)

    def createDragTaskCentralWidget(self)->QWidget:
        self.corrent_text_order = ["If", "__name__", "==", '"__main__"', ":"]
        text_list = ["If", "__name__", "==", '"__main__"', ":"]
        movable_list = [True, True, True, True, True]

        temp = list(zip(text_list, movable_list))
        shuffle(temp)
        text_list, movable_list = zip(*temp)
        text_list, movable_list = list(text_list), list(movable_list)

        self.drag = DragWidget(orientation=Qt.Orientation.Horizontal)
        for n, l, flag in zip(list(range(len(text_list))), text_list, movable_list):
            item = DragItem(l)
            item.set_data(n, flag)  # Store the data.
            self.drag.add_item(item)

        # Print out the changed order.
        self.drag.orderChanged.connect(print)

        self.container = QWidget()
        self.layout_drag = QVBoxLayout()
        self.layout_drag.addStretch(1)
        self.layout_drag.addWidget(self.drag)
        self.layout_drag.addStretch(1)
        
    def checkAnswer(self):
        # Получаем порядок элементов из виджета перетаскивания
        dragged_items = [item.data() for item in self.drag.get_item_data()]

        # Сравниваем порядок элементов с правильным порядком
        if dragged_items == self.corrent_text_order:
            print("Ответ верный!")
        else:
            print("Ответ неверный.")