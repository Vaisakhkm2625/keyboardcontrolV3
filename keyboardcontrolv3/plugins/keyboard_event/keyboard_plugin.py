
from PyQt6.QtWidgets import  QKeySequenceEdit, QVBoxLayout, QWidget
from plugin_categories.event_plugin import Event

class KeyboardUiWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.data = {}
        self.keyedit = QKeySequenceEdit()

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.keyedit)

        self.setLayout(self.vbox)

    def get_ui_data(self):
        self.data["shortcut"] = self.keyedit.keySequence().toString()
        return self.data

    def set_ui_data(self,data):
        self.data = data
        print("setting keyboard data",self.data)
        self.keyedit.setKeySequence(self.data["shortcut"])


class KeyboardEventPlugin(Event):
    def __init__(self):
        super().__init__()

        self.key_mappings = []

    def get_ui_widget(self):
        return KeyboardUiWidget

    def set_data_mappings(self, id_mappings=[]):
        #self.key_mappings.append({"id":data})
        self.key_mappings = id_mappings
        print("keyboard mapping ->",self.key_mappings)
        

    def start_event_listener(self,callback):
        # keyboard press ed > callback
        print("starting keyboard listenr")


    def stop_event_listener(self):
        print("stoping keyboard listenr")
