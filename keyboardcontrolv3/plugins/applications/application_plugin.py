from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QComboBox, QLabel, QLineEdit, QWidget,QVBoxLayout,QPushButton
from plugin_categories.action_plugin import Action
import os


class ApplicationUiWidget(QWidget):

    data = {}

    def __init__(self):
        super().__init__()

        print("application ui")
        #self.lab = QVBoxLayout()
        ##self.lab.addWidget(QPushButton("Application"))
        #self.application_name = QLineEdit() 

        #self.lab.addWidget(QLabel("Application automation"))
        #self.lab.addWidget(QLabel("Select the application you wanted from the menu below"))

        #self.lab.addWidget(self.application_name)
        #self.lab.addStretch()


        #self.setLayout(self.lab)

        # Create widgets
        label1 = QLabel("Application Lanuncher")
        label2 = QLabel("Select the application you want from the menu below")
        #self.application_name = QComboBox()
        self.application_name = QLineEdit()

        # Create layout
        layout = QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(self.application_name)
        layout.addStretch()

        # Apply styles
        label1.setStyleSheet("font-size: 18px; font-weight: bold;")
        label2.setStyleSheet("font-size: 14px; color: #555;")
        self.application_name.setStyleSheet("padding: 5px; font-size: 14px;")

        # Set layout for the main widget
        self.setLayout(layout)


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


        application_name = data["application_name"]
        # Determine the appropriate command based on the platform
        if os.name == 'nt':  # Windows
            command = f'start {application_name}'
        elif os.name == 'posix':  # Linux or macOS
            command = f'open {application_name}'
        else:
            raise NotImplementedError("Unsupported operating system")

        import subprocess
        process = subprocess.Popen(application_name,shell=True)

