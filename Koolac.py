#3D Plot
import matplotlib.pyplot as plt
x=[1,2,3]; y=[1,2,3]; z=[1,2,3]
plt.axes(projection="3d").scatter3D(x,y,z,color="blue",s=100)
plt.show()

#Function time
def f():
    for i in range(10**8):
        pass

from time import time
start=time()
f()
end=time()

print("duration: ",start-end)
