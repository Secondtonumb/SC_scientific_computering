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




L_x = np.arange(0, 1, 1/3)
ref = np.cos(L_x * np.pi)

n = len(L_x)

test_x = np.arange(0.05, 1, 0.02)
l_mat = np.zeros([len(test_x), n])

for m in xrange(len(test_x)):
    for i in xrange(n):
        print ("this is l_vec's %dth element\n"%(i))
        l_mat[m, i] = ln(L_x, i, test_x[m])

print l_mat

L_y = np.dot(ref ,l_mat.T)

print L_y



# n = 3


plt.plot(ori_x, ori_y)
plt.plot(test_x, L_y)
plt.show()
    
