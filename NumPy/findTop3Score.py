import numpy as np

scores=np.array([53,86,95,96,75,89,74])
sorted=np.sort(scores)
print("top 3 scores : ")
print(sorted[-3:])