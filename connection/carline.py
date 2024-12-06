import matplotlib.pyplot as plt
import numpy as np

xpoints=np.array(['2024-1-1', '2024-4-27', '2024-7-31', '2024-9-21', '2024-4-4'])
ypoints = np.array([10, 5, 4, 8, 0])

font1={'family':'serif', 'color':'blue', 'size':20}
font2={'family':'serif', 'color':'darkred', 'size':15}

#plot1
plt.subplot(2,1,1)
plt.plot(xpoints, ypoints, marker='o', linestyle='dotted', color='r')
plt.title("car-sales", fontdict=font1)
plt.xlabel("purchase_date", fontdict=font2)
plt.ylabel("quantity", fontdict=font2)

#plot2
x=np.array([0,1,2,3])
y=np.array([10,20,30,40])

plt.subplot(2,1,2)
plt.plot(x,y)
plt.suptitle("Random")
plt.grid()
plt.show()

