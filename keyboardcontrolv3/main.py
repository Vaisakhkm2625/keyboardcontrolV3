import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon



class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("hello")
        self.setGeometry(150,150,500,500)
        self.setWindowIcon(QIcon("icons/list.png"))
        self.setStyleSheet("background-color:red")
        self.setWindowOpacity(0.7)


app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())
