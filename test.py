from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import math

n = 3
x_axis = np.linspace(0, 1, n)
f = np.cos(x_axis * np.pi)
f_deriv = -np.sin(x_axis * np.pi)


def lag(samples, temp_index):
    n = len(samples)
    temp_samples = np.delete(samples, temp_index)

    sub_arr = samples[temp_index] * np.ones(n - 1) - temp_samples

    de = 1
    for i in sub_arr:
        de *= i
    result_poly = np.poly(temp_samples) / de
    print result_poly
    return result_poly


li = np.zeros([n, n])
li_deriv_xk = np.zeros(n)

ui = np.zeros([n, 2 * n])
vi = np.zeros([n, 2 * n])

for i in xrange(n):
    li[i, :] = lag(x_axis, i)
    temp_P = np.poly1d(li[i, :])
    temp_P_2 = (temp_P * temp_P)

    print temp_P_2
    temp_P_deriv = temp_P.deriv(1)
    li_deriv_xk[i] = temp_P_deriv(x_axis[i])
    
    addu_P = np.poly1d(
        [-2 * li_deriv_xk[i], 1 + 2 * li_deriv_xk[i] * x_axis[i]])
    addv_P = np.poly1d([1, -x_axis[i]])
    
    print addu_P
    print addv_P

    Ui = addu_P * temp_P_2
    Vi = addv_P * temp_P_2
    print Ui
    
    if (len(np.array(addu_P)) < 2):
        ui[i, :] = np.append(0, np.array(Ui))
    else:
        ui[i, :] = np.array(Ui)
        vi[i, :] = np.array(Vi)


print li_deriv_xk


L = np.dot(f, li)

L_P = np.poly1d(L)

print "result of L"
print L_P

U = np.dot(f, ui)
V = np.dot(f_deriv, vi)

H_P = np.poly1d(U + V)

print "result of H"
print H_P


x = np.linspace(0, 1, 100)

y = np.cos(x * np.pi)
y_La = L_P(x)
y_La2 = L_P(x) * L_P(x)
y_H = H_P(x)

plt.plot(x, y)
plt.plot(x, y_La)
plt.plot(x, y_H)
plt.show()
