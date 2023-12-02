
from PyQt6.QtWidgets import QHBoxLayout, QLineEdit, QPushButton, QWidget
from plugin_categories.action_plugin import Action 

class PythonScriptUI(QWidget):
    def __init__(self):
        super().__init__()
        data = {}

        print("PythonScriptUi plugin loaded")
        la = QHBoxLayout()
        self.line_edit= QLineEdit("no data")
        la.addWidget(self.line_edit)
        self.setLayout(la)


    def set_ui_data(self,data):
        self.data = data
        self.line_edit.setText(data["script_location"])

    def get_ui_data(self):
        self.data["script_location"] = self.line_edit.text
        return self.data
    

class PythonScriptPlugin(Action):

    def __init__(self):
        super().__init__()

    def get_ui_widget(self):
        return PythonScriptUI

    def run_action(self,data):
        print(data["script_location"],"loaded")

        from subprocess import call
        call(["python", data["script_location"]])



