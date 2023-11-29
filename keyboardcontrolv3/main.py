import sys
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLineEdit, QListWidget, QListWidgetItem, QMainWindow, QPushButton, QWidget
from PyQt6.QtGui import QIcon

from ui.main_ui import Ui_MainWindow


from item import Item

class Manager:
    def __init__(self):
        self.item_list = []


class Application(QApplication):

    def __init__(self, argv):
        super().__init__(argv)

        #apply_stylesheet(self, theme='dark_teal.xml')
        self.window = MainWindow()
        self.window.show()

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        pushbut = QPushButton()



if __name__ == "__main__":
    app = Application(sys.argv)
    sys.exit(app.exec())
