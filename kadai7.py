from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import math

stride = 500

x = np.linspace(0, 5, stride + 1)
y = np.zeros(stride + 1)
y_adms_3 = np.zeros(stride + 1)
y_adms_4 = np.zeros(stride + 1)


def f(x, y):
    f = np.sin(x) - y
    return f


def RK_method(xn, yn, h):
    k1 = f(xn, yn)
    k2 = f(xn + h / 2, yn + h * k1 / 2)
    k3 = f(xn + h / 2, yn + h * k2 / 2)
    k4 = f(xn + h, yn + h * k3)

    y_new = yn + (k1 + 2 * k2 + 2 * k3 + k4) / 6 * h

    return y_new


def Adams_3(x_arr, y_arr, h):
    '''
    x_arr = [xn, x(n-1), x(n-2)]
    y_arr = [yn, y(n-1), y(n-2)]
    '''
    f_arr = f(x_arr, y_arr)
    coef_corr_new = (h / 12) * np.array([23, -16, 5])
    y_corr_new = y_arr[0] + coef_corr_new.dot(f_arr)

    coef_new = (h / 12) * np.array([5, 8, -1])
    f_new = np.append(f(x_arr[0] + h, y_corr_new),
                      f_arr[0: 2])
    y_new = y_arr[0] + coef_new.dot(f_new)

    return y_new


def Adams_4(x_arr, y_arr, h):
    '''
    x_arr = [xn, x(n-1), x(n-2), x(n-3)]
    y_arr = [yn, y(n-1), y(n-2), x(n-3)]
    '''
    f_arr = f(x_arr, y_arr)
    coef_corr_new = (h / 24) * np.array([55, -59, 37, -9])
    y_corr_new = y_arr[0] + coef_corr_new.dot(f_arr)

    coef_new = (h / 24) * np.array([9, 19, -5, 1])
    f_new = np.append(f(x_arr[0] + h, y_corr_new),
                      f_arr[0: 3])
    y_new = y_arr[0] + coef_new.dot(f_new)

    return y_new


y[0] = 1
step = x[1]

for i in xrange(1, len(x)):
    y[i] = RK_method(x[i - 1], y[i - 1], step)

y_adms_3[0: 3] = y[0: 3]
y_adms_4[0: 4] = y[0: 4]

for i in xrange(2, len(x) - 1):
    x_array = np.array([x[i],
                        x[i - 1],
                        x[i - 2]])
    y_array = np.array([y_adms_3[i],
                        y_adms_3[i - 1],
                        y_adms_3[i - 2]])
    y_adms_3[i + 1] = Adams_3(x_array, y_array, step)

for i in xrange(3, len(x) - 1):
    x_array = np.array([x[i],
                        x[i - 1],
                        x[i - 2],
                        x[i - 3]])
    y_array = np.array([y_adms_4[i],
                        y_adms_4[i - 1],
                        y_adms_4[i - 2],
                        y_adms_4[i - 3]])
    y_adms_4[i + 1] = Adams_4(x_array, y_array, step)

plt.figure(figsize=(11.69,8.27))
plt.subplot(321)
plt.title("Plot by Runge-Kutta methods(step = 0.01)")
plt.plot(x, y, label="RB method")
plt.legend(fontsize=10)

plt.subplot(322)
plt.title("Plot by Runge-Kutta methods(step = 0.01)")
plt.plot(x, y, label="RB method")
plt.legend(fontsize=10)

plt.subplot(323)
plt.plot(x, y_adms_3,label="Adam methods(m = 3)", color='r')
plt.legend(fontsize=10)

plt.subplot(324)
plt.plot(x, y_adms_4,label="Adam methods(m = 4)", color='r')
plt.legend(fontsize=10)

plt.subplot(325)
plt.plot(x, y - y_adms_3,label="Error RB - Adams(3)",color='g')
plt.legend(fontsize=10)

plt.subplot(326)
plt.plot(x, y - y_adms_4,label="Error RB - Adams(4)",color='g')
plt.legend(fontsize=10)

plt.show()
