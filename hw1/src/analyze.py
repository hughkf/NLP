# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 14:00:05 2017

@author: Hugh Krogh-Freeman
"""
import utils
import sys

model_filename, vectorized_test_data_filename = sys.argv[1], sys.argv[2]
utils.analyze(model_filename, vectorized_test_data_filename)
