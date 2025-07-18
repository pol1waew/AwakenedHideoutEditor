from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, Qt
from PySide6.QtWidgets import QMainWindow, QWidget, QGraphicsTextItem, QGraphicsTextItem
from gui.user_interface import UserInterface
from gui.doodad_list_item import DoodadListItem
from logic.hideout_parser import HideoutParser


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Awakened Hideout Editor")
        self.setObjectName(u"main_window")
        self.setEnabled(True)
        self.resize(1280, 720)

        self.ui = UserInterface()
        self.ui.setup_ui(self)

        DoodadListItem.set_scene_reference(self.ui.scene)
        self.parser = HideoutParser("logic/2B Dreadnought-1.0.hideout")

        for i, data in self.parser.decorations_data.iterrows():
            self.ui.scene.create_item(data["name"], data["uuid"], data["hash"], data["x"], data["y"])

        for i, data in self.parser.decorations_data.drop_duplicates(subset=["hash"]).iterrows():
            item = DoodadListItem(data["name"], data["hash"], self.ui.doodads_container)
            item.set_count((self.parser.decorations_data["name"] == data["name"]).sum())
            self.ui.doodads_layout.addWidget(item)
