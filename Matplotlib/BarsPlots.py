import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Victor", "Joel", "Juan", "Francisco"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color = 'purple', width = 0.5)
plt.show()