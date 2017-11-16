from collections import OrderedDict



WA = lambda x: np.average(x, axis=0, weights = df.loc[x.index, 'reportingPeriodActualEndBalanceAmount'])

income = {
    1:'Not Stated, Not Verified',
    2:'Stated, Not Verified',
    3:'Stated, Verified',
    4:'Stated, Verified: 12 M',
    5:'Stated, Verified: 24 M'
}

job =  {
    1:'Not Stated, Not Verified',
    2:'Stated, Not Verified',
    3:'Stated, Third Party Verified'
}

newUsed = {
    1:'New Vehicle',
    2:'Used Vehicle'
}

avgDict = {
    0:'Credit Score at Origination',
    1:'Remaining Term to Maturity',
    2:'APR at Origination',
    3:'Payment to Income'
}

wAvg = {
    'Weighted Average':[WA(cs['obligorCreditScore']),
                                WA(df['remainingTermToMaturityNumber']),
                                WA(df['originalInterestRatePercentage']),
                                WA(df['paymentToIncomePercentage'])]
}

a = OrderedDict([
        ('assetNumber', ['count']),
        ('reportingPeriodActualEndBalanceAmount', ['sum', 'mean']),
        ('pctDeal', ['sum']),
        ('originalLoanTerm', [WA]),
        ('originalInterestRatePercentage', [WA])
    ])

labelKey = {
    'Fico':'obligorCreditScore',
    'APR':'originalInterestRatePercentage',
    'LTV':'LTV',
    'PTI':'paymentToIncomePercentage'
}

bins = {
    'Fico':[-1, 440, 500, 560, 620, 680, 740, 800, 1000],
    'APR':[0, .04, .08, .12, .16, .20, .24, .28, 1000],
    'LTV':[-1, .7, .8, .9, 1, 1.1, 1.2, 1.3, 1.4, 1000],
    'PTI':[-1, .02, .04, .06, .08, .1, .12, .14, .16, 1000]
}

groups = {
    'Fico':['[-1, 440)', '[440, 500)', '[500, 560)', '[560, 620)', '[620, 680)', '[680, 740)', '[740, 800)','[800, 1000)'],
    'APR':['[0.0, 0.04)', '[0.04, 0.08)', '[0.08, 0.12)', '[0.12, 0.16)', '[0.16, 0.20)', '[0.20, 0.24)','[0.24, 0.28)', '[0.28, 1000)'],
    'LTV':['[-1.0, 0.7)', '[0.7, 0.8)', '[0.8, 0.9)', '[0.9, 1.0)', '[1.0, 1.1)', '[1.1, 1.2)', '[1.2, 1.3)','[1.3, 1.4)', '[1.4, 1000.0)'],
    'PTI':['[-1.0, 0.02)', '[0.02, 0.04)', '[0.04, 0.06)', '[0.06, 0.08)', '[0.08, 0.1)', '[0.1, 0.12)','[0.12, 0.14)', '[0.14, 0.16)', '[0.16, 1000.0)']
}
