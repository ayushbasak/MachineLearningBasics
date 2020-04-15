#File Handling
inp = open("input.txt","r")
out = open("output.txt","w")
contentsOfX = inp.readlines()
x = []
y = []
for i  in range(0,len(contentsOfX)):
    x.append(float(contentsOfX[i].split("\n")[0]))


#CODE begins here!
import random

#set the factor to anything you want
factor = 0.812

for i in range(0,len(contentsOfX)):
    y.append(round(x[i]*factor + 0.1*random.uniform(-1,1),5))
    out.writelines(str(y[i])+"\n")


inp.close()
out.close()