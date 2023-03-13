# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 03:06:45 2023

@author: sunli
"""

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import (
    QWidget, QLineEdit, QLabel, QPushButton, QScrollArea, QMainWindow,
    QApplication, QHBoxLayout, QVBoxLayout, QSpacerItem, QSizePolicy, QCompleter, QTableWidget
    )
from PyQt5.QtCore import QObject, Qt, pyqtSignal
import sys
from AddWidget import AddWidget
from ListWidget import ListWidget
from database import widget_names, widget_names_1



# class UI(QWidget):
#     def __init__(self):
#         super(UI, self).__init__()
#         uic.loadUi('Bar_widget.ui',self)
#         self.show()

#         self.label_song.setText(data_base[ind[0],0][0])
#         self.label_singer.setText(data_base[ind[0],1][0])
#         self.pushButton.setText('点播')
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__()

        self.controls = QWidget()
        self.controlsLayout = QVBoxLayout()
        self.controls.setLayout(self.controlsLayout)
             
        self.widgets = []
        self.setCentralWidget(self.controls)
        for name in widget_names:
            item = AddWidget(name[0],name[1])
            self.controlsLayout.addWidget(item)
            self.widgets.append(item)
            
        spacer = QSpacerItem(1, 1, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.controlsLayout.addItem(spacer)
        self.controls.setLayout(self.controlsLayout)
        
                
        
        # List for ordered song
        self.list = QWidget()
        self.listLayout = QVBoxLayout()
        self.list.setLayout(self.listLayout)
        
        self.widgets_list = []
        for name in widget_names:
            item_list = ListWidget(name[0],name[1])
            self.listLayout.addWidget(item_list)
            self.widgets_list.append(item_list)
            
        spacer = QSpacerItem(1, 1, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.listLayout.addItem(spacer)
        self.list.setLayout(self.listLayout)
        
        # Scroll Area Properties.
        self.scroll_list = QScrollArea()
        self.scroll_list.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll_list.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_list.setWidgetResizable(True)
        self.scroll_list.setWidget(self.list)
                
        # Scroll Area Properties.
        self.scroll = QScrollArea()
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.controls)

        # Search bar.
        self.searchbar = QLineEdit()
        self.searchbar.setPlaceholderText('搜索')
        self.searchbar.textChanged.connect(self.update_display)

        # Adding Completer.
        self.completer = QCompleter(widget_names_1)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.searchbar.setCompleter(self.completer)
        
        # add widgets
        searchblc = QWidget()
        searchblcLayout = QVBoxLayout()
        searchblcLayout.addWidget(self.searchbar)
        searchblcLayout.addWidget(self.scroll)
        # searchblcLayout.addWidget(self.controls)
        
        searchblc.setLayout(searchblcLayout)
        self.setCentralWidget(searchblc)
        
        container = QWidget()
        containerLayout = QHBoxLayout()
        containerLayout.addWidget(searchblc)
        containerLayout.addWidget(self.scroll_list)

        container.setLayout(containerLayout)
        self.setCentralWidget(container)

        self.setGeometry(600, 100, 800, 600)
        self.setWindowTitle('Control Panel')
        
    def update_display(self, text):

        for widget in self.widgets:
            if text.lower() in widget.song_name.lower() or text.lower() in widget.singer_name.lower():
                widget.show()
            else:
                widget.hide()
                
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())