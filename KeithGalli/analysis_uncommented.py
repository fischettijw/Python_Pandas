# https://youtu.be/vmEHCJofslg
# https://www.kaggle.com/datasets
# https://pandas.pydata.org/docs/

import re
import pandas as pd
import os
os.system('cls')

df = pd.read_csv('.\KeithGalli\pokemon_data.csv')
df = pd.read_excel('.\KeithGalli\pokemon_data.xlsx')
df = pd.read_csv('.\KeithGalli\pokemon_data.txt', delimiter='\t')


print(df, '\n')
print(df.head(8), '\n')
print(df.tail(8), '\n')
print(df.columns, '\n')
print(df['Name'][0:7], '\n')
print(df[['#', 'Name', 'Type 2']][0:7], '\n')

print(df.iloc[2], '\n')
print(df.iloc[2:6], '\n')
print(df.iloc[6, 3], '\n')

for index, row in df.iterrows():
    print(index, row['Name'], '\n')

print(df.loc[df['Type 1'] == 'Fire'])

print(df.describe(), '\n')

print(df.sort_values('Name'), '\n')

print(df.sort_values(['Type 1', 'HP'], ascending=[1, 0]), '\n')

print(df.columns, '\n')
df['TOTAL'] = df['HP'] + df['Attack'] + df['Defense'] + \
    df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
print(df.head(8), '\n')
df = df.drop(columns=['TOTAL'])
print(df.head(8), '\n')
# https: // youtu.be/vmEHCJofslg?t = 1201
df['TOTAL'] = df.iloc[:, 4:10].sum(axis=1)
print(df.head(8), '\n')


cols = list(df.columns)
df = df[cols[0:4] + [cols[-1]] + cols[4:14]]
print(df.head(8), '\n')
df.to_csv(('.\KeithGalli\pokemon_data_mofified.csv'))

# https://youtu.be/vmEHCJofslg?t=1912

new_df = df.loc[(df['Type 1'] == 'Grass') & (
    df['Type 2'] == 'Poison') & (df['HP'] > 70)]
new_df.reset_index(drop=True, inplace=True)
new_df.to_csv(('.\KeithGalli\pokemon_data_filtered.csv'))
print(new_df, '\n')
print(df.loc[df['Name'].str.contains('Mega')])
print(df.loc[~df['Name'].str.contains('Mega')])
print(df.loc[df['Type 1'].str.contains('Fire|Grass', regex=True)])


# Aggregate Statistics(Groupby)
print(df, '\n')
df_stat = df.groupby(['Type 1']).mean()
print(df_stat, '\n')
df_stat = df.groupby(['Type 1']).mean().sort_values('Defense', ascending=False)
print(df_stat, '\n')
df_stat = df.groupby(['Type 1', 'Type 2']).count()
print(df_stat, '\n')
