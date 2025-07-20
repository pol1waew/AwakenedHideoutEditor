from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from gui.custom_scene import Scene


class DoodadListItem(QWidget):
    scene_ref : Scene


    def __init__(self, display_name : str, doodad_hash : int, parent : QWidget = None):
        super().__init__(parent)

        self.doodad_hash = doodad_hash
        self.is_related_doodads_visible = True

        self.setup_ui(display_name)         

    def setup_ui(self, display_name : str):
        self.item_layout = QVBoxLayout(self)
        self.item_layout.setObjectName(u"doodad_list_item_layout")
        self.setLayout(self.item_layout)

        self.labels_container = QWidget(self)
        self.labels_container.setObjectName(u"labels_container")
        self.labels_layout = QHBoxLayout(self.labels_container)
        self.labels_layout.setObjectName(u"labels_layout")
        self.labels_container.setLayout(self.labels_layout)

        self.doodad_name_label = QLabel(self, text=display_name)
        self.doodad_name_label.setObjectName(u"doodad_name_label")
        self.doodad_count_label = QLabel(self, text="x1")
        self.doodad_count_label.setObjectName(u"doodad_count_label")

        self.labels_layout.addWidget(self.doodad_name_label)
        self.labels_layout.addWidget(self.doodad_count_label)
        self.item_layout.addWidget(self.labels_container)

        self.buttons_container = QWidget(self)
        self.buttons_container.setObjectName(u"buttons_container")
        self.buttons_layout = QHBoxLayout(self.buttons_container)
        self.buttons_layout.setObjectName(u"horizontal_layout")
        self.buttons_container.setLayout(self.buttons_layout)

        self.visibility_button = QPushButton(self)
        self.visibility_button.setObjectName(u"visibility_button")
        self.visibility_button.setText("Hide all")
        self.visibility_button.clicked.connect(self.on_visibility_button_click)

        self.show_only_button = QPushButton(self)
        self.show_only_button.setObjectName(u"show_only_button")
        self.show_only_button.setText("Show only")
        self.show_only_button.clicked.connect(self.on_show_only_button_click)

        self.buttons_layout.addWidget(self.visibility_button)
        self.buttons_layout.addWidget(self.show_only_button)
        self.item_layout.addWidget(self.buttons_container) 

    def set_count(self, value : int):
        self.doodad_count_label.setText("x{}".format(value))

    @classmethod
    def set_scene_reference(cls, scene : Scene):
        cls.scene_ref = scene

    @Slot()
    def on_visibility_button_click(self):
        self.is_related_doodads_visible = not self.is_related_doodads_visible

        DoodadListItem.scene_ref.change_item_visibility(self.doodad_hash, self.is_related_doodads_visible)

        self.visibility_button.setText("Hide all" if self.is_related_doodads_visible else "Show all")

    @Slot()
    def on_show_only_button_click(self):
        DoodadListItem.scene_ref.show_only(self.doodad_hash)
