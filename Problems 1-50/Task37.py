import time
seconds = time.time()
primeList = []
trunkablePrimes= []


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
 
def trunkable(number):
        go = 0
        num = number
        while num > 10:
            num = int(num/10)
            if num not in primeList:
                go = 1
                return
        num = number
        if go == 0:
            while num > 10:
                string = str(num)
                string = string[1:len(string)]
                num = int(string)
                if num not in primeList:
                    go = 1
                    return
        if go == 0:
            trunkablePrimes.append(number)
      
getPrimes(100000)
print(time.time() - seconds)
for a in primeList:
    trunkable(a)
print(trunkablePrimes)
print(time.time()-seconds)



