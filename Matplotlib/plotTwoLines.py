import matplotlib.pyplot as plt

x=[1,2,3,4]

plt.plot(x,[2,4,6,8], label="line 1")
plt.plot(x,[1,3,5,7],label="line 2")

plt.legend()
plt.show()