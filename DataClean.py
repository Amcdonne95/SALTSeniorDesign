import Current
import dict
import pandas as pd



def cleanAdd(df):
    df['LTV'] = (df['originalLoanAmount'] / df['vehicleValueAmount']) * 100  # Loan to value ratio
    df['pctDeal'] = (df['reportingPeriodActualEndBalanceAmount'] / (
    df['reportingPeriodActualEndBalanceAmount'].sum())) * 100

    df['obligorCreditScore'] = pd.to_numeric(df['obligorCreditScore'], errors='coerce')
    df['vehicleNewUsedCode'] = pd.to_numeric(df['vehicleNewUsedCode'], errors='coerce')
    df['obligorIncomeVerificationLevelCode'] = pd.to_numeric(df['obligorIncomeVerificationLevelCode'], errors='coerce')
    df['obligorEmploymentVerificationCode'] = pd.to_numeric(df['obligorEmploymentVerificationCode'], errors='coerce')
    cs = df['obligorCreditScore'][~df.obligorCreditScore.isin(['-'])]
    cs['obligorCreditScore'] = pd.to_numeric(cs, errors='coerce')

    return df
