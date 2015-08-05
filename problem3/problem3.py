#!/usr/bin/env python3

"""problem3.py: solution to Project Euler Problem 3. 'projecteuler.net/problem=3'

What is the largest prime factor of the number 600851475143?"""

___author___="Jeremy Minton"
___status___="Passed"

largestPrimeFactor = 1;
factorTrial=2;
#number=13195;
number = 600851475143;
while factorTrial<=number:
    if number%factorTrial == 0:
        largestPrimeFactor = factorTrial;
        number = number/factorTrial;
        print(largestPrimeFactor);
    else:
        factorTrial += 1
