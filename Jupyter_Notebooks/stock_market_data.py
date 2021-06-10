# https://www.youtube.com/watch?v=NjEc7PB0TxQ

import time
import datetime
import pandas as pd
import os
os.system('cls')

print(os.getcwd())


path = f"{os.path.dirname(os.path.realpath(__file__))}\\"
ticker = 'IBM'
file_name = f'{ticker}.csv'

period1 = int(time.mktime(datetime.datetime(2020, 1, 1, 23, 59).timetuple()))
period2 = int(time.mktime(datetime.datetime(2020, 12, 31, 23, 59).timetuple()))
interval = '1d'  # 1d, 1wk, 1mo

query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'
print('\n', query_string, '\n')
df = pd.read_csv(query_string)
print(df)

if os.path.exists(f'{path}{file_name}'):
    os.remove(f'{path}{file_name}')
    print('remove & create', '\n')
else:
    print('create', '\n')

df.to_csv(f'{path}{file_name}')
