## **Segmentation Fault with Tricontour**
https://github.com/matplotlib/matplotlib/issues/10167

### **Description:**

Given an array of data where its lower or upper triangular values are populated with NaNs, tricontour and tricontourf is unable to draw contour lines and results in a segmentation fault, which further prevents the plot from being displayed.

### **Reproducing the Bug (*as submitted by AndreiSavici*):**
```
import numpy as np
import matplotlib.pyplot as plt

x,y=np.meshgrid(np.arange(10),np.arange(10))
z=x**2.+y**2.
z[x<y]=np.nan
fig,ax=plt.subplots()
ax.tricontourf(x.ravel(),y.ravel(),z.ravel())
#ax.tripcolor(x.ravel(),y.ravel(),z.ravel(),vmax=100,vmin=0)
plt.show()
```

