# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 13:40:16 2017

@author: Hugh Krogh-Freeman
"""
import sys
import utils 

train_filename = sys.argv[1]
test_filename = sys.argv[2]

utils.classify(train_filename, test_filename)