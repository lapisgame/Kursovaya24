import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QFont
from Scripts.DragTask import DragTaskWidget

class DialogWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle("Drag Task")
 
        self.DragWidget = DragTaskWidget()
        container = self.DragWidget.container
 
        layout = QVBoxLayout()
        layout.addWidget(container)
        layout.addStretch(1)
        
        btn = QPushButton('Check')
        btn.clicked.connect(self.check_ans)
 
        layout.addWidget(btn)

        self.setLayout(layout)
    
    def check_ans(self):
        corrent_text_order = self.DragWidget.corrent_text_order
        this_text_order = self.DragWidget.drag.get_item_data()

        print(this_text_order == corrent_text_order)