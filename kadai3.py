from __future__ import division

x = 2
for i in range(0,10):
    x = (x ** 2 + 1) / (x * 2 - 1)
    print("Iteration %d %0.50f" %(i + 1,x))
    
