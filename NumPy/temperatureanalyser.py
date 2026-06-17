import numpy as np

temp=np.array([32,35,40,45,36,34,42])

average=np.mean(temp)
hottest=np.max(temp)
coldest=np.min(temp)
aboveaverage=temp[temp>average]

print("average temperature:",average)
print("hottest  day : ",hottest)
print("coldest day : ",coldest)
print("above average : ",len(aboveaverage))