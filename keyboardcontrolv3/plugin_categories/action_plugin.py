
from PyQt6.QtWidgets import QWidget


# qwidget returned should have
# - get_ui_data()
# - set_ui_data()


class Action(object):

    def __init__(self):
        super().__init__()
        print("initialising action plugin")

    def get_ui_widget(self) -> QWidget:
        print("This is plugin 1")

        return QWidget()

    def run_action(self):
        print("plugin action running")

