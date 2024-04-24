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

print("duration: ",end-start)

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
#-----------------------------------break
x=[]
for i in range (1,11):
    if i>4:
        break
    x.append(i)
    
print(x)
#-----------------------------------install package in Python
#in windows search type cmd or press window+R cmd
#type: pip install numpy
#pip uninstall numpy
#pip show numpy
#pip --version

#-----------------------------------install package in Anaconda
#search cmd select Anaconda Prompt
#search package name on internet and copy link into the prompt "conda open cv"
#conda install -c conda-forge opencv
#conda install -c anaconda natsort
#import natsort
#or in anaconda console type
#ln[]: !conda install -c conda-forge unicodedata2 --y
#--To show list of packages
!conda list
!conda env list
!conda update conda
!activate py35
!conda update PACKAGENAME
!conda creat --name ai37 python=3.7
!conda env list
!source activate ai37

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

#-----------------------------------put two pictures on eachother
import cv2
im1=cv2.imread(r"C:\Users\ataghi2\Desktop\R\Python\1.png")
im2=cv2.imread(r"C:\Users\ataghi2\Desktop\R\Python\2.png")
final_image=cv2.addWeighted(img1,0.8,img2,0.2,0)
cv2.imshow("Window",final_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#-----------------------------------Class and objects
class MyClass:
    x=5
    y=10

print(MyClass().y)
#----
class person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

print(person("arash", 40).name)
#----
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name} ({self.age})"

print(Person("John", 36))
#----
class Person:
    def __init__(self,name,age):
        self.name= name
        self.age= age

    def myfunc(self):
        print("hello I am " + self.name)

Person("Arash", 10).myfunc()

#-----------------------------------Class as a library
#file1: CreatClass.py
class Car:

    def __init__(self,make,model,year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("This "+self.model+" is driving")

    def stop(self):
        print("This "+self.model+" is stopped")

#file2: UseClass.py
from CreatClass import Car

car_1 = Car("Chevy","Corvette",2021,"blue")
car_2 = Car("Ford","Mustang",2022,"red")

car_1.drive()
car_2.stop()

print(car_1.year)
#---------------------------- Import csv file
df=pd.read_csv("C:/Users/ataghi2/Desktop/Data.csv")
#or
df=pd.read_csv(r"C:\Users\ataghi2\Desktop\Data.csv")
#---------------------------- Export csv file
df.to_csv((r"C:\Users\ataghi2\")
#---------------------------- Tests code up to a certine line
print (polygon)
exit()
#---------------------------- Make a library in Python to add 2 numbers

# simple_addition.py --> save in desk or python path
def add_numbers(a, b):
    """
    Function to add two numbers.

    Parameters:
    - a: The first number
    - b: The second number

    Returns:
    The sum of the two numbers
    """
    return a + b

# main_script.py
import simple_addition
result = simple_addition.add_numbers(3, 4)
print("The sum is:", result)

#or

from simple_addition import add_numbers
result = add_numbers(3, 4)
print("The sum is:", result)

#---------------------------- variable by f string
# I have shapefile variable I can change it to f"temperory_{shapefile}"
#---------------------------- try, except
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Error: Division by zero!")
else:
    print("Result:", result)  # This will not be executed because of the exception
finally:
    print("Cleanup code here")  # This will always be executed
#---------------------------- 
