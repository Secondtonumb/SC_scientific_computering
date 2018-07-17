# coding=utf-8
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import math
import argparse

def phi_i(x, arr, l, index):
    res = 0;
    if(index == 0):
        if(arr[0] <= x and x <= arr[1]):
            res = (arr[1] - x) / (arr[1] - arr[0])
        else:
            res = 0
    elif(index == l):
        if(arr[l - 1] <= x and x <= arr[l]):
            res = (x - arr[l]) / (arr[l] - arr[l - 1])
        else:
            res = 0
    else:
        
        if(arr[index - 1] <= x and x <= arr[index]):
            res = (x - arr[index - 1]) / (arr[index] - arr[index - 1])
        elif(arr[index] <= x and x <= arr[index + 1]):
            res = (arr[index + 1] - x) / (arr[index + 1] - arr[index])
        else:
            res = 0
    return res
    

def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-m_power", type=int, default=10)
    parser.add_argument("-samples", type=int, default=32)
    args = parser.parse_args()

    M = np.zeros(args.m_power) 

    for i in range(1, args.m_power):
        M[i] = 2 ** i 
    for n in range(1, args.m_power):
        m = int(M[n])
        samples = args.samples
        X = np.linspace(0, 1, samples + 1)
        res = np.zeros(samples + 1)
        exact = -0.5 * np.abs(X - 0.5) ** 2 + 1/ 8
        # print(exact)
        u = np.linspace(0, m, m + 1)

        A = np.zeros([m + 1, m + 1])
        A[0, 0] = 1
        A[m ,m] = 1
        for i in range(1, m):
            A[i, i] = 2;
            A[i - 1, i] = -1;
            A[i, i - 1] = -1;

        A[0, 1] = 0;
        A[1, 0] = 0;
        A[m - 1, m] = 0;
        A[m, m - 1] = 0;
        # print(A)
        b = (1 / m ** 2) * np.ones(m + 1)
        b[0] = 0
        b[m] = 0

        u = np.linalg.inv(A) @ b
        # print(u)

        phi = np.zeros(m + 1)
        mesh = np.linspace(0, 1, m + 1)

        for x in range(0, samples):
            for i in range(0, m):
                phi[i] = phi_i(X[x], mesh, m + 1, i)
                # print(phi)
            res[x] = phi @ u

            # print(res)

        SSD = np.sum((res - exact) ** 2)

        #        plt.subplot(args.m_power // 3, 3, n)

        plt.cla()
        plt.plot(X, res, 'x-',label='FEM')
        plt.plot(X, exact,'*-',label='Exact Solution')
        plt.legend()
        plt.title("m = %d"%(m))
        plt.text(0.35 , 0, "SSD = %e"%(SSD))
        plt.savefig("m = %d.png"%(m),dpi=200)
    # plt.show()

if __name__ == "__main__":
    main()
