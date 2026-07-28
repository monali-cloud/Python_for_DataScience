import matplotlib.pyplot as plt

months=["jan","feb","mar","apr"]

sales=[10,20,30,40]
plt.bar(months,sales)
plt.xticks(rotation=45)
plt.show()