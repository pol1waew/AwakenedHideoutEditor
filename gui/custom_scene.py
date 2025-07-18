from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QGraphicsScene, QGraphicsTextItem, QGraphicsSceneMouseEvent, QRubberBand
from PySide6.QtGui import QKeyEvent
from collections import defaultdict
from gui.doodad_scene_item import DoodadSceneItem


class Scene(QGraphicsScene):
    def __init__(self, parent : QWidget = None):
        super().__init__(parent)
        
        self.can_move_items = True

        self.comparison_dict = defaultdict(list)

        self.pivot_marker = QGraphicsTextItem("+")
        self.pivot_marker.setPos(0., 0.)
        #self.addItem(self.pivot_marker)

    def create_item(self, display_name : str, uuid : str, doodad_hash : int, pos_x : float, pos_y : float):
        scene_item = DoodadSceneItem("+" + display_name, uuid, doodad_hash)
        scene_item.setPos(pos_x, pos_y)

        self.addItem(scene_item)
        self.comparison_dict[doodad_hash].append(scene_item)

    def change_item_visibility(self, doodad_hash : int, is_visible : bool):
        for item in self.comparison_dict[doodad_hash]:
            item.setVisible(is_visible)

    def show_only(self, doodad_hash : int):
        self.change_item_visibility(doodad_hash, True)

        for hash in self.comparison_dict.keys():
            if hash != doodad_hash:
                self.change_item_visibility(hash, False)

    def show_all(self):
        for hash in self.comparison_dict.keys():
            self.change_item_visibility(hash, True)

    def mousePressEvent(self, event : QGraphicsSceneMouseEvent):
        if self.can_move_items:
            super().mousePressEvent(event)

    def mouseReleaseEvent(self, event : QGraphicsSceneMouseEvent):
        moved_item = self.mouseGrabberItem()

        super().mouseReleaseEvent(event)
    
        if moved_item and not self.mouseGrabberItem():
            self.item_moved()

    def keyPressEvent(self, event : QKeyEvent):
        if event.key() == Qt.Key.Key_Shift:
            self.can_move_items = False

        super().keyPressEvent(event)

    def keyReleaseEvent(self, event : QKeyEvent):
        if event.key() == Qt.Key.Key_Shift:
            self.can_move_items = True

        super().keyReleaseEvent(event)

    def item_moved(self):
        print("qqqqq")
