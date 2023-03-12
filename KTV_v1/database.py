# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 16:02:42 2023

@author: sunli
"""

import numpy as np
import os
import webbrowser

# addr = os.path.join(os.path.expanduser('~'),'Desktop')+'\Test_songlist.txt'
addr = os.path.abspath(os.path.dirname((__file__)))+'/Test_songlist.txt'
data_base = np.loadtxt(addr,encoding="utf8", dtype='str')
widget_names = data_base.tolist()
widget_names_1 = [element for sublist in [i[:2] for i in widget_names[:]] for element in sublist]
widget_names_1 = list(set(widget_names_1))