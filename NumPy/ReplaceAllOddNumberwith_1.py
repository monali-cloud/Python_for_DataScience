import numpy  as np

numbers=np.array([23,45,67,75,25,55,68,76,59])

numbers[numbers%2!=0]=-1

print(numbers)