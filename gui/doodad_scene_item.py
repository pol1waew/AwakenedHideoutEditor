from PySide6.QtWidgets import QGraphicsTextItem


class DoodadSceneItem(QGraphicsTextItem):
    def __init__(self, text : str, uuid : str):
        super().__init__(text)

        self.uuid = uuid

        self.setFlag(QGraphicsTextItem.GraphicsItemFlag.ItemIsMovable, True)
        self.setFlag(QGraphicsTextItem.GraphicsItemFlag.ItemIsSelectable, True)

    def on_item_moved(self):
        print(self.toPlainText())
