from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QScrollArea
import pandas as pd
from gui.doodad_list_item import DoodadListItem


class DoodadList(QScrollArea):
    def __init__(self, parent : QWidget):
        super().__init__(parent)

        self.setup_ui()

    def setup_ui(self):
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setWidgetResizable(True)

        self.list_container = QWidget(self)
        self.list_container.setObjectName(u"doodad_list_container")
        self.list_layout = QVBoxLayout(self)
        self.list_layout.setObjectName(u"doodad_list_layout")
        #self.doodads_layout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.list_container.setLayout(self.list_layout)

        self.setWidget(self.list_container)

    def load_hideout_data(self, doodads_data : pd.DataFrame):
        for i, data in doodads_data.drop_duplicates(subset=["hash"]).iterrows():
            self.create_item(data["name"], 
                             data["hash"], 
                             (doodads_data["name"] == data["name"]).sum())

    def create_item(self, display_name : str, doodad_hash : int, count : int):
        item = DoodadListItem(display_name, doodad_hash, self)
        item.set_count(count)

        self.list_layout.addWidget(item)
