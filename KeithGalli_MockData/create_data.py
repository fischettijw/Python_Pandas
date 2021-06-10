# https://www.youtube.com/watch?v=VJBY2eVtf7o&list=PLFCB5Dp81iNVmuoGIqcT5oF4K-7kTI5vp&index=10

import pandas as pd
import numpy as np
import random
import datetime
import os
os.system('cls')


columns = ['Order ID', 'Product', 'Quantity Ordered',
           'Price Each', 'Order Date', 'Purchase Address']

products = {
    # Product: [Price, weight]
    'iPhone': [700, 10],
    'Google Phone': [600, 8],
    'Vareebadd Phone': [400, 3],
    '20in Monitor': [109.99, 6],
    '34in Ultrawide Monitor': [379.99, 9],
    '27in 4K Gaming Monitor': [389.99, 9],
    '27in FHD Monitor': [149.99, 11],
    'Flatscreen TV': [300, 7],
    'Macbook Pro Laptop': [1700, 7],
    'ThinkPad Laptop': [999.99, 6],
    'AA Batteries (4-pack)': [3.84, 30],
    'AAA Batteries (4-pack)': [2.99, 30],
    'USB-C Charging Cable': [11.95, 30],
    'Lightning Charging Cable': [14.95, 30],
    'Wired Headphones': [11.99, 26],
    'Bose SoundSport Headphones': [99.99, 19],
    'Apple Airpods Headphones': [150, 22],
    'LG Washing Machine': [600.00, 1],
    'LG Dryer': [600.00, 1]
}

product_list = [product for product in products]
weights = [products[product][1] for product in products]

path = '.\KeithGalli_MockData\\'

df = pd.DataFrame(columns=columns)

order_id = 143253

for i in range(1000):
    product = random.choices(product_list, weights=weights)[0]
    # product = random.choice(list(products.keys()))
    price = products[product]
    df.loc[i] = [order_id, product, 1, price, 'NA', 'NA']
    order_id += 1

print('\n', product_list, '\n')
print(weights, '\n')

if os.path.exists(path + 'test_data.csv'):
    os.remove(path + 'test_data.csv')
    print('remove & create', '\n')
else:
    print('create', '\n')

df.to_csv(path + 'test_data.csv', '\n')

print(df.sample(n=20), '\n')
