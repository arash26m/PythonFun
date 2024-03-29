#Search pandas series operations
#https://www.youtube.com/watch?v=F6kmIpWWEdU&list=LLzEIoMmyr0gft7MAGwdX7VA&index=9&t=0s
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html#https://www.ritchieng.com/pandas-multi-criteria-filtering/
#https://www.ritchieng.com/pandas-multi-criteria-filtering/
#-------------------------------comment a block
"""
this is big block of texts
"""
#-------------------------------make a data frame 
import pandas as pd
df=pd.DataFrame({'a' : [1 , 2, 3], 'b' : [4, 5, 6]})
df.head()

#add rows under data frame or combine two dataframe
df2=pd.DataFrame({'a':[7, 8], 'b':[9,10]})
df2.head()
df=df.append(df2)
#-------------------------------calculate sum of column a
df['a'].sum()
#-------------------------------import csv data
import pandas as pd
df=pd.read_csv("C:/Users/ataghi2/Desktop/Data.csv")
#or
df=pd.read_csv(r"C:\Users\ataghi2\Desktop\Data.csv")
#-------------------------------import excel data
import pandas as pd
df = pd.read_excel(r'C:\Users\arasht\OneDrive\0-TAMU\AAL Flood\original-input_ex.xlsx', sheet_name='original-input')
print(df)
#-------------------------------write on a csv file
import pandas as pd
cities = pd.DataFrame([['Sacramento', 'California'], ['Miami', 'Florida']], columns=['City', 'State'])
cities.to_csv('cities.csv')
#-------------------------------write on an Excel file
filename = "output.xlsx"
df.to_excel(filename, index=False)
#-------------------------------put list data to csv file
import pandas as pd
list_name = ['item_1', 'item_2', 'item_3']
df = pd.DataFrame (list_name, columns = ['column_name'])
print(df)
df.to_csv('csv name.csv')
#-------------------------------put multiple lists to csv file or convert list to dataframe
import pandas as pd
al=[]
for i in range (10):
    al.append(i)
print(al)
bl=[]
for i in range (len(al)):
    bl.append(al[i]*3)
print(bl)
df = pd.DataFrame({'AALb':al, 'AALc':bl})
df.to_csv('AAL Results.csv')
#-------------------------------convert a dataframe column to a list 
import pandas as pd
# Create a sample DataFrame
df = pd.DataFrame({'col1': [1, 2, 3, 4],
                   'col2': ['A', 'B', 'C', 'D']})

# Convert column 'col1' to a list
col1_list = df['col1'].tolist()
print(col1_list)
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

# pandas
df_pd[(df_pd["cost"] > 750) & (df_pd["store"] == "Violet")]
# polars
df_pl.filter((pl.col("cost") > 750) & (pl.col("store") == "Violet"))
#-------------------------------filter rows like excel
#We can select the rows for product groups PG1, PG2, and PG3 as follows
# pandas
df_pd[df_pd["product_group"].isin(["PG1", "PG2", "PG5"])]

# polars
import polars as pl
df_pl.filter(pl.col("product_group").is_in(["PG1", "PG2", "PG5"]))

#These building types be in occutype column
building_type = ["RES1-1SNB", "RES1-2SNB", "RES1-2SNB", "RES1-1SWB", 
                            "RES1-2SNB", "RES1-2SWB", "RES1-3SNB", 
                            "RES1-3SWB", "RES1-SLNB", "RES1-SLWB"] 
    
df = df[df['occtype'].isin(building_type)] 
df.fd_id.count()
print(df["occtype"].unique())
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
print ("this is the fit", fit)
#-------------------------------print coefficents separatly
print (fit[0])
print (fit[1])
#-------------------------------put list data to csv file
import pandas as pd
list_name = ['item_1', 'item_2', 'item_3']
df = pd.DataFrame (list_name, columns = ['column_name'])
print(df)
df.to_csv('csv name.csv')
#-------------------------------dataframe row append per loop
import pandas as pd

input = pd.read_csv(r"C:\Users\ataghi2\OneDrive\0-TAMU\SHMP\Flood AAL Methodology\input.csv")

df = pd.DataFrame([])

for a in range (len(input['no'])):
    ...
    print('per AALb = ', pAALb)
    print('per AALc = ', pAALc)
    print('dol AALb = ', dAALb)
    print('dol AALc = ', dAALc)
    print('dol AALt = ', dAALt)
    dataf = pd.DataFrame({'ppAALb':[pAALb], 'ppAALc':[pAALc], 'ddAALb':[dAALb], 'ddAALc':[dAALc], 'ddAALt':[dAALt]})
    df = df.append(dataf)
    
print(df[:10])
df.to_csv('ResultsOfAAL.csv')
#-------------------------------if in for loop
print ("\nlimit flood depth data in their range from -2 to 16\n")
FD2 = [-8, -2, 0, 16, 30]
for i in range (len(FD)):
    if FD[i]<-2:
        FD[i]=-2
    elif FD[i]>16:
        FD[i]=16
    FD2.append (FD[i])
print("FD2 = ", FD2[:10])
#-------------------------------multiply a number to list
a = [1, 2, 5]
b = [i*0.5 for i in a]
#-------------------------------replace values in a column
import pandas as pd
df = pd.DataFrame({'A': [0, "nan", 3, 0, 4], 'B': [5, 6, 7, 8, 9], 'C': ['a', 'b', 'c', 'd', 'e']})
df
df["A"].replace([0, 4], 5, inplace=True)
df
#-------------------------------if and or
n_o_s = df["n_o_s"].values.tolist()
number_of_story = []
for i in range (len(n_o_s)):
    if n_o_s[i]==1:
        n_o_s[i]=1
    elif n_o_s[i]==2:
        n_o_s[i]=2
    elif n_o_s[i]==1.5:
        n_o_s[i]=1.5
    elif n_o_s[i]=="split_level" or n_o_s[i]=="split level":
        n_o_s[i]=1.5
    else: 
        n_o_s[i]=2
    number_of_story.append (n_o_s[i])
print("number_of_story = ", number_of_story)
#-------------------------------remove missing values
df = df.dropna(subset=['Age', 'Salary'])
df.dropna()
#-------------------------------replace missing values
values = {"Column A": 99999, "Column B": 888888, "Column C": 77777, "Column D": 66666}
df.fillna(value=values)
#-------------------------------add empty column
df.insert(10,"foundation", "no_basement")
df["Blank_Column"] = " "
df["NaN_Column"] = np.nan
df["None_Column"] = None
#-------------------------------convert dataframe to dictionary
import pandas as pd
df = pd.read_excel(r'C:\Users\arasht\OneDrive\0-TAMU\AAL Flood\test.xlsx', sheet_name='Sheet1')
df.to_dict()
df1 = pd.DataFrame({'A': {0: 1, 1: 4, 2: 1, 3: 4, 4: 7, 5: 10, 6: 10, 7: 11},
   'B': {0: 5, 1: 3, 2: 2, 3: 5, 4: 8, 5: 11, 6: 10, 7: 11},
   'C': {0: 3, 1: 1, 2: 3, 3: 6, 4: 9, 5: 12, 6: 11, 7: 11}})
#-------------------------------compare values in datafarme rows
df1 = pd.DataFrame({'A': {0: 1, 1: 4, 2: 1, 3: 4, 4: 7, 5: 10, 6: 10, 7: 11},
   'B': {0: 5, 1: 3, 2: 2, 3: 5, 4: 8, 5: 11, 6: 10, 7: 11},
   'C': {0: 3, 1: 1, 2: 3, 3: 6, 4: 9, 5: 12, 6: 11, 7: 11}})

for i in range (len(df["A"])):
    if df["A"].loc[df.index[i]]<df["B"].loc[df.index[i]]<df["C"].loc[df.index[i]]:
        pass
    else:
        df.at[i, "A"]=""
        df.at[i, "B"]=""
        df.at[i, "C"]=""
    
print(df)
#-------------------------------Write inside specefic column and rows
df.loc[1:5,"found_type"]="P"
df.loc[6:14,"found_type"]="I"

#-------------------------------decimat format
# %d means print without decimal  
print("%d" % 5.6434343434343)
# "%.2f" % a --> show a with 2 decimals
print("%.2f" % 5.3434343434343)

#-------------------------------chunk a large csv file to smaller csv files
import pandas as pd

# Define the chunk size for loading the dataframe
chunk_size = 100000  # Adjust this value based on your system's memory capacity

# Create a counter variable to keep track of the chunk number
chunk_counter = 1

# Iterate over the CSV file in chunks and process each chunk
for chunk in pd.read_csv('large_data.csv', chunksize=chunk_size):
    # Perform any necessary preprocessing or analysis on the chunk
    # For demonstration purposes, let's just print the summary statistics of each chunk
    print(chunk.describe())
    
    # Write the chunk to a separate CSV file
    chunk.to_csv(f'chunk_{chunk_counter}.csv', index=False)
    chunk_counter += 1
#-------------------------------move the first 100 rows to a new csv file
import pandas as pd

# Assuming df is your original DataFrame
# Create a new DataFrame with the first 100 rows
new_df = df.head(100)

# Save the new DataFrame to a CSV file
new_df.to_csv('first_100_rows.csv', index=False)
#-------------------------------groupby
grouped=df.groupby("recip_gender")
count_grouped = grouped.count()
print(count_grouped)

grouped2 = df.groupby(['age', 'Race_CD'])
result_df = grouped2.agg({'age': 'sum', 'Race_CD': 'count'})
result_df
#-------------------------------




