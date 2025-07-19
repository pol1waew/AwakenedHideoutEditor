from PySide6.QtWidgets import QApplication, QFileDialog
from gui.main_window import MainWindow
from logic.hideout_parser import HideoutParser


class Application(QApplication):
    def __init__(self):
        super().__init__()

        self.main_window = MainWindow()

        self.main_window.ui.load_action.triggered.connect(self.load_hideout)

        self.main_window.show()

    def load_hideout(self):
        """Loads hideout file into a programm
        """
        
        file_path, _ = QFileDialog.getOpenFileName(self.main_window, "Select hideout file", "logic/hideout_files/", "Hideout file (*.hideout)")

        self.parser = HideoutParser(file_path)

        self.main_window.load_hideout_data(self.parser.doodads_data)
