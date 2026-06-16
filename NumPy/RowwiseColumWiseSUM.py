import numpy as np

arr=np.array([
    [1,2,3],
    [2,3,4],
    [4,5,6]
])

print("row Sum :")
print(np.sum(arr,axis=1))

print("colums sum: ")
print(np.sum(arr,axis=0))