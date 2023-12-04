from PyQt6.QtWidgets import QWidget


# qwidget returned should have
# - get_ui_data()
# - set_ui_data()

class Event(object):

    def __init__(self):
        print("event plugin instantated")


    def get_ui_widget(self):
        return QWidget


    def set_data_mappings(self, id_mappings=[]):
        print("regitored ",id_mappings)


    def start_event_listener(self,callback_func):
        pass

    def stop_event_listener(self):
        pass
