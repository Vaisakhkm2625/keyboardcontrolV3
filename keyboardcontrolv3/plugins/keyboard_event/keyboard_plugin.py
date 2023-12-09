
from PyQt6.QtWidgets import QKeySequenceEdit, QLineEdit, QVBoxLayout, QWidget, QLabel
from plugin_categories.event_plugin import Event
import keyboard
import os


from PyQt6.QtGui import QKeySequence
from PyQt6.QtCore import QThread, Qt
from PyQt6.QtCore import pyqtSignal


class KeyboardWorker(QThread):

    run_function_signal = pyqtSignal()

    def __init__(self, keyboard):
        super().__init__()
        self.keyboard = keyboard

    def run(self):
        self.keyboard.run()


class KeyboardUiWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.vbox = QVBoxLayout()
        self.data = {}

        self.label = QLabel()
        #self.keyboard_edit = QKeySequenceEdit(QKeySequence(Qt.Key.Key_K))
        self.keyboard_edit = QLineEdit()
        #self.keyboard_edit.setVisible(True)


        self.vbox.addWidget(self.label)
        #self.vbox.addWidget(self.keyboard_edit)

        self.setLayout(self.vbox)

    def get_ui_data(self):
        #self.data["shortcut"] = self.keyboard_edit.keySequence().toString()
        self.data["shortcut"] = self.keyboard_edit.text()
        return self.data

    def set_ui_data(self, data):
        self.data = data
        print("setting keyboard data", self.data)
        try:
            self.label.setText(self.data["shortcut"])
            #self.keyboard_edit.setKeySequence(QKeySequence(self.data["shortcut"]))
            #self.keyboard_edit.setText(self.data["shortcut"])
        except Exception as e:
            print("error: unable to set keybinding ->", e, "<-")
            #self.label.setText("no keybinding")
            #self.keyboard_edit.clear()
            #self.keyboard_edit.clear()


class KeyboardEventPlugin(Event):
    def __init__(self):
        super().__init__()

        self.key_mappings = []

    def get_ui_widget(self):
        return KeyboardUiWidget

    def set_data_mappings(self, id_mappings=[]):
        # self.key_mappings.append({"id":data})
        self.key_mappings = id_mappings
        print("keyboard mapping ->", self.key_mappings)

    def start_event_listener(self, callback_func):
        # keyboard press ed > callback
        print("starting keyboard listenr")

        # Determine the appropriate command based on the platform
        if os.name == 'nt':  # Windows

            for keymap in self.key_mappings:
                print(keymap)
                try:
                    keyboard.add_hotkey(
                        # keymap["data"]["shortcut"], print, args=('triggered', 'hotkey'))
                        keymap["data"]["shortcut"], callback_func, args=(keymap["item"],),suppress=True)
                except Exception as e:
                    print("adding hotkey ->",
                          keymap["data"]["shortcut"], " failed")

        elif os.name == 'posix':  # Linux or macOS
            print(
                "keyboard plugin need higher privilages to run on linux.. currently not supported")
        else:
            raise NotImplementedError("Unsupported operating system")

    def stop_event_listener(self):
        print("stoping keyboard listenr")

