# -*- coding: utf-8 -*-
number = ""
num = 1
while len(number) < 1000000:
    number += str(num)
    num = num+1
total = int(number[0]) * int(number[9]) * int(number[99]) * int(number[999]) * int(number[9999])* int(number[99999]) * int(number[999999])
print(total)