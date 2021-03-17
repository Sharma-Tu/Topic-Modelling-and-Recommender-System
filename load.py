# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 13:40:14 2020

@author: tusha
"""

import pandas as pd
import gzip
import json
import re
from os import listdir
from os.path import isfile, join
from pathlib import Path

###     Load all files in a directory      ###

mypath = './Data/'

def parse(path):
  g = gzip.open(path, 'rb')
  for l in g:
    yield json.loads(l)

def getDF(path):
    i = 0
    df = {}
    
    for d in parse(path):
        df[i] = d
        i += 1
    return pd.DataFrame.from_dict(df, orient='index')

onlyfiles = [join(mypath,f) for f in listdir(mypath) if isfile(join(mypath, f))]

df_list = []

def loadDF(s=1e10):        
    for f in onlyfiles:
        if Path(f).stat().st_size<s:
            cat = re.search('Data/(.*)_5.json',f).group(1)
            df_file = getDF(f)
            df_file['category']=cat
            df_list.append(df_file)
            
    df = pd.concat(df_list, ignore_index = True, sort=False)
    return(df)

if __name__ == '__main__':
    df = loadDF()
    print(df.shape)
