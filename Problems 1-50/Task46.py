# -*- coding: utf-8 -*-
import math
primeList = []
oddComposite = []
works = []

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
  
for a in range(3,10000,2):
    if a not in primeList and a%2 ==1:
        oddComposite.append(a)

for a in range(0, len(oddComposite)):
    for b in range(1, int(math.sqrt(oddComposite[a]/2))+1):
        if oddComposite[a] - 2*(b**2) in primeList:
            works.append(oddComposite[a])
            break
    if oddComposite[a] not in works:
        print(oddComposite[a])
