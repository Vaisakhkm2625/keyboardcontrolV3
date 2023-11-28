import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon

from ui.main_ui import Ui_MainWindow

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







if __name__ == "__main__":
    app = Application(sys.argv)
    sys.exit(app.exec())
