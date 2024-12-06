import matplotlib.pyplot as plt
import numpy as np

xpoints=np.array(['2024-1-1', '2024-4-27', '2024-7-31', '2024-9-21', '2024-4-4'])
ypoints = np.array([10, 5, 4, 8, 0])
colors=np.array([0, 25, 50, 75, 100])
sizes=np.array([90, 75, 45, 34, 20])

plt.scatter(xpoints, ypoints, c=colors, cmap='nipy_spectral', s=sizes, alpha=0.5)
plt.colorbar()
plt.show()