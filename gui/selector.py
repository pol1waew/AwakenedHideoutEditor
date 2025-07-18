from PySide6.QtCore import QRect, QSize, QPoint, Qt
from PySide6.QtWidgets import QRubberBand, QGraphicsView
from PySide6.QtGui import QPainterPath


class Selector(QRubberBand):
    def __init__(self, shape : QRubberBand.Shape, parent : QGraphicsView):
        super().__init__(shape, parent)
        
        self.parent_view = parent
        self.selection_operation = Qt.ItemSelectionOperation.ReplaceSelection

    def show(self, init_pos : QPoint):
        super().show()

        self.init_pos = init_pos
        
        self.update(QSize())

    def update(self, new_pos : QPoint):
        self.setGeometry(QRect(self.init_pos, new_pos).normalized())
        self.select_overlaped_items()

    def select_overlaped_items(self):
        selected_rect = self.parent_view.mapToScene(self.geometry()).boundingRect()

        painter_path = QPainterPath()
        painter_path.addPolygon(selected_rect)

        self.parent_view.scene().setSelectionArea(painter_path, selectionOperation=self.selection_operation)

    def set_selection_mode(self, selection_operation : Qt.ItemSelectionOperation):
        self.selection_operation = selection_operation
