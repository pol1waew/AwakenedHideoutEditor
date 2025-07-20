from PySide6.QtWidgets import QApplication, QFileDialog, QMessageBox
from gui.main_window import MainWindow
from logic.hideout_parser import HideoutParser


class Application(QApplication):
    def __init__(self):
        super().__init__()

        self.parser = HideoutParser()
        self.main_window = MainWindow()

        self.main_window.ui.load_action.triggered.connect(self.load_hideout)
        self.main_window.ui.save_as_action.triggered.connect(self.save_data_as_new)

        self.main_window.show()

    def load_hideout(self):
        """Loads hideout file into a programm
        """
        
        self.opened_file_path, _ = QFileDialog.getOpenFileName(self.main_window, 
                                                               "Select hideout file", 
                                                               "hideout_files/", 
                                                               "Hideout file (*.hideout)")

        if not self.opened_file_path:            
            ## TODO: make a sep method
            self.main_window.ui.save_as_action.setEnabled(False)
            self.main_window.ui.save_action.setEnabled(False)
            return

        if not self.parser.parse_hideout_file(self.opened_file_path):
            QMessageBox.warning(self.main_window,
                                "Opened wrong file",
                                "Seems like you have opened wrong file which looks like a PoE hideout file")

            self.main_window.ui.save_as_action.setEnabled(False)
            self.main_window.ui.save_action.setEnabled(False)
            return

        self.main_window.load_hideout_data(self.parser.doodads_data)

        self.main_window.ui.save_as_action.setEnabled(True)
        self.main_window.ui.save_action.setEnabled(True)

    def save_data_as_new(self):
        new_file_path, _ = QFileDialog.getSaveFileName(self.main_window, 
                                                       "Save hideout as new file", 
                                                       self.opened_file_path.replace(".hideout", "_2.hideout"), 
                                                       "Hideout file (*.hideout)")
        
        if not new_file_path:
            return
        
        self.parser.make_output_file(new_file_path)

    def save_data_as_overriding(self):
        self.parser.make_output_file(self.opened_file_path)
