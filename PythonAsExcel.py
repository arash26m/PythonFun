#Search pandas series operations
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html

import pandas as pd
df=pd.read_csv("C:/Users/ataghi2/Desktop/RData.csv")

#number of rows and columns
rows, columns = df.shape
df.head(2)
df.tail()
df.D1
#add 2 columns
D4=df.D1+df.D2
D5=D4+df.D1
#add new column to df
df['D4'] = D4 

#Delete or drop column
df.drop(['D1','D2'], axis=1)
df.drop(['D1','D2'], axis=1, inplace=True)
del df['D1']

#Drop or delete row by index
df.drop([0, 1])

df.set_index('D3', inplace=True)
df.drop(['b', 'a'],inplace=True)
df.reset_index(inplace=True)

#show specific columns
df[['D1',D3']]

#show specific rows and columns
df.loc[2:4,['D1','D2']]
df.loc[df.D3=='b',['D1','D2']]

#show statistics
df.D1.max()
df.D1.mean()
df.D1.describe()

#filter by condition
x=df[df.D1>=20]
x=df[df.D3 == 'b']
x.D1.mean()
df[df.D1]
df.D1[df[df.D3 == 'b']]
#if title has space instead of df.D1 use df['D1']