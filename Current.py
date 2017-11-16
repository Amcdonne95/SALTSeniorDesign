import Excel
import dict
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict
import re
from datetime import datetime


def strats(df):
    WA = lambda x: np.average(x, axis=0, weights=df.loc[x.index, 'reportingPeriodActualEndBalanceAmount'])

    for i in range(0,len(dict.bins)):
        label = ['Fico', 'APR', 'PTI', 'LTV']
        cols = ['assetNumber', 'pctDeal', 'reportingPeriodActualEndBalanceAmount', 'originalLoanTerm','originalInterestRatePercentage']
        if label == 'Fico':
            df[label[i] + 'Group'] = pd.cut(df[dict.labelKey[i]], dict.bins[label[i]], right=True, labels=dict.groups[label[i]])
            df[label[i] + 'Group'] = df[label[i] + 'Group'].cat.add_categories('No Score').fillna('No Score')
        else:
            df[label[i] + 'Group'] = pd.cut(df[dict.labelKey[i]], dict.bins[label[i]], right=True,labels=dict.groups[label[i]])

        stratTable  = df[cols].groupby([df[label[i] + 'Group']]).agg(dict.a)

    return()

def summary(df):
    WAdf = pd.DataFrame(data=dict.wAvg).rename(index=dict.avgDict)

    nonSubvented = df[df['subvented'] == '0']['pctDeal'].sum()
    subvented = df[df['subvented'] != '0']['pctDeal'].sum()

    newUsed = df[['pctDeal']].groupby(df['vehicleNewUsedCode']).sum().rename(index=dict.newUsed)
    topManufacturer = (df[['pctDeal']].groupby(df['vehicleManufacturerName']).sum()).sort_values(['pctDeal'],ascending=False).head(5)
    topModel = (df[['pctDeal']].groupby(df['vehicleModelName']).sum()).sort_values(['pctDeal'], ascending=False).head(5)
    topLocation = (df[['pctDeal']].groupby(df['obligorGeographicLocation']).sum()).sort_values(['pctDeal'],ascending=False).head(5)

    incomeVerify = df[['pctDeal']].groupby(df['obligorIncomeVerificationLevelCode']).sum().rename(index=dict.income)
    jobVerify = df[['pctDeal']].groupby(df['obligorEmploymentVerificationCode']).sum().rename(index=dict.job)

    return()

def out():

    stratTable = strats.



    return