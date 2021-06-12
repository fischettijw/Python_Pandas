# https://www.youtube.com/watch?v=NjEc7PB0TxQ

import time
import datetime
import pandas as pd
import os
os.system('cls')

ticker = 'GOOGL'

file_name = f'{ticker}.csv'
path = f"{os.path.dirname(os.path.realpath(__file__))}\\"
prgm_path = f'{os.path.dirname(os.path.realpath(__file__))}\\'
print(f'------\n{path}{file_name}\n------')

file_name = f'{ticker}.csv'
file_path = f'{os.path.dirname(os.path.realpath(__file__))}\\{file_name}'


period1 = int(time.mktime(datetime.datetime(2020, 1, 1, 23, 59).timetuple()))
period2 = int(time.mktime(datetime.datetime(2020, 12, 31, 23, 59).timetuple()))
interval = '1d'  # 1d, 1wk, 1mo

query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'
df = pd.read_csv(query_string)
print(df)


if os.path.exists(file_path):
    os.remove(file_path)
    print('remove & create', '\n')
else:
    print('create', '\n')


df.to_csv(file_path)
