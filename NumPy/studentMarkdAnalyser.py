import numpy as np

marks=np.array([87,86,75,96,65,74,85,76,73,79])

highest=np.max(marks)
lowest=np.min(marks)
average=np.mean(marks)

aboveAverage=marks[marks>average]

print("highest marks:",highest)
print("lowest marks:",lowest)
print("average marks:",average)
print("above average marks:",len(aboveAverage))

