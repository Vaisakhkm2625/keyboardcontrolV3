from PyQt6.QtWidgets import QWidget

class Event(object):

    def __init__(self):
        print("event plugin instantated")


    def get_ui_widget(self):
        return QWidget

    def registor_id_data(self,id,data={}):
        print("regitored ",id,"with data",data)


    def start_event_listener(self,callback_func):
        pass

    def stop_event_listener(self):
        pass
