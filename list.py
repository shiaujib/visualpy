
import numpy as np

a=np.random.randint(80,100,size=15)
print a
a[:-5]=a[5:]
print a
