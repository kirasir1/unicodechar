from random import *
from math import *

def factor(N):
    L = []
    for d in range(2, int(sqrt(N))):
        if N % d == 0:
            L.append(d)
            N = N//d
    if N>1:
        L.append(N)
    return L

def primenum(r0):
    r1 = r0 * 10
    N = 2
    prime = []
    while N > 0:
        r = randint(r0, r1)
        L = factor(r)
        if len(L) == 1:
            prime.append(r)
            N = N - 1
    return prime