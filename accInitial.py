from api import accT,seqT
import matplotlib.pyplot as plt
import numpy as np

def draw(size:int):
    axis=[i for i in range(size)]
    res=[0 for i in range(size)]
    for i in range(size):
        res[i]=accT(10)
    plt.plot(axis,res)
    plt.savefig('distribution of first run of ACC.png')

draw(100)