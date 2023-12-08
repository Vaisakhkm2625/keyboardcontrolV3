from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QGridLayout
from PyQt6.QtWidgets import QVBoxLayout, QWidget, QLabel
from plugin_categories.event_plugin import Event
import sys
import mouse
import os

import moosegesture


from PyQt6.QtCore import QThread
from PyQt6.QtCore import pyqtSignal


class MouseUiWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.sequence = []

        self.init_ui()

    def init_ui(self):
        layout = QGridLayout()

        self.label = QLabel("Input Sequence: ")
        layout.addWidget(self.label, 0, 0, 1, 2)

        btn_up_left = QPushButton("↖")
        btn_up = QPushButton("Up")
        btn_up_right = QPushButton("↗")
        btn_right = QPushButton("Right")
        btn_left = QPushButton("Left")
        btn_down_left = QPushButton("↙")
        btn_down = QPushButton("Down")
        btn_down_right = QPushButton("↘")
        btn_backspace = QPushButton("Backspace")

        btn_up_left.clicked.connect(lambda: self.add_to_sequence("UL"))
        btn_up.clicked.connect(lambda: self.add_to_sequence("U"))
        btn_up_right.clicked.connect(lambda: self.add_to_sequence("UR"))
        btn_left.clicked.connect(lambda: self.add_to_sequence("L"))
        btn_right.clicked.connect(lambda: self.add_to_sequence("R"))
        btn_down_left.clicked.connect(lambda: self.add_to_sequence("DL"))
        btn_down.clicked.connect(lambda: self.add_to_sequence("D"))
        btn_down_right.clicked.connect(lambda: self.add_to_sequence("DR"))

        btn_backspace.clicked.connect(self.remove_last_from_sequence)

        layout.addWidget(btn_up_left, 1, 0)
        layout.addWidget(btn_up, 1, 1)
        layout.addWidget(btn_up_right, 1, 2)
        layout.addWidget(btn_left, 2, 0)
        layout.addWidget(btn_right, 2, 2)
        layout.addWidget(btn_down_left, 3, 0)
        layout.addWidget(btn_down, 3, 1)
        layout.addWidget(btn_down_right, 3, 2)
        layout.addWidget(btn_backspace, 4, 0, 1, 3)

        self.setLayout(layout)
        self.setWindowTitle('Input Sequence Widget')

    def add_to_sequence(self, direction):
        if self.sequence and self.sequence[-1] == direction:
            return
        self.sequence.append(direction)
        self.update_sequence_label()

    def remove_last_from_sequence(self):
        if self.sequence:
            self.sequence.pop()
            self.update_sequence_label()

    def update_sequence_label(self):
        self.label.setText(f"Input Sequence: {' '.join(self.sequence)}")
        print(self.sequence)

    def get_ui_data(self):
        self.data["gesture_sequence"] = self.sequence
        return self.data

    def set_ui_data(self, data):
        self.data = data

        print("setting keyboard data", self.data)
        try:

            self.sequence = self.data["gesture_sequence"]
            self.update_sequence_label()

        except Exception as e:
            print("error: unable to set gesture_sequence ->", e)


class MouseEventPlugin(Event):
    def __init__(self):
        super().__init__()

        self.mouse_gesture_mappings = []
        self.mouse_pos = []

    def get_ui_widget(self):
        return MouseUiWidget

    def set_data_mappings(self, id_mappings=[]):
        # self.key_mappings.append({"id":data})
        self.mouse_gesture_mappings = id_mappings
        print("mouse_gesture mapping ->", self.mouse_gesture_mappings)

    def find_item_id(self, gesture_sequence, data):
        print("guestures:", gesture_sequence)
        for item in data:
            if "data" in item and "gesture_sequence" in item["data"]:
                if item["data"]["gesture_sequence"] == gesture_sequence:
                    return item["item"]
        return None

    def start_event_listener(self, callback_func):
        # keyboard press ed > callback
        print("starting mouse_gesture listener")

        # Determine the appropriate command based on the platform
        if os.name == 'nt':  # Windows
            def on_mouse_event(e):

                if mouse.is_pressed(button="left"):

                    # print(mouse.get_position())
                    self.mouse_pos.append(mouse.get_position())

                if isinstance(e, mouse.ButtonEvent):
                    print(e.event_type)
                    if (e.event_type == "up"):
                        print("mousepos:", self.mouse_pos)
                        gesture = moosegesture.getGesture(self.mouse_pos)
                        print(gesture)
                        # print(mousepos)
                        self.mouse_pos.clear()

                        result = self.find_item_id(
                            gesture, self.mouse_gesture_mappings)

                        if result:
                            print("result:", result)
                            callback_func(result)
                        else:
                            print("not found")

            mouse.hook(on_mouse_event)

        elif os.name == 'posix':  # Linux or macOS
            print(
                "mouse plugin need higher privilages to run on linux.. currently not supported")
        else:
            raise NotImplementedError("Unsupported operating system")

    def stop_event_listener(self):
        print("stopping mouse listener")

        if os.name == 'nt':  # Windows
            mouse.unhook_all()

        elif os.name == 'posix':  # Linux or macOS
            print(
                "mouse plugin need higher privilages to run on linux.. currently not supported")
        else:
            raise NotImplementedError("Unsupported operating system")

