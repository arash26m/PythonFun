#-----------------------------------3D Plot
import matplotlib.pyplot as plt
x=[1,2,3]; y=[1,2,3]; z=[1,2,3]
plt.axes(projection="3d").scatter3D(x,y,z,color="blue",s=100)
plt.show()

#-----------------------------------Function time
def f():
    for i in range(10**8):
        pass

from time import time
start=time()
f()
end=time()

print("duration: ",start-end)

#-----------------------------------Bar Plot
from sklearn.datasets import load_iris
x,y=load_iris(return_X_y=True)

import matplotlib.pyplot as plt
plt.hist(x[:,0],ec="black",color="lightgray")
plt.show()

#-----------------------------------for loop
x=[]
for i in range (5):
    x.append(i**2)
    
print(x)    

#-----------------------------------install package
#in windows search type cmd or press window+R cmd
#type: pip install numpy
#pip uninstall numpy
#pip show numpy
#pip --version

#-----------------------------------k-means
#import iris data
from sklearn.datasets import load_iris
x,y=load_iris(return_X_y=True)
#import k-means from sklearn
from sklearn.cluster import KMeans
#define the model
model=KMeans(n_clusters=3,init="k-means++")
#fit the model
model.fit(x,y)
#print results
print(model.labels_)

#-----------------------------------
