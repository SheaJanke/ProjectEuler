# -*- coding: utf-8 -*-

answers = []
def pandigital(num1, num2):
    digits = ["1","2","3","4","5","6","7","8","9"]
    number1 = str(num1)
    number2 = str(num2)
    for a in range(0,len(number1)):
        if number1[a] in digits:
            digits.remove(number1[a])
        else:
            return
    for a in range(0,len(number2)):
        if number2[a] in digits:
            digits.remove(number2[a])
        else:
            return
    number3 = str(num1*num2)
    for a in range(0,len(number3)):
        if number3[a] in digits:
            digits.remove(number3[a])
        else:
            return    
    if len(digits) == 0:
        if num1*num2 not in answers:
            answers.append(num1*num2)
   
for a in range(1,1000):
    for b in range(1,10000):
        pandigital(a,b)
total = 0        
for a in answers:
    total +=a
print(total)