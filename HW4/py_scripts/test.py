#!/usr/bin/env python3
# coding: utf-8

# load data(assumed {login:pass}) from system environ path to dict

import os
import pickle


url = os.environ.get('DATABASE')

file = [file for file in os.listdir(url) if '.erv' in file][0]

# loading to dict 
with open(url+'/'+file,'rb') as f:
    c = pickle.load(f)
f.close()
 
