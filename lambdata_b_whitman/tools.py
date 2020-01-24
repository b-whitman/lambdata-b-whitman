#!/usr/bin/env python

import scipy.stats as stats
import pandas as pd
import numpy as np


def contingency_chi2(categorical_1, categorical_2):

    '''

    contingency_chi2(categorical_1, categorical_2)

    '''
    crosstab = pd.crosstab(categorical_1, categorical_2)
    chi2, _, _, _ = stats.chi2_contingency(crosstab)
    return chi2, crosstab


def check_nulls(df):

    """

    check_nulls(df)

    Checks a dataframe for null values.

    Parameters
    ----------
    df : Pandas dataframe
        Specifies dataframe to check

    """
    nulls = df.isna().sum()
    return nulls
