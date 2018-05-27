from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import math

x0 = 0
y0 = 1
h = 0.1

result = np.zeros([10, 2])

x = x0
y = y0

for i in xrange(10):
    k1 = x + y
    k2 = x + (h / 2) + y + (h / 2) * k1
    k3 = x + (h / 2) + y + (h / 2) * k2
    k4 = x + h + y + h * k3
    fi = (k1 + 2 * k2 + 2 * k3 + k4) / 6
    print (k1, k2, k3, k4, fi)
    x = x + h
    y = y + h * fi
    result[i, 0] = x
    result[i, 1] = y
    print (x, y)

print result

x1 = range(0,1,10)
print x1
y1 = [(2 * 1 * math.exp(i) - 1 - i) for i in x1]

plt.plot(x1,y1, 'rx')
plt.plot(result[:,0], result[:,1], 'bo')
plt.show()
