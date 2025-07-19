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

        for i, data in doodads_data.drop_duplicates(subset=["hash"]).iterrows():
            item = DoodadListItem(data["name"], data["hash"], self.ui.doodads_container)
            item.set_count((doodads_data["name"] == data["name"]).sum())
            self.ui.doodads_layout.addWidget(item)
