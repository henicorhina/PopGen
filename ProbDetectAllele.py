#! /usr/bin/env python
"""
@author: henicorhina
"""


import math
import random
import matplotlib.pyplot as plt

# crap, this can be broken down to p = b^n

# Question 2

print "Lets calculate range of percent probability of detecting an allele"
print "using the equation: p = (n!/s!t!)(a^s)(b^t)"
print "given a = 0.05"

# in this case, we want to calculate the probability of detecting an allele
# this is equal to the 1 - the probability of not detecting, so when s = 0
# when s = 0, the equation becomes p = (b^t) and is independent of sample size (n)

n = []
a = 0.05
s = 0.0

listp = [] # blank list to add stuff to. probability of detection in this case.

for t in range(1,201): # a for loop for the entire formula above
	n = int(random.uniform(1,201))
	b = 1 - a
	t = (n - s)
	n1 = math.factorial(n)
	s1 = math.factorial(s)
	t1 = math.factorial(t)
	a1 = a ** s			
	b1 = b ** t
	st = s1 * t1
	ratio = n1 / st
	probability = ratio * a1 * b1
	oneminusprob = 1.0 - probability
	percentage = oneminusprob * 100.00
	listp.append(percentage)

listp.sort()
plt.plot(listp)
plt.xlabel("frequency")
plt.ylabel("probability of detection")
plt.show()
