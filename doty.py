#!/usr/bin/python
# -*- coding: UTF-8 -*-

year = int(input('Input year: '))
month = int(input('Input month: '))
day = int(input('Input day: '))
total = 0
tries = 100
if year%4 == 0:
    days = 29
    yee = 'leap'
    if year%100 == 0:
        days = 28
        yee = 'common'
        if year%400 ==0:
            days = 29
            yee = 'leap'
        else:
            days = 28
            yee = 'common'
    else:
        days = 29
        yee = 'leap'
else:
    days = 28
    yee = 'common'
while tries > 0:
    if month > 12 or month < 1:
        print'Invaild input'
        month = int(input('Input month: '))
    elif month in (4,6,9,11) and day > 31 or day < 1:
        print'Invaild input'
        day = int(input('Input day: '))
    elif month in (1,3,5,7,8,10,12) and day > 32 or day < 1:
        print'Invaild input'
        day = int(input('Input day: '))
    elif month==2 and day>days:
        print'Invaild input'
        day = int(input('Input day: '))
    tries = tries - 1
print year, 'year is',yee,'Feb has', days, 'days'
if month <= 1:
    total = day
elif month == 2:
    total = 31 + day
elif month == 9 or month == 11:
    total = (month - 2) * 30 + days + month/2 + day + 1
else:
    total = (month - 2) * 30 + days + month/2 + day
print year, 'year',month, 'month', day, 'day is the', total, 'days'
