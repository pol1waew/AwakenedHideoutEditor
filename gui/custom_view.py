from PySide6.QtCore import Qt, QRect
from PySide6.QtWidgets import QWidget, QGraphicsView, QRubberBand
from PySide6.QtGui import QMouseEvent, QKeyEvent
from gui.selector import Selector


class View(QGraphicsView):
    def __init__(self, parent : QWidget = None):
        super().__init__(parent)

        self.can_select_items = True
        self.selector = Selector(QRubberBand.Shape.Rectangle, self)
        self.setResizeAnchor(self.ViewportAnchor.AnchorUnderMouse)
        

        #self.verticalScrollBar().blockSignals(True)
        #self.horizontalScrollBar().blockSignals(True)
        #self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        #self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

    def mousePressEvent(self, event : QMouseEvent):
        if self.can_select_items and not self.itemAt(event.pos()):
            self.selector.show(event.pos())

        super().mousePressEvent(event)

    def mouseMoveEvent(self, event : QMouseEvent):
        if not self.selector.isHidden():
            self.selector.update(event.pos())

        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event : QMouseEvent):
        if not self.selector.isHidden():
            #self.fitInView(self.selection.geometry(), Qt.AspectRatioMode.KeepAspectRatio)
            self.selector.hide()

        super().mouseReleaseEvent(event)

    def keyPressEvent(self, event : QKeyEvent):
        if event.key() == Qt.Key.Key_Shift:
            self.can_select_items = False
            self.setDragMode(self.DragMode.ScrollHandDrag)
        elif event.key() == Qt.Key.Key_Control:
            self.selector.set_selection_mode(Qt.ItemSelectionOperation.AddToSelection)
        elif event.key() == Qt.Key.Key_Escape:
            self.fitInView(self.sceneRect(), Qt.AspectRatioMode.KeepAspectRatio)

        super().keyPressEvent(event)

    def keyReleaseEvent(self, event : QKeyEvent):
        if event.key() == Qt.Key.Key_Shift:
            self.can_select_items = True
            self.setDragMode(self.DragMode.NoDrag)
        elif event.key() == Qt.Key.Key_Control:
            self.selector.set_selection_mode(Qt.ItemSelectionOperation.ReplaceSelection)

        super().keyReleaseEvent(event)
