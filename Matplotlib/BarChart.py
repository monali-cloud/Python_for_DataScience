import matplotlib.pyplot as plt

students=["A","B","C","D"]
marks=[80,65,90,75]

plt.bar(students,marks)
plt.xlabel("students")
plt.ylabel("marks")
plt.show()