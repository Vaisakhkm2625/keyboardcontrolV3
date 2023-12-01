
from PyQt6.QtWidgets import QKeySequenceEdit, QWidget
from plugin_categories.event_plugin import Event

class KeyboardUiWidget(QWidget):

    def __init__(self):
        super().__init__(self)
        self.data = {}
        self.keyedit = QKeySequenceEdit()

    def get_data(self):
        self.data["key_sequence"] = self.keyedit.keySequence.keySequence().toString()
        return self.data

    def set_data(self,data):
        self.data = data
        self.keyedit.setKeySequence(self.data["key_sequence"])
        return self.data


class KeyboardEventPlugin(Event):
    def __init__(self):
        super().__init__()

        self.key_mappings = []

    def get_ui_widget(self):
        return KeyboardEventPlugin 

    def registor_id_data(self, id, data={}):
        self.key_mappings.append({"id":data})

    def start_event_listener(self,callback):
        # keyboard press ed > callback
        print("starting keyboard listenr")


    def stop_event_listener(self):
        print("stoping keyboard listenr")
