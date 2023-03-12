# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 11:41:03 2023

@author: sunli
"""

from PyQt5.QtWidgets import (QWidget, QLabel, QPushButton, QHBoxLayout)
import numpy as np
from database import widget_names, widget_names_1
import webbrowser

class AddWidget(QWidget):

    def __init__(self, song_name, singer_name):
        super(AddWidget, self).__init__()

        self.song_name = song_name  # Name of widget used for searching.
        self.singer_name = singer_name
        self.lbl_song = QLabel(self.song_name)
        self.lbl_singer = QLabel(self.singer_name)
        self.btn = QPushButton('点播')
        
        self.hbox = QHBoxLayout()       # A horizontal layout to encapsulate the above
        self.hbox.addWidget(self.lbl_song)   # Add the label to the layout
        self.hbox.addWidget(self.lbl_singer)   # Add the label to the layout
        self.hbox.addWidget(self.btn)    # Add the button to the layout
        self.setLayout(self.hbox)
        
        self.btn.clicked.connect(self.add_to_list)
    
    def add_to_list(self):
        content = self.lbl_song.text()
        print('play '+content)
        ind = self.find_in_list_of_list(widget_names,content)
        url_list = widget_names[ind[0]][2]
        print(url_list)
        webbrowser.open(url_list)
        # ind = np.where(widget_names==song_name)
        # url_list = widget_names[ind[0],2]
        
        
    def show(self):
        """
        Show this widget, and all child widgets.
        """
        for w in [self, self.lbl_song, self.lbl_singer, self.btn]:
            w.setVisible(True)

    def hide(self):
        """
        Hide this widget, and all child widgets.
        """
        for w in [self, self.lbl_song, self.lbl_singer, self.btn]:
            w.setVisible(False)
    
    def find_in_list_of_list(self,mylist, char):
        for sub_list in mylist:
            if char in sub_list:
                return (mylist.index(sub_list), sub_list.index(char))
        raise ValueError("'{char}' is not in list".format(char = char))