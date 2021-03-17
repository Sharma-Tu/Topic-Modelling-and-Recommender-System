# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 20:38:37 2020

@author: tusha
"""


import load
import matplotlib.pyplot as plt
#import pandas as pd

df = load.loadDF()



"""Group the data by reviewerID and take frequeny
of reviews posted. Plot the histograms"""

fig, ax = plt.subplots()
freq = df['reviewerID'].value_counts()
freq = freq[freq.between(freq.quantile(.01), freq.quantile(.99))]
freq.plot.hist(bins = 12)
