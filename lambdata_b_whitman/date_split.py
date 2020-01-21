#!/usr/bin/env python

'''

date_split()

Accepts a date array, formats it as a datetime object using default pandas to_datetime behavior, and splits it into year, month, and day arrays. Adds those arrays to starting dataframe.

Parameters
----------
df : Pandas dataframe

Dataframe containing date array to be split

date_col : str

Name of column containing dates to be split

'''

import pandas as pd
import numpy as np

def date_split(df, date_col):
    df[dates_dt] = pd.to_datetime(df[date_col])
    year = df[dates_dt].dt.year
    month = df[dates_dt].dt.month
    day = df[dates_dt].dt.day

    return year, month, day

def add(x, y):
    return x + y

foo = 2
bar = 4