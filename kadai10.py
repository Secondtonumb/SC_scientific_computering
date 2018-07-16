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
    parser.add_argument("n", nargs='?', type=int)
    args = parser.parse_args()

    n = args.n

    x = np.linspace(0, 1, n + 1)
    y = np.linspace(0, 1, n + 1)

    G = np.zeros((n - 1) ** 2)
    # 右辺の行列式の作成
    for i in range(n - 1):
        G[i] += 0
        G[(n-2) * (n-1) + i] += 0
        G[(n-1) * i] += 0
        G[(n-1) * i + (n-2)] = (1 / 4) * np.sin(np.pi * (y[i + 1]))
    #　係数行列式の作成
    Coef = np.eye((n - 1) ** 2)

    for j in range(n - 1):
        for k in range(1, n - 1):
            Coef[j * (n - 1) + k][j * (n - 1) + k - 1] = -1/4
            Coef[j * (n - 1) + k - 1][j * (n - 1) + k] = -1/4

    for j in range(1, n - 1):
        for k in range(n - 1):
            Coef[j * (n - 1) + k][(j - 1) * (n - 1) + k] = -1/4
            Coef[(j - 1) * (n - 1) + k][j * (n - 1) + k] = -1/4

    # X = A-1 * G
    res = np.linalg.inv(Coef).dot(G.T)
    res = res.reshape(n - 1, n - 1)
    res = block_diag(0.0, res, 0.0)
    # 境界条件を代入
    res[:, n] = np.sin(np.pi * y)
    print("n = %d 差分法の結果" % (n))
    print(res)

    Acc = np.zeros([(n + 1), (n + 1)])

    for i in range(1, n):
        for j in range(1, n):
            Acc[j, i] = u(x[i], y[j])
    # 境界条件を代入
    Acc[:, n] = np.sin(np.pi * y)
    print("n = %d 精確値" % (n))
    print(Acc)

    fig = plt.figure()
    ax = fig.add_subplot(1, 2, 1, projection='3d')
    x, y = np.meshgrid(x, y)

    plot1 = ax.plot_surface(x, y, res, label="差分法",
                            cmap="rainbow")
    fig.colorbar(plot1, shrink=0.5)
    ax.text2D(0.05, 0.95, "FDM", transform=ax.transAxes)

    ax = fig.add_subplot(1, 2, 2, projection='3d')
    plot2 = ax.plot_surface(x, y, Acc, label="精確値",
                            cmap="rainbow")
    fig.colorbar(plot2, shrink=0.5)

    ax.text2D(0.05, 0.95, "Exact Solution", transform=ax.transAxes)
    plt.show()

    plt.subplot(121)
    plt.title("FDM")
    plt.imshow(res,
               cmap="Blues",
               interpolation="nearest")

    plt.subplot(122)
    plt.title("Exact Solution")
    plt.imshow(Acc,
               cmap="Blues",
               interpolation="nearest")
    plt.show()


if __name__ == "__main__":
    main()
