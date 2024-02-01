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
