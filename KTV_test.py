# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 14:27:40 2023

@author: yaoli
"""
import numpy as np
import os
import webbrowser

# addr = os.path.join(os.path.expanduser('~'),'Desktop')+'/Test_songlist.txt'
addr = os.path.abspath(os.path.dirname((__file__)))+'/Test_songlist.txt'


name = input("請輸入歌名: ")
data_base = np.loadtxt(addr,encoding="utf8", dtype='str')
ind = np.where(data_base==name)
url_list = data_base[ind[0],2]
print(url_list)
webbrowser.open(url_list[0])


# # 增加
# data_base.append("e")   
# # 加入
# data_base.insert(0, '1')   
#   # 移除 
# data_base.pop()
# # 複製
# data1 = data_base.copy()
# print('2.',data_base)
# print(data1)

# number = 0;
# for i in range(1,101):
#     number = number+i
# print(number)

# data_base = open(addr,encoding="utf8").read()
