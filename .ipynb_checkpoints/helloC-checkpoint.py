from ctypes import CDLL

lib=CDLL('./*.so')

seq=lib.seq_time
seq.argtypes=int
seq.restype=c_double
acc=lib.acc_time
acc.argtypes=int
acc.restype=c_double

res=seq(20)
print(float(res))