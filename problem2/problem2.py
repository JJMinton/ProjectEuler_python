#!/usr/bin/env python3

"""problem2.py: solution to Project Euler Problem 2. 'projecteuler.net/problem=2'"""

___author___="Jeremy Minton"
___status___="Passed"

upperLimit = 4e6;
sum = 0;
first = 1;
second = 1;
while first<upperLimit or second<upperLimit:
    first += second;
    second = first-second;
    if first%2==0:
        sum+=first;
print('The sum of even terms in the fibbonaci sequence belew {:} is {:}'.format(upperLimit, sum));
