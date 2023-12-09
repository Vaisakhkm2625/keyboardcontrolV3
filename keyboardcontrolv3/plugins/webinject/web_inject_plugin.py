from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QComboBox, QFileDialog, QLabel, QLineEdit, QWidget, QVBoxLayout, QPushButton
from plugin_categories.action_plugin import Action
import os
import keyboard
import urllib.parse


class WebInjectUiWidget(QWidget):

    data = {}

    def __init__(self):
        super().__init__()

        self.file_path = "./"

        print("application ui")
        # self.lab = QVBoxLayout()
        # self.lab.addWidget(QPushButton("WebInject"))
        # self.application_name = QLineEdit()

        # self.lab.addWidget(QLabel("WebInject automation"))
        # self.lab.addWidget(QLabel("Select the application you wanted from the menu below"))

        # self.lab.addWidget(self.application_name)
        # self.lab.addStretch()

        # self.setLayout(self.lab)take about 3

        # Create widgets
        label1 = QLabel("Web Injecter")
        label2 = QLabel("Choose javascript file")
        self.btn_choose_file = QPushButton('Choose File', self)
        # self.application_name = QComboBox()
        self.js_file_path = QLineEdit()

        # Create layout
        layout = QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(self.js_file_path)
        layout.addWidget(self.btn_choose_file)
        layout.addStretch()

        # self.btn_choose_file.setGeometry(150, 150, 100, 30)
        self.btn_choose_file.clicked.connect(self.showFileDialog)

        # Apply styles
        label1.setStyleSheet("font-size: 18px; font-weight: bold;")
        label2.setStyleSheet("font-size: 14px; color: #555;")
        self.js_file_path.setStyleSheet("padding: 5px; font-size: 14px;")

        # Set layout for the main widget
        self.setLayout(layout)

    def showFileDialog(self):
        # Create a file dialog
        file_dialog = QFileDialog(self)
        file_dialog.setWindowTitle('Open File')

        # Set the file dialog mode to select a single file
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)

        # Execute the file dialog and get the selected file path
        file_path, _ = file_dialog.getOpenFileName(
            self, 'Open File', '', 'All Files (*);;Text Files (*.txt)')

        # Display the selected file path (optional)
        print("Selected File:", file_path)
        self.js_file_path.setText(file_path)

        # You can perform further actions with the selected file path here

    def set_ui_data(self, data):
        self.data = data
        self.js_file_path.setText(self.data["js_file_path"])

    def get_ui_data(self):
        self.data["js_file_path"] = self.js_file_path.text()
        return self.data


class WebInjectPlugin(Action):
    def __init__(self):
        super().__init__()
        print("app plugin loaded")

    def get_ui_widget(self):
        return WebInjectUiWidget

    def create_bookmarklet(self, js_code):
        # URL encode the JavaScript code
        encoded_js_code = urllib.parse.quote(js_code)

        # Wrap the encoded JavaScript code in a bookmarklet template
        bookmarklet_template = f"javascript:(function(){{{encoded_js_code}}})();"
        return bookmarklet_template

    def read_file(self, js_file_name):
        with open(js_file_name) as f:
            js_code = f.read()

        return js_code

    def inject_bookmarklet(self, bookmarklet):

        keyboard.press_and_release("ctrl+l")
        keyboard.write(bookmarklet)
        keyboard.press_and_release("enter")

    def web_inject(self, js_file_name):

        js_code = self.read_file(js_file_name)
        # Generate the bookmarklet using the provided JavaScript code
        bookmarklet = self.create_bookmarklet(js_code)
        self.inject_bookmarklet(bookmarklet)

    def run_action(self, data):
        print("running application plugin >", data["js_file_path"])

        # Determine the appropriate command based on the platform
        if os.name == 'nt':  # Windows
            self.web_inject(data["js_file_path"])
            # print(data["js_file_path"])

        elif os.name == 'posix':  # Linux or macOS
            pass
        else:
            raise NotImplementedError("Unsupported operating system")

