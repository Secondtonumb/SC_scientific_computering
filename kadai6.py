#coding=utf-8
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import argparse
import math

def trape(arr, n):
    h = 1 / n
    inter = (arr[0] + arr[n]) / 2
    for i in xrange(1, n - 1):
        inter += arr[i]
    inter = inter * h
    return inter

def simpson(arr, n):
    h = 1 / (2 * n)
    inter = arr[0] + 4 * arr[1] + arr[2 * n]
    for i in xrange(1, n - 1):
        inter += 2 * arr[2 * i] + 4 * arr[2 * i + 1]
    inter = inter * h / 3
    return inter

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("n", nargs='?', type=int)
    args = parser.parse_args()
    
    x1 = np.linspace(0, 1, args.n + 1)
    x2 = np.linspace(0, 1, 2 * args.n + 1)

    y1 = np.sqrt(1 - x1 ** 2)
    y2 = np.sqrt(1 - x2 ** 2)
    
    a = trape(y1, args.n)
    print ("台形公式の結果:%f        誤差:%f"%(a, np.pi / 4 - a ))

    b = simpson(y2, args.n)
    print ("シンプソン公式の結果:%f  誤差:%f"%(b, np.pi/ 4 - b))

if __name__ == "__main__":
    main()
