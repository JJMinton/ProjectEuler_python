#!/usr/bin/env python3

"""problem1.py: solution to Project Euler Problem 1. 'projecteuler.net/problem=1'"""

___author___="Jeremy Minton"
___status___="Draft"

multiples = [3,5]
upperLimit = 1000;

numbers = set();
for multiple in multiples:
    numbers = numbers | set(i for i in range(0,upperLimit,multiple));
answer = sum(numbers);

print('The sum of the multiples of {:} below {:} is {:}'.format(multiples, upperLimit, answer))
    
