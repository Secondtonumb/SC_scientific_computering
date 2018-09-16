# coding=utf-8
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import math
import argparse
from scipy.linalg import block_diag
from mpl_toolkits.mplot3d import Axes3D

# Define Function u

def u(x, y):
    res = (np.sinh(np.pi * x) / np.sinh(np.pi)) * np.sin(np.pi * y)
    return res


def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", type=int)
    parser.add_argument("-x", type=float, default=0.5)
    args = parser.parse_args()

    m = args.n
    x = args.x
    
    coef = np.zeros(m);
    for i in np.linspace(1, m, m):
        index =  int(i - 1)
        coef[index] = i ** 2 * np.pi ** 2 / 2         

    A = np.diag(coef)
    # print(A)

    b = np.zeros(m)
    for i in np.linspace(1, m, m):
        index =  int(i - 1)
        b[index] = (1 - np.cos(i * np.pi)) / (i * np.pi)

    a_res = np.linalg.inv(A) @ b
    
    phi = np.zeros(m)
    for i in np.linspace(1, m, m):
        index = int(i - 1)
        temp = i * np.pi * x
        phi[index] = np.sin(temp)

    res = 0 + a_res @ phi
    print("m = %d : %lf"%(m, res))

if __name__ == "__main__":
    main()
