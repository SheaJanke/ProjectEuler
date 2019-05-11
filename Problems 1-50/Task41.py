# -*- coding: utf-8 -*-
primeList = []
largest = 0
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

def pandigital(num):
    global largest
    number = str(num)
    digits = []
    for a in range(0,len(number)):
        digits.append(str(a+1))
    for a in range(0,len(number)):
        if number[a] in digits:
            digits.remove(number[a])
        else:
            return
    if len(digits) == 0:
        largest = num

getPrimes(10000000)
for a in primeList:
    pandigital(a)
print(largest)
            