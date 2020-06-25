#Search pandas series operations
#https://www.youtube.com/watch?v=F6kmIpWWEdU&list=LLzEIoMmyr0gft7MAGwdX7VA&index=9&t=0s
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html#https://www.ritchieng.com/pandas-multi-criteria-filtering/
#https://www.ritchieng.com/pandas-multi-criteria-filtering/

import pandas as pd
df=pd.read_csv("C:/Users/ataghi2/Desktop/Data.csv")

#number of rows and columns
rows, columns = df.shape
df.head(2)
df.tail()
df.D1
#add 2 columns
D3=df.D1+df.D2
print(D3)
D4=D3*df.D1
print(D4)
#add new column to df
df['D3'] = D3 
df ['D4'] = D4
df
#delete or drop column
df.drop(['D3','D4'], axis=1)
df
df.drop(['D3'], axis=1, inplace=True)
df
del df['D4']
df
#drop or delete row by index
df.drop([0, 1, 2])
df
#set index for a column
df
df.set_index('D0', inplace=True)
df
df.drop(['b', 'a'],inplace=True)
df
df.reset_index(inplace=True)
df
#import data again
df=pd.read_csv("C:/Users/ataghi2/Desktop/Data.csv")
df
#show specific columns
df[['D1','D2']]

#show specific rows and columns
df.loc[2:4,['D1','D2']]
df.loc[df.D0=='b',['D1','D2']]

#show statistics
df.D1.max()
df.D1.mean()
df.D1.describe()

#filter by condition
df
x=df[df.D1>=50]
x
x=df[df.D0 == 'b']
x
x.D1.mean()
z=df[df.D == 'no']
z
z.D1
#if title has space instead of df.D1 use df['D1']
#filter by multiple conditions
df
x=df[(df.D=='yes')&(df.D0=='a')&(df.D1>10)]
x
x.D2.sum()
