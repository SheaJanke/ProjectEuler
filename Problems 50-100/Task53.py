# -*- coding: utf-8 -*-
import time
start = time.time()
def factorial(num):
    total = 1
    for a in range(0,num):
        total = total*(a+1)
    return total

def comb (num1,num2):
    return factorial(num1)/(factorial(num2)*factorial(num1-num2))
count = 0
for n in range(1,101):
    for r in range(0,n):
        if(comb(n,r) > 1000000):
            count = count+1
print(count)


print(time.time()-start)