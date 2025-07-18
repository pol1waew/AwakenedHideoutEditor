from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
                           QCursor, QFont, QFontDatabase, QGradient,
                           QIcon, QImage, QKeySequence, QLinearGradient,
                           QPainter, QPalette, QPixmap, QRadialGradient,
                           QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
                               QSizePolicy, QStatusBar, QVBoxLayout, QHBoxLayout, 
                               QWidget, QPushButton, QLayout, QScrollArea, QGraphicsScene)
from gui.custom_scene import Scene
from gui.custom_view import View


class UserInterface(object):
    def setup_ui(self, main_window : QMainWindow):
        self.central_widget = QWidget(main_window)
        self.central_widget.setObjectName(u"central_widget")
        self.central_layout = QHBoxLayout(self.central_widget)
        self.central_layout.setObjectName(u"central_layout")
        self.central_widget.setLayout(self.central_layout)

        self.doodads_container = QWidget(self.central_widget)
        self.doodads_container.setObjectName(u"doodads_container")
        self.doodads_layout = QVBoxLayout(self.doodads_container)
        self.doodads_layout.setObjectName(u"doodads_layout")
        #self.doodads_layout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.doodads_container.setLayout(self.doodads_layout)
        self.doodads_scroll_area = QScrollArea(self.central_widget)
        self.doodads_scroll_area.setObjectName(u"doodads_scroll_area")
        self.doodads_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.doodads_scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.doodads_scroll_area.setWidgetResizable(True)
        self.doodads_scroll_area.setWidget(self.doodads_container)
        self.central_layout.addWidget(self.doodads_scroll_area)

        self.scene = Scene()
        self.scene.setItemIndexMethod(QGraphicsScene.ItemIndexMethod.NoIndex)
        self.view = View(self.central_widget)
        self.view.setScene(self.scene)
        self.central_layout.addWidget(self.view)

        self.central_layout.setStretchFactor(self.doodads_scroll_area, 2)
        self.central_layout.setStretchFactor(self.view, 7)

        main_window.setCentralWidget(self.central_widget)

        self.menubar = QMenuBar(main_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 817, 33))
        main_window.setMenuBar(self.menubar)

        self.override_action = QAction(main_window)
        self.override_action.setObjectName(u"override_action")
        self.save_action = QAction(main_window)
        self.save_action.setObjectName(u"save_action")

        self.file_menu = QMenu(self.menubar)
        self.file_menu.setObjectName(u"file_menu")
        self.file_menu.addAction(self.save_action)
        self.file_menu.addAction(self.override_action)

        self.show_all_action = QAction(main_window)
        self.show_all_action.setObjectName(u"show_all_action")
        self.show_all_action.triggered.connect(self.scene.show_all)
        self.remove_mtx_action = QAction(main_window)
        self.remove_mtx_action.setObjectName(u"remove_mtx_action")

        self.funcs_menu = QMenu(self.menubar)
        self.funcs_menu.setObjectName(u"funcs_menu")
        self.funcs_menu.addAction(self.show_all_action)
        self.funcs_menu.addAction(self.remove_mtx_action)

        self.statusbar = QStatusBar(main_window)
        self.statusbar.setObjectName(u"statusbar")
        main_window.setStatusBar(self.statusbar)

        self.menubar.addAction(self.file_menu.menuAction())
        self.menubar.addAction(self.funcs_menu.menuAction())

        self.retranslate_ui()

        QMetaObject.connectSlotsByName(main_window)

    def retranslate_ui(self):
        self.override_action.setText(QCoreApplication.translate("MainWindow", u"Override existing", None))
        self.save_action.setText(QCoreApplication.translate("MainWindow", u"Save as new", None))
        self.show_all_action.setText(QCoreApplication.translate("MainWindow", u"Show all doodads", None))
        self.remove_mtx_action.setText(QCoreApplication.translate("MainWindow", u"Remove all MTX's", None))
        self.file_menu.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.funcs_menu.setTitle(QCoreApplication.translate("MainWindow", u"Funcs", None))
