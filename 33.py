import numpy as np
x = np.array(['python is easy'], dtype =np.str)
print("Original Array:")
print(x)
r = np.char.join(" ", x)
print(r)