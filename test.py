#!/usr/bin/env python3
import pandas as pd
import bna as airport

df1 = airport.getStatus('arrivals')
n = len(df1)
df1 = df1.drop(range(n-30, n))
df1.loc[12, :]['Gate'] = 'Z99'
df1 = df1.set_index('Flight')
print(df1)
print('='*50)
print(len(df1))
df2 = airport.getStatus('arrivals')
n = len(df2)
df2 = df2.drop(range(10))
df2 = df2.reset_index(drop=True)
df2 = df2.set_index('Flight')
print(df2)
print('='*50)
print(len(df2))
df1 = df2.combine_first(df1)
print(df1)
print(len(df1))
