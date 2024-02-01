from api import accT,seqT
import matplotlib.pyplot as plt
import numpy as np

#discard the low bound
def draw(low:int,up:int, iteration:int)->None:
    axis=[i for i in range(low, up )]
    accTMean=[0.0 for i in range(low-1, up )]
    accTUB=[0.0 for i in range(low-1, up )]
    accTLB=[0.0 for i in range(low-1, up )]
    seqTMean=[0.0 for i in range(low, up )]
    seqTUB=[0.0 for i in range(low, up )]
    seqTLB=[0.0 for i in range(low, up )]

    for i in range(low-1, up ):
        samples=np.zeros(iteration)
        for j in range(iteration):
            samples[j]=accT(i)
        mean=np.mean(samples)
        std=np.std(samples)
        accTMean[i-low+1]=mean
        accTUB[i-low+1]=mean+3*std/np.sqrt(iteration)
        accTLB[i-low+1]=mean-3*std/np.sqrt(iteration)
    for i in range(low, up ):
        samples=np.zeros(iteration)
        for j in range(iteration):
            samples[j]=seqT(i)
        mean=np.mean(samples)
        std=np.std(samples)
        seqTMean[i-low]=mean
        seqTUB[i-low]=mean+3*std/np.sqrt(iteration)
        seqTLB[i-low]=mean-3*std/np.sqrt(iteration)

    plt.plot(axis,accTMean[1:],label='openACC',color='b')
    plt.fill_between(axis,accTLB[1:],accTUB[1:],label='Asymptic 3-sigma confidence interval for openACC',color='g')
    plt.plot(axis,seqTMean,label='sequential',color='r')
    plt.fill_between(axis,seqTLB,seqTUB,label='Asymptic 3-sigma confidence interval for sequential',color='y')
    plt.xlabel('log(size)')
    plt.ylabel('time/ms')
    plt.title('Executation time of Bitonic Sort')
    plt.legend()
    plt.savefig('Stage2.png')
    
draw(10,23,100)