#!/usr/bin/env python3

"""problem4.py: solution to Project Euler Problem 4. 'projecteuler.net/problem=4'

Find the largest palindrome made from the product of two 3-digit numbers.

This was completed using O(10^n) memory and O(10^2n) computations. This seems bad and there may be a better way to do it.
For elegance iterating through the products in order was implemented with an iterator.

"""

___author___="Jeremy Minton"
___status___="Finished"


import math

def checkPalendrome(inpMult):
    inpStr = str(inpMult[0]*inpMult[1]); 
    return inpStr==inpStr[::-1];

class multiples:
    def __init__(self, n):
        nmax = 10**n-1;
        nmin = 10**(n-1)
        self.vals = [n*(x+1) for x in range(nmin, nmax)];
        self.count = [n,]*(nmax-nmin);
        print(self.vals);
        
    def __iter__(self):
        return self;

    def __next__(self):
        val = max(self.vals);
        if val==0:
            raise StopIteration; 
        else:
            indx = self.vals.index(val);
            self.count[indx] -= 1;
            self.vals[indx] -= indx;
            return (indx, self.count[indx]+1);




nDigitNumbers = 3
for multple in multiples(nDigitNumbers):
    if checkPalendrome(multple):
        break;

print("Largest palendrome prodcut of two n={:} digit numbers is {:}".format(nDigitNumbers, multple[0]*multple[1]));







