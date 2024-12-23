#-----------------------------------Python Libraries
pypi.org
#-----------------------------------Deploy Python Program on Cloud with url
repl.it
#to share with others change url
#replace #main.py with  ?embed=1
#generate url from pdf result
filestack python pakage and API

#get free API from filestack
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
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
x.r, x.i # ==> (3.0, -4.5)
#----
class MyClass:
    """A simple example class"""
    i = 12345
    j = 567

    def f(self):
        return 'hello world'

MyClass().j   # ==> 567
MyClass().__doc__     # ==> 'A simple example class'

x = MyClass()
x.i = 1234
x.f()                 # => 'hello world'

#----
class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

print(Person("arash", 40).name)
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
#-----------------------------------Class & Statisticmethod
#when we want to call a function inside class independently
class Person:
    def __init__(self, age):
        self.age = age

    @staticmethod
    def is_adult(age):
        return age >= 21

age = 24
is_adult = Person.is_adult(age)
#-----------------------------------Class & classmethod
#in class method we can define new variables insde the class
from datetime import date

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    # a class method to create a Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)
 
    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18
 
person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)
 
print(person1.age)
print(person2.age)
 
# print the result
print(Person.isAdult(22))

#-----------------------------------Class & dataclass
from dataclasses import dataclass
from typing import Any #any data type

@dataclass
class Exercise:
   name: str
   reps: int
   sets: int
   weight: float  # Weight in lbs
    note: Any

ex1 = Exercise("Bench press", 10, 3, 52.5, NA)
ex1.name
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
#---------------------------- Dictionary
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(thisdict["brand"])
--
import ETL_Tools.dictionary as dic
print(dic.all_vax_views["RSV"], dic.all_vax_views["HPV"])
print(len(dic.all_vax_views))
print(dic.all_vax_views)
print(f"I like to see {dic.all_vax_views['most_recent_vax']}")
#---------------------------- Make dictionary using function 
def my_function(**kwargs):
    print(kwargs)

my_function(doghtur=1, son=2, age=3, name="arash") 

# output {'doghtur': 1, 'son': 2, 'age': 3, 'name': 'arash'}

#---------------------------- Make a  ( , , , ) using function
def my_function(*args):
    print(args)

my_function(1, 2, 3)  # Output: (1, 2, 3)
#---------------------------- how to use *
def add (a,b):
  return a+b

s = [4,5]

add(*s) # --> 9
------
def greet(*names):
    for name in names:
        print (f"hello {name}")

greet("ali", "hassan", "hossein")
hello ali
hello hassan
hello hossein
#---------------------------- namedtuple
from collections import namedtuple
HPVCounts = namedtuple("HPVCounts", ["female", "male", "unknown", "nonbinary"])
example_counts = HPVCounts(female=150, male=100, unknown=20, nonbinary=5)
print(example_counts.female)      # Outputs: 150
#---------------------------- 



