from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QLineEdit, QWidget,QHBoxLayout,QPushButton
from plugin_categories.action_plugin import Action


class ApplicationUiWidget(QWidget):

    data = {}

    def __init__(self):
        super().__init__()

        print("application ui")
        self.lab = QHBoxLayout()
        #self.lab.addWidget(QPushButton("Application"))
        self.application_name = QLineEdit() 
        self.lab.addWidget(self.application_name)

        self.setLayout(self.lab)

    def set_ui_data(self,data):
        self.data = data
        self.application_name.setText(self.data["application_name"])

    def get_ui_data(self):
        self.data["application_name"] = self.application_name.text()
        return self.data


class ApplicationPlugin(Action):
    def __init__(self):
        super().__init__()
        print("app plugin loaded")

    def get_ui_widget(self):
        return ApplicationUiWidget

    def run_action(self,data):
        print("running application plugin >",data["application_name"])

        import subprocess
        process = subprocess.Popen(data["application_name"])

