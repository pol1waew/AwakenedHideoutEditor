from PySide6.QtCore import QCoreApplication, QMetaObject, QRect
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (QMainWindow, QMenu, QMenuBar,
                               QStatusBar, QHBoxLayout, 
                               QWidget, QGraphicsScene)
from gui.custom_scene import Scene
from gui.custom_view import View
from gui.doodad_list import DoodadList


class UserInterface(object):
    def setup_ui(self, main_window : QMainWindow):
        self.central_widget = QWidget(main_window)
        self.central_widget.setObjectName(u"central_widget")
        self.central_layout = QHBoxLayout(self.central_widget)
        self.central_layout.setObjectName(u"central_layout")
        self.central_widget.setLayout(self.central_layout)

        self.doodads_list = DoodadList(self.central_widget)
        self.central_layout.addWidget(self.doodads_list)

        self.scene = Scene()
        self.scene.setItemIndexMethod(QGraphicsScene.ItemIndexMethod.NoIndex)
        self.view = View(self.central_widget)
        self.view.setScene(self.scene)
        self.central_layout.addWidget(self.view)

        self.central_layout.setStretchFactor(self.doodads_list, 2)
        self.central_layout.setStretchFactor(self.view, 7)

        main_window.setCentralWidget(self.central_widget)

        self.menubar = QMenuBar(main_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 817, 33))
        main_window.setMenuBar(self.menubar)

        self.load_action = QAction(main_window)
        self.load_action.setObjectName(u"load_action")
        self.save_as_action = QAction(main_window)
        self.save_as_action.setObjectName(u"save_as_action")
        self.save_as_action.setEnabled(False)
        self.save_action = QAction(main_window)
        self.save_action.setObjectName(u"save_action")
        self.save_action.setEnabled(False)

        self.file_menu = QMenu(self.menubar)
        self.file_menu.setObjectName(u"file_menu")
        self.file_menu.addAction(self.load_action)
        self.file_menu.addAction(self.save_as_action)
        self.file_menu.addAction(self.save_action)

        self.show_all_action = QAction(main_window)
        self.show_all_action.setObjectName(u"show_all_action")
        ## TODO: move to main_window or future custom QApplication
        self.show_all_action.triggered.connect(self.scene.show_all)
        self.remove_mtx_action = QAction(main_window)
        self.remove_mtx_action.setObjectName(u"remove_mtx_action")
        self.remove_mtx_action.setEnabled(False)

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
        self.load_action.setText(QCoreApplication.translate("MainWindow", u"Load from file", None))
        self.save_as_action.setText(QCoreApplication.translate("MainWindow", u"Save as", None))
        self.save_action.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.file_menu.setTitle(QCoreApplication.translate("MainWindow", u"File", None))

        self.show_all_action.setText(QCoreApplication.translate("MainWindow", u"Show all doodads", None))
        self.remove_mtx_action.setText(QCoreApplication.translate("MainWindow", u"Remove all MTX's", None))
        self.funcs_menu.setTitle(QCoreApplication.translate("MainWindow", u"Funcs", None))
