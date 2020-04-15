import numpy as np
#matplotlib is not a necessary library. Its just for visualising the line formed by linear regression
#Comment out the last piece of code if you dont have matplotlib
import matplotlib.pyplot as plt


#IGNORE this section of code. This is done to deal with file handling of inputs and outputs
inp = open("input.txt","r")
out = open("output.txt","r")
contentsOfX = inp.readlines()
contentsOfY = out.readlines()
assert(len(contentsOfX) == len(contentsOfY))
x = []
y = []
for i  in range(0,len(contentsOfX)):
    x.append(float(contentsOfX[i].split("\n")[0]))
    y.append(float(contentsOfY[i].split("\n")[0]))
x = np.array(x)
y = np.array(y)
inp.close()
out.close()

#CODE starts here!
#Some functions which are obvious and will use later


#to calculate the mean of array
def mean(var):
    sum = 0
    for i in range(0,len(var)):
        sum+=var[i]
    sum /= len(var)
    return sum

#to calculate the array     (p-mean(p))
def difference(var,mean):
    arr = []
    for i in range(0,len(var)):
        arr.append(var[i]-mean)
    return np.array(arr)

#to create an array with each element squared   (p**2)
def squared_newX(var):
    arr = []
    for i in range(0,len(var)):
        arr.append(var[i]**2)
    return np.array(arr)

def sum(arr):
    sum = 0
    for i in range(0,len(arr)):
        sum+=arr[i]
        
    return sum

#to create an array of product of two elements of different arrys at same index     (p*q)
def product(arr1,arr2):
    arr = []
    for i in range(0,len(arr1)):
        arr.append(arr1[i]*arr2[i])
    return np.array(arr)

meanX = mean(x)
meanY = mean(y)

newX = difference(x,meanX)
newY = difference(y,meanY)

squared_newX = squared_newX(newX)

regressionSlope = sum(product(newX,newY))/sum(squared_newX)
yIntercept = meanY - regressionSlope*meanX

print(yIntercept,"  ",regressionSlope)

#If you dont have matplotlib, comment out the code below
plottedY = []
for i in range(0,len(x)):
    plottedY.append(yIntercept + regressionSlope*x[i])
plottedY = np.array(plottedY)

plt.scatter(x,y)
plt.plot(x,plottedY)
plt.show()