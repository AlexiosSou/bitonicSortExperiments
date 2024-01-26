from ctypes import CDLL,c_int, c_double
import matplotlib.pyplot as plt
import numpy as np

lib=CDLL('./bitonic.so')

#results are in microseconds
seq=lib.seq_time
seq.argtypes=[c_int]
seq.restype=c_double
acc=lib.acc_time
acc.argtypes=[c_int]
acc.restype=c_double


#print(float(acc(20)))

def accT(n:int):
    return float(acc(n))/1000
def seqT(n:int):
    return float(seq(n))/1000

#discard the low bound
def draw(low:int,up:int, iteration:int)->None:
    axis=[i for i in range(low, up )]
    meanR=[0.0 for i in range(low, up )]
    upperBound=[0.0 for i in range(low, up )]
    lowerBound=[0.0 for i in range(low, up )]
    initialization=accT(10)
    for i in range(low, up ):
        samples=np.zeros(iteration)
        for j in range(iteration):
            samples[j]=seqT(i)/accT(i)
        mean=np.mean(samples)
        std=np.std(samples)
        meanR[i-low]=mean
        upperBound[i-low]=mean+3*std/np.sqrt(iteration)
        lowerBound[i-low]=mean-3*std/np.sqrt(iteration)

    plt.plot(axis,meanR,label='seq/acc',color='b')
    plt.fill_between(axis,lowerBound,upperBound,label='Asymptic 3-sigma confidence interval for ratio of executation time',color='g')
    plt.xlabel('log(size)')
    plt.title('Ratio of Executation time of Bitonic Sort')
    plt.legend()
    plt.savefig('ratio.png')
    
draw(10,28,1)