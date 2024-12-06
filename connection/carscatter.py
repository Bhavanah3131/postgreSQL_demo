import matplotlib.pyplot as plt
import numpy as np

#day1
xpoints=np.array(['2024-1-1', '2024-4-27', '2024-7-31', '2024-9-21', '2024-4-4'])
ypoints = np.array([10, 5, 4, 8, 0])
plt.scatter(xpoints, ypoints)

#day2
x=np.array([2,2,8,1,15,17,9,8,7,5])
y=np.array([100,105,84,105,90,99,90,95,94,100])
plt.scatter(x, y)
plt.show()