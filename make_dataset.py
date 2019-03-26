#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 22:40:20 2019

@author: xinchen
"""

import numpy as np
import os
import shutil

#folder = "./Dataset"
#
#if not os.path.exists(folder):
#    os.makedirs(folder)


# Create folders
data_dir='/Users/jinge/Documents/MAP583/VireoFood172'
folder_train = data_dir + "/Dataset/train"
folder_val = data_dir + "/Dataset/val"
folder_test = data_dir + "/Dataset/test"


num = np.arange(172)+1

for i in num:
    f_train = os.path.join(folder_train,str(i))
    f_val = os.path.join(folder_val,str(i))
    f_test = os.path.join(folder_test,str(i))
    if not os.path.exists(f_train):
        os.makedirs(f_train)
    if not os.path.exists(f_val):
        os.makedirs(f_val)
    if not os.path.exists(f_test):
        os.makedirs(f_test)

# Move images
        
TR_name = open('./SplitAndIngreLabel/TR.txt', 'r').read().split('\n')[:-1]
for i in TR_name:
    source = os.path.join("./ready_chinese_food", i[1:])
    destination = os.path.join("./Dataset/train", i[1:])
    shutil.copy(source, destination)
    
VAL_name = open('./SplitAndIngreLabel/VAL.txt', 'r').read().split('\n')[:-1]
for i in VAL_name:
    source = os.path.join("./ready_chinese_food", i[1:])
    destination = os.path.join("./Dataset/val", i[1:])
    shutil.copy(source, destination)

TE_name = open('./SplitAndIngreLabel/TE.txt', 'r').read().split('\n')[:-1]
for i in TE_name:
    source = os.path.join("./ready_chinese_food", i[1:])
    destination = os.path.join("./Dataset/test", i[1:])
    shutil.copy(source, destination)