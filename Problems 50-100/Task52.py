# -*- coding: utf-8 -*-
import time
start = time.time()
def sameDigits(num1,num2):
    nums = []
    nums2 = []
    for a in num1:
        nums.append(a)
    for a in num2:
        nums2.append(a)
    nums.sort()
    nums2.sort()
    if(nums == nums2):
        return True
    else:
        return False
    
a = 1
while a < 1000000:
    number = int("1" + str(a))
    if sameDigits(str(number), str(2*number)):
        if sameDigits(str(number), str(3*number)):
           if sameDigits(str(number), str(4*number)):
               if sameDigits(str(number), str(5*number)):
                   if sameDigits(str(number), str(6*number)):
                        print(number)
                        break
    a = a+1
print(time.time() - start)