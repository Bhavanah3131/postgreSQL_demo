import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([10, 5, 4, 8, 0])
mylabels=['2024-1-1', '2024-4-27', '2024-7-31', '2024-9-21', '2024-4-4']
myexplode=[0.2, 0, 0, 0, 0]
mycolors=["Black", "hotpink", "Brown", "green"]

plt.pie(ypoints, labels=mylabels,explode=myexplode, shadow=True, colors=mycolors)
plt.legend(title="Car_sales")
plt.show()