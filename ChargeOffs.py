import Excel

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict
import re
from datetime import datetime

def aggChargeOffs():
    agg_df = pd.DataFrame()
    for i in range(0, len(Excel.dfTapes[Excel.deal].index)):
        if Excel.dfTapes[Excel.deal][i] == 'None':
            break
        else:
            path = Excel.directory + '\\' + Excel.shelf + '\\' + Excel.deal + '\\' + Excel.dfTapes[Excel.deal][i]

            df = pd.read_csv(path, memory_map=True, low_memory=False)
            df = df[~df.zeroBalanceCode.isin(['-'])]
            # df['Month'] =
            agg_df = pd.concat([agg_df, df])

    return agg_df

