# -*- coding: utf-8 -*-
import time
startTime = time.time()
primeList = []
factors = []

def getPrimes(max):
    primes = []
    for a in range(2,max+1):
        primes.append(True)
    for a in range(0,int(max/2)):
        if primes[a] == True:
            for b in range (2*a + 2, max-1,a+2):
                primes[b] = False
    for a in range(2,max+1):
        if primes[a-2] == True:
            primeList.append(a)
    
getPrimes(10000)

for a in primeList:
    powers = []
    b = 1
    while a**b < 100000:
        powers.append(a**b)
        b += 1
    factors.append(powers)
    
for a in factors:
    for b in a:
        for c in factors:
            for d in c:
                for e in factors:
                    for f 

print(time.time() - startTime)