
import numpy as np
import matplotlib.pyplot as plt


x = np.arange(1, 11)
y = x * x


plt.title("Line graph")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.plot(x, y, color ="red")
plt.show()
