from PySide6.QtWidgets import QApplication
from gui.main_window import MainWindow


app = QApplication()
main_window = MainWindow()

main_window.show()

app.exec()