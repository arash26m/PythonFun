#Search pandas series operations
#https://www.youtube.com/watch?v=F6kmIpWWEdU&list=LLzEIoMmyr0gft7MAGwdX7VA&index=9&t=0s
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html#https://www.ritchieng.com/pandas-multi-criteria-filtering/
#https://www.ritchieng.com/pandas-multi-criteria-filtering/

#-------------------------------make a data frame
import pandas as pd
df=pd.DataFrame({'a' : [1 , 2, 3], 'b' : [4, 5, 6]})
df.head()

#add rows under data frame
df2=pd.DataFrame({'a':[7, 8], 'b':[9,10]})
df2.head()
df=df.append(df2)
#-------------------------------calculate sum of column a
df['a'].sum()

#import csv data
import pandas as pd
df=pd.read_csv("C:/Users/ataghi2/Desktop/Data.csv")
#or
df=pd.read_csv(r"C:\Users\ataghi2\Desktop\Data.csv")
#-------------------------------number of rows and columns
rows, columns = df.shape
df.head(2)
df.tail()
df.D1
#-------------------------------add 2 columns
D3=df.D1+df.D2
print(D3)
D4=D3*df.D1
print(D4)
#-------------------------------add new column to df
df['D3'] = D3 
df ['D4'] = D4
df
#-------------------------------delete or drop column
df.drop(['D3','D4'], axis=1)
df
df.drop(['D3'], axis=1, inplace=True)
df
del df['D4']
df
#-------------------------------drop or delete row by index
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
#-------------------------------import data again
df=pd.read_csv("C:/Users/ataghi2/Desktop/Data.csv")
df
#-------------------------------show specific columns
df[['D1','D2']]

#show specific rows and columns
df.loc[2:4,['D1','D2']]
df.loc[df.D0=='b',['D1','D2']]
#-------------------------------show statistics
df.D1.max()
df.D1.mean()
df.D1.describe()
#-------------------------------filter by condition
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
#-------------------------------Excel V-LookUp
import pandas as pd
import numpy as np

df1=pd.read_excel('C:/Users/ataghi2/Desktop/R/Python/1.xlsx')
df2=pd.read_excel('C:\\Users\\ataghi2\\Desktop\\R\\Python\\2.xlsx')
df1
df2
print(df1.columns)
print(df2.columns)
#-------------------------------rename column
df1.rename(columns={'no':'ID'}, inplace=True)
df1
#-------------------------------v-lookup
df3=pd.merge(df1, df2[['ID','Gift']], on='ID', how='left')
print(df3)

#replace nan with nothing
df3=df3.replace(np.nan, '', regex=True)
print(df3)

#write in excel
df3.to_excel('C:/Users/ataghi2/Desktop/R/Python/3.xlsx', index=False)

#-------------------------------Add a number to all cells in a column
A = 10

C = [1 , 2, 3, 4, 5]

D = []
for i in range(len(C)):
    D.append(C[i]+A)
print("D = ", D) 
#-------------------------------Another way
a=10
c=list(range(1,6))
d=[ithem+a for ithem in c]
print(f"D = {d}")

#or

A=10
C=[1, 2, 3, 4, 5, 6]
D=[ithem+A for ithem in C]
print("D = ", D) 
#-------------------------------Add two columns
D=[1, 2, 3, 4]
C=[5, 6, 7, 8]

E=[]
for i in range(len(D)):
    E.append(D[i]+C[i])
    
print('E= ', E)
#-------------------------------Make data categorical
df = pd.DataFrame({"A": ["a", "b", "c", "a"]})
df["B"] = df["A"].astype("category")
#There is a good example in W3School>Python>Machine Learning>Decision Tree
#-------------------------------Convert horizontal array to vertical array (row to column)
import numpy
X = numpy.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88])
X = numpy.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88]).reshape(-1,1)

#-------------------------------Generate 5000 random number
Ran= []

for i in range (5000):
    i = np.random.uniform (low = 0, high = 1)
    Ran.append (i)
print ("Ran = ", Ran)  
--------#or
Ran=pd.read_csv("C:/Users/ataghi2/OneDrive/0-TAMU/SHMP/Flood AAL Methodology/RandomNumbers.csv")
#convert data frame to list
Ran = Ran['invr'].values.tolist()
print(Ran[:10])
#-------------------------------Calculate Ln, average
print (np.log(10))
J = [1, 4, 8]
print (np.mean (J))
#-------------------------------Find y based on x values
#1 interpolation
import numpy as np
d = [-2,-1.5,-1,-0.5,0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10,10.5,11,11.5,12,12.5,13,13.5,14,14.5,15, 15.5, 16]
sl = [0,1.25,2.5,7.95,13.4,18.35,23.3,27.7,32.1,36.1,40.1,43.6,47.1,50.15,53.2,55.9,58.6,60.9,63.2,65.2,67.2,68.85,70.5,71.85,73.2,74.3,75.4,76.3,77.2,77.85,78.5,79,79.5,79.85,80.2,80.45,80.7]
cl = [0,1.2,2.4,5.25,8.1,10.7,13.3,15.6,17.9,19.95,22,23.85,25.7,27.25,28.8,30.15,31.5,32.65,33.8,34.75,35.7,36.45,37.2,37.8,38.4,38.8,39.2,39.45,39.7,39.85,40,40,40,40,40,40,40]
np.interp(12, d, sl)
#2 
import pandas as pd
data = {'depth' : [-2,-1.5,-1,-0.5,0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10,10.5,11,11.5,12,12.5,13,13.5,14,14.5,15, 15.5, 16],
'structure_loss' : [0,1.25,2.5,7.95,13.4,18.35,23.3,27.7,32.1,36.1,40.1,43.6,47.1,50.15,53.2,55.9,58.6,60.9,63.2,65.2,67.2,68.85,70.5,71.85,73.2,74.3,75.4,76.3,77.2,77.85,78.5,79,79.5,79.85,80.2,80.45,80.7],
'contents_loss' : [0,1.2,2.4,5.25,8.1,10.7,13.3,15.6,17.9,19.95,22,23.85,25.7,27.25,28.8,30.15,31.5,32.65,33.8,34.75,35.7,36.45,37.2,37.8,38.4,38.8,39.2,39.45,39.7,39.85,40,40,40,40,40,40,40]
        }
df = pd.DataFrame(data)
print(df.loc[df['depth'] == 5, 'structure_loss'])
#3
df.loc[df['depth'] == 16, 'contents_loss'].iloc[0]
df.loc[df['depth'] == 16, 'contents_loss'].values[0]
#4 query is like SQL
df.query('depth == 10')['contents_loss']
#-------------------------------use if inside for loop
FD = [-4, 1, 0, 5, 16, 18, 100]
FD2 = []
for i in range (len(FD)):
    if FD[i]<-2:
        FD[i]=-2
    elif FD[i]>16:
        FD[i]=16
    FD2.append (FD[i])
print("FD2 = ", FD2)
#-------------------------------Convert data frame to list
a = df['header'].values.tolist()
#-------------------------------Logarithmic regression
R_minus_one = [10-1, 50-1, 100-1, 500-1]
flood_height = [2.3, 2.8, 3.1, 3.6]

plt.scatter(R_minus_one, flood_height)
plt.show()

fit = np.polyfit(np.log(R_minus_one), flood_height, 1)
print (fit)
#-------------------------------print coefficents separatly
print (fit[0])
print (fit[1])
#-------------------------------












