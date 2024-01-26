import matplotlib.pyplot as plt
import numpy as np

axis=[i for i in range(10)]
value=[2*i for i in range(10)]

plt.plot(axis,value)
plt.savefig('helloPlt.png')
