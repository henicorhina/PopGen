#! /usr/bin/env python
"""
@author: henicorhina
"""

import math
import random
import numpy
import matplotlib.pyplot as plt

# Question 3

print "Lets calculate range the sample size needed to detect an allele at a frequency of 5% in a population."
print "using the equation: p = (n!/s!t!)(a^s)(b^t)"

# in this case, we want to calculate the probability of detecting an allele
# this is equal to the 1 - the probability of not detecting, so when s = 0
# when s = 0, the equation becomes p = (b^t) and is independent of sample size (n)

n = []
a = 0.05
s = 0.0

listp = [] # blank list to add stuff to.


# The formula. The bulk of this program.
for o in range(0,500): # a for loop for the entire formula 
	n = o + 1
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
	listp.append(probability) # append the probability of detection to the list "listp"

# create and sort a list of 500 numbers. This is the proxy for sample sizes. 
kList = []
for g in range(0,500):
	kList.append(g + 1.0)
kList.sort() 

newList2 = []

# taking the 95% value of the list of probabilities.
listp.sort()
newList = listp[int(len(listp) * 0.0) : int(len(listp) * 0.95)]
d = max(newList) # this is the 95% value

# next set of lists
newList2 = kList[int(len(kList) * 0.0) : int(len(kList) * d)] # This takes the 95% value of the sample size.
h = max(newList2)

plt.plot(newList2)
plt.ylabel("frequency")
plt.xlabel("probability of detection")
plt.show()
