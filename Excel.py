
import xlwings as xw
import numpy as np

wb = xw.Book('Salt.xlsm')
setup = wb.sheets('Setup')
output = wb.sheets('Output')
strats = wb.sheets('Strat Tables')
performance = wb.sheets('Performance')

# Path For the Current deal that is selected based on Setup
directory = setup['Directory'].value
shelf = setup['Shelf'].value
deal = setup['Deal'].value
report = setup['Report'].value
tapes = np.array(setup['Tapes'].value)

#Based on the output Tab

deal_select = output['Deal_Selection'].value
month_select = output['Month_Selection'].value

