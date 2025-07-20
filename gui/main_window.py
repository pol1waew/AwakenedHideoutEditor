from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, Qt
from PySide6.QtWidgets import QMainWindow
import pandas as pd
from gui.user_interface import UserInterface
from gui.doodad_list_item import DoodadListItem


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Awakened Hideout Editor")
        self.setObjectName(u"main_window")
        self.resize(1280, 720)
        self.setEnabled(True)

        self.ui = UserInterface()
        self.ui.setup_ui(self)

        DoodadListItem.set_scene_reference(self.ui.scene)

    def load_hideout_data(self, doodads_data : pd.DataFrame):
        self.ui.scene.load_hideout_data(doodads_data)
        self.ui.doodads_list.load_hideout_data(doodads_data)        
