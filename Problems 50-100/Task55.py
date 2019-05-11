# -*- coding: utf-8 -*-
import time
start = time.time()
def palindrome(num):
    for a in range(0,int(len(num)/2)):
        if num[a] != num[len(num)-(a+1)]:
            return False
    return True

def reverse(num):
    number = ""
    for a in range(0,len(num)):
        number = number + num[len(num)-(a+1)]
    return int(number)



def lychrel(num):
    for b in range(0,50):
        number = num + reverse(str(num))
        if palindrome(str(number)) == True:
            return True
        else:
            num = number
    return False

works = 0
for a in range(0,10000):
    if lychrel(a) == False:
        works = works + 1
print(works)
print(time.time() - start)