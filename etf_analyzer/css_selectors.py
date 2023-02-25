'''
Contains CSS selectors for data points.
'''

CSS_SELECTORS = {
    'Inception Date': 'div.mb-10:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2)',
    'Expense Ratio': 'div.mb-10:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2)',
    'Type': 'div.border-black\/20:nth-child(3) > div:nth-child(2)',
    'Fund Owner': 'div.flex:nth-child(4) > div:nth-child(2)',
    'Volume (1M avg. daily)': 'div.flex:nth-child(5) > div:nth-child(2)',
    'AUM': 'div.flex:nth-child(6) > div:nth-child(2)',
    'Associated Index': 'div.flex:nth-child(7) > div:nth-child(2)',
    'Inverse/Leveraged': 'div.flex:nth-child(8) > div:nth-child(2)',
    'Passive/Active': 'div.flex:nth-child(9) > div:nth-child(2)',
    'Fractionable on Composer': 'div.flex:nth-child(10) > div:nth-child(2)',
    'Top 1st Holding': ['div.grid-cols-\[0fr_1fr_0fr\]:nth-child(1) > div:nth-child(1) > span:nth-child(1)', 'div.grid-cols-\[0fr_1fr_0fr\]:nth-child(1) > div:nth-child(3)'],
    'Top 2nd Holding': ['div.grid:nth-child(2) > div:nth-child(1) > span:nth-child(1)', 'div.grid:nth-child(2) > div:nth-child(3)'],
    'Top 3rd Holding': ['div.grid:nth-child(3) > div:nth-child(1) > span:nth-child(1)', 'div.grid:nth-child(3) > div:nth-child(3)'],
    'Top 4th Holding': ['div.grid:nth-child(4) > div:nth-child(1) > span:nth-child(1)', 'div.grid:nth-child(4) > div:nth-child(3)'],
    'Top 5th Holding': ['div.grid:nth-child(5) > div:nth-child(1) > span:nth-child(1)', 'div.grid:nth-child(5) > div:nth-child(3)'],
    'Top 6th Holding': ['div.grid:nth-child(6) > div:nth-child(1) > span:nth-child(1)', 'div.grid:nth-child(6) > div:nth-child(3)'],
    'Top 7th Holding': ['div.grid:nth-child(7) > div:nth-child(1) > span:nth-child(1)', 'div.grid:nth-child(7) > div:nth-child(3)'],
    'Top 8th Holding': ['ddiv.grid:nth-child(8) > div:nth-child(1) > span:nth-child(1)', 'div.grid:nth-child(8) > div:nth-child(3)'],
    'Top 9th Holding': ['div.grid:nth-child(9) > div:nth-child(1) > span:nth-child(1)', 'div.grid:nth-child(9) > div:nth-child(3)'],
    'Top 10th Holding': ['div.grid:nth-child(10) > div:nth-child(1) > span:nth-child(1)', 'div.grid:nth-child(10) > div:nth-child(3)'],
}