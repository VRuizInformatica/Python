import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
mycolors = ["purple", "pink", "b", "orange"]

plt.pie(y, labels=mylabels, colors=mycolors, startangle=90, shadow=True, explode=(0, 0, 0.2, 0), autopct='%1.1f%%')
plt.legend(title="Four Fruits:", loc="upper right")
plt.show()