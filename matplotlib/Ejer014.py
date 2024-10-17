import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

xpoints2 = np.array([1, 2, 6, 8])
ypoints2 = np.array([5, 4, 5, 1])

font1 = {'family':'serif','color':'purple','size':30}
font2 = {'family':'serif','color':'red','size':15}

plt.title("Titulazo", fontdict = font1)
plt.xlabel("Horizontal", fontdict = font2)
plt.ylabel("Vertical", fontdict = font2)

plt.plot(xpoints, ypoints)
plt.plot(xpoints, ypoints, marker = 'o', ms = 20, mec = 'm', mfc = 'm', c = 'b', linewidth = '2.55')

plt.plot(xpoints2, ypoints2)
plt.plot(xpoints2, ypoints2, marker = '*', ms = 15, mec = 'r', mfc = 'r', c = 'g', linewidth = '2.55')

""""
#Graficos separados este seria el 1:

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 1, 1)
plt.plot(x,y)

#Este seria el 2:

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 1, 2)
plt.plot(x,y)
plt.title("INCOME")
plt.suptitle("MY SHOP")

"""

plt.grid(color = 'purple', linestyle = '--', linewidth = 0.5)
plt.show()
