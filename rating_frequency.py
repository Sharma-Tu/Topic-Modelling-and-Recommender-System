# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 13:25:38 2020

@author: tusha
"""


"""Frequency for each rating

"""


import load
import matplotlib.pyplot as plt
#import pandas as pd

df = load.loadDF()



"""Group the data by reviewerID and take frequeny
of reviews posted. Plot the histograms"""

fig, ax = plt.subplots()
freq = df['overall'].value_counts().sort_index()
freq.plot.bar()
plt.title("Ratings Frequency")
plt.show()