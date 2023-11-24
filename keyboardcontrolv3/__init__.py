
from PyQt6.QtWidgets import QApplication, QWidget
import sys


class SWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()




if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainapp = SWidget()
    mainapp.show()

    sys.exit(app.exec())
