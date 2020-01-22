#!/usr/bin/env python

'''

contingency_chi2(categorical_1, categorical_2)

'''

import scipy.stats as stats
import pandas as pd

def contingency_chi2(categorical_1, categorical_2):
    crosstab = pd.crosstab(categorical_1, categorical_2)
    chi2 = stats.contingency_chi2(crosstab)
    return chi2, crosstab

def add(x, y):
    return x + y

foo = 2
bar = 4