from PyQt6.QtWidgets import QDialog,QFormLayout,QVBoxLayout,QLineEdit,QComboBox,QPushButton
from PyQt6.QtCore import pyqtSignal
from item import Item


class AddItemDialog(QDialog):
    data_passed_signal = pyqtSignal(Item)

    def __init__(self, parent=None,action_list=[]):
        super(AddItemDialog, self).__init__(parent)

        flayout = QFormLayout()

        # Add widgets to the dialog
        self.name_line_edit = QLineEdit()
        self.description_line_edit = QLineEdit()
        self.action_combobox = QComboBox()

        for action in action_list:
            self.action_combobox.addItem(action)


        flayout.addRow("Name",self.name_line_edit)
        flayout.addRow("Description",self.description_line_edit)
        flayout.addRow("Action",self.action_combobox )

        #layout.addWidget(self.name_line_edit)
        #layout.addWidget(self.description_line_edit)
        #action_type 
        
        button_ok = QPushButton("OK")
        button_cancel = QPushButton("Cancel")

        # Connect accept and reject signals to slots
        button_ok.clicked.connect(self.accept_with_data)
        button_cancel.clicked.connect(self.reject)

        layout = QVBoxLayout()
        layout.addLayout(flayout)
        layout.addWidget(button_ok)
        layout.addWidget(button_cancel)

        self.setLayout(layout)

    def accept_with_data(self):

        item = Item(self.name_line_edit.text()) 
        item.description = self.description_line_edit.text()
        item.action_type = self.action_combobox.currentText()

        self.data_passed_signal.emit(item)
        self.accept()
