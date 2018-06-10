from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import math


def ln(samples_arr, x_index, X):
    coef_arr = np.delete(samples_arr, x_index)
    numerator = 1.0
    denominator = 1.0
    l = 1.0
    l_der = 1.0
    
    for i in xrange(len(coef_arr)):
        numerator = numerator * (X - coef_arr[i])
        denominator = denominator * (samples_arr[x_index] - coef_arr[i]) 
        
        l = l * (numerator / denominator)
        l_der = (l + (X - samples_arr[i + 1] * l_der))

    result = numerator / denominator

    return result


# def ln_1(samples_arr, x_index, X):
#     coef_arr = np.delete(samples_arr, x_index)
#     numerator = 1.0
#     denominator = 1.0
#     l = 1.0
#     l_der = 1.0
    
#     for i in xrange(len(coef_arr)):

#         l_der = ((l + (X - coef_arr[i]) * l_der)) / (samples_arr[x_index]) 
#         l = l * (X - coef_arr[i]) / (samples_arr[x_index] - coef_arr[i])

#         print(l, l_der)

# return l, l_der

    
ori_x = np.linspace(0, 1, 100)
ori_y = np.cos(ori_x * np.pi)

L_x = np.linspace(0, 1, 3)
ref = np.cos(L_x * np.pi)

n = len(L_x)

test_x = np.linspace(0, 1, 100)
l_mat = np.zeros([len(test_x), n])
l_der_mat = np.zeros([len(test_x), n])


for m in xrange(len(test_x)):
    for i in xrange(n):
        l_mat[m, i], l_der_mat[m, i] = ln_1(L_x, i, test_x[m])

print l_mat,l_der_mat

L_y = np.dot(ref ,l_mat.T)

print L_y

# n = 3


plt.plot(ori_x, ori_y)
plt.plot(test_x, L_y)
plt.show()
    
