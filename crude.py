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

def draw(size:int)->None:
    axis=[i for i in range(10, size )]
    accT=[0.0 for i in range(10, size )]
    seqT=[0.0 for i in range(10, size )]

    for i in range(10, size ):
        accT[i-10]=float(acc(i))/1000
    for i in range(10, size ):
        seqT[i-10]=float(seq(i))/1000

    plt.plot(axis,accT,label='openACC')
    plt.plot(axis,seqT,label='sequential')
    plt.xlabel('log(size)')
    plt.ylabel('time/ms')
    plt.title('Executation time of Bitonic Sort')
    plt.legend()
    plt.savefig('Stage1.png')
    
draw(25)