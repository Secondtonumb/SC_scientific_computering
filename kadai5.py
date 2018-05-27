from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import math


def ln(x_arr, x_index, X):
    coef_arr = np.delete(x_arr, x_index)
    print coef_arr
    numerator = 1.0
    denominator = 1.0
    
    for i in xrange(len(coef_arr)):
        numerator = numerator * (X - coef_arr[i])
        denominator = denominator * (x_arr[x_index] - coef_arr[i]) 
        print(numerator, denominator)

    result = numerator / denominator

    print(result)
    return result

        
ori_x = np.arange(0, 1, 0.01)
ori_y = np.cos(ori_x * np.pi)

n = 3


L_x = np.array([0, 0.5, 1], dtype = float)
ref = np.cos(L_x)

L_y = np.zeros(n)

l_vec = np.zeros(n)

for i in xrange(n):
    print ("this is l_vec's %dth element\n"%(i))
    l_vec[i] = ln(L_x, i, 1/4) 




# n = 3


plt.plot(ori_x, ori_y)
plt.show()
    
