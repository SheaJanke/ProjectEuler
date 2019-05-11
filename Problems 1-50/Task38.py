# -*- coding: utf-8 -*-

def pandigital (number, times):
    digits = ["1","2","3","4","5","6","7","8","9"]
    pan = ""
    global largest
    for a in range(1,times+1):
        num = str(number * a)
        pan+=num
        for b in range(0,len(num)):
            if num[b] in digits:
                digits.remove(num[b])
            else:
                return
    if len(digits) == 0:
        if int(pan) > largest:
            largest = int(pan)
            
largest = 0
for a in range(1000,10000):
    pandigital(a,2)
for a in range(100,1000):
    pandigital(a,3)
for a in range(10,100):
    pandigital(a,4)
for a in range(1,10):
    pandigital(a,5)
print(largest)