from api import accT,seqT
import matplotlib.pyplot as plt
import numpy as np

#discard the low bound
def draw(low:int,up:int, iteration:int)->None:
    axis=[i for i in range(low, up )]
    accTMean=[0.0 for i in range(low-1, up )]
    accTUB=[0.0 for i in range(low-1, up )]
    accTLB=[0.0 for i in range(low-1, up )]

    for i in range(low-1, up ):
        samples=np.zeros(iteration)
        for j in range(iteration):
            samples[j]=accT(i)
        mean=np.mean(samples)
        std=np.std(samples)
        accTMean[i-low+1]=mean
        accTUB[i-low+1]=mean+3*std/np.sqrt(iteration)
        accTLB[i-low+1]=mean-3*std/np.sqrt(iteration)
        
    plt.plot(axis,accTMean[1:],label='openACC',color='b')
    plt.fill_between(axis,accTLB[1:],accTUB[1:],label='Asymptic 3-sigma confidence interval for openACC',color='g')
    plt.xlabel('log(size)')
    plt.ylabel('time/ms')
    plt.title('Executation time of Bitonic Sort')
    plt.legend()
    plt.savefig('complexityACC.png')
    
draw(10,23,100)