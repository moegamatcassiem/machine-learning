from matplotlib import pyplot as plt
import numpy as np


data = np.array([0.5, 0.7, 1., 1.2, 1.3, 2.1])
bins=[0, 1, 2, 3]

ax = plt.axes()
ax.set_facecolor("black")
plt.title("histogram:Histogram of nums against bins")
plt.xlabel("nums", fontweight="bold")
plt.ylabel("bins", fontweight="bold")
plt.hist(data, bins, color="black", edgecolor="orange")
plt.show()