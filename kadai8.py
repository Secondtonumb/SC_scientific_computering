from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import math


def Jacobi(x, D, L, U, b):
    D_inv = np.linalg.inv(D)
    res = -D_inv.dot(L + U).dot(x) + D_inv.dot(b)
    return res


def SOR(x, D, L, U, b, omega):
    DL_inv = np.linalg.inv(D + omega * L)
    res = DL_inv.dot(((1 - omega) * D - omega * U)).dot(x) + omega * np.dot(DL_inv, b)
    return res

def Err(a, b):
    err = (1 / len(a)) * np.sum(np.power(a - b, 2))
    return err

A = np.zeros([10, 10])

A[0, 0] = 4

for i in xrange(1, 10):
    A[i, i] = 4
    A[i, i - 1] = -2
    A[i - 1, i] = -1

Diag = np.diag(np.diag(A))

Triu = np.triu(A, 1)

Tril = np.tril(A, -1)

b = np.array([2, 4, -3, 0, -1, 4, -3, -1, 4, -2]).T

x_init = np.ones(10)


Acc = np.linalg.inv(A).dot(b)
print("Accuracy Root")

print Acc
# Jacobi Method
J_conv = []
J_result = x_init

old = np.zeros(10)

while np.linalg.norm(old - J_result) > 1e-9:
    J_conv = np.append(J_conv,  np.linalg.norm(old - J_result))
    old = J_result
    J_result = Jacobi(J_result, Diag, Tril, Triu, b)
    # print J_result
# print J_conv
print("Jacobi Method Result")
print J_result
# Gauss-Seidel Method

GS_conv = []
GS_result = x_init
old = np.zeros(10)

while np.linalg.norm(old - GS_result) > 1e-9:
    GS_conv = np.append(GS_conv, np.linalg.norm(old - GS_result))
    old = GS_result
    GS_result = SOR(GS_result, Diag, Tril, Triu, b, 1)
    # print GS_result
# print GS_conv
print("GS Method result")
print(GS_result)
# SOR Method

Relax_Corr = 1.2
SOR_conv = []
SOR_result = x_init
old = np.zeros(10)

while np.linalg.norm(old - SOR_result) > 1e-9:
    SOR_conv = np.append(SOR_conv,  np.linalg.norm(old - SOR_result))
    old = SOR_result
    SOR_result = SOR(SOR_result, Diag, Tril, Triu, b, Relax_Corr)
    # print SOR_result
# print SOR_conv
print("SOR Method result")
print(SOR_result)

plt.ylabel("log(Norm)")
plt.plot(xrange(len(J_conv)), np.log(J_conv), 'r.',label = "Jacobi Method")
plt.plot(xrange(len(GS_conv)), np.log(GS_conv), 'g.', label = "Gauss Seidel Method")
plt.plot(xrange(len(SOR_conv)), np.log(SOR_conv), 'b.', label = "SOR Method (omega = 1.2) ")
plt.legend(fontsize = 10)

plt.show()
