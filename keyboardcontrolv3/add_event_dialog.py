from PyQt6.QtWidgets import QDialog,QFormLayout,QVBoxLayout,QLineEdit,QComboBox,QPushButton
from PyQt6.QtCore import pyqtSignal
from item import Item


class AddEventDialog(QDialog):
    data_passed_signal = pyqtSignal(object)

    def __init__(self, parent=None,event_list=[]):
        super(AddEventDialog, self).__init__(parent)

        flayout = QFormLayout()

        # Add widgets to the dialog
        self.event_combobox = QComboBox()

        for event in event_list:
            self.event_combobox.addItem(event)


        flayout.addRow("event",self.event_combobox )

        #layout.addWidget(self.name_line_edit)
        #layout.addWidget(self.description_line_edit)
        #event_type 
        
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

        event = {}
        event["type"] = self.event_combobox.currentText()
        event["data"] = {} 

        self.data_passed_signal.emit(event)
        self.accept()
