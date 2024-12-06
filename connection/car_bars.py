import matplotlib.pyplot as plt
import numpy as np

xpoints=np.array(['2024-1-1', '2024-4-27', '2024-7-31', '2024-9-21', '2024-4-4'])
ypoints = np.array([10, 5, 4, 8, 0])

plt.bar(xpoints, ypoints, width=0.5)
plt.show()