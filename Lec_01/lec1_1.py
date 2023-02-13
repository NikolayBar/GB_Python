import numpy as np
import matplotlib.pyplot as plt


def task01():
    A = [1743, 1648, 1650, 1622, 1581, 1490]
    B = [743, 648, 711, 780, 805, 846]
    delta_A = [A[i+1]-A[i] for i in range(len(A)-1)]
    mean_A = sum(delta_A)/len(delta_A)

    delta_B = []
    mean_B = 0

    delta_B = [B[i+1]-B[i] for i in range(len(B)-1)]
    mean_B = sum(delta_B)/len(delta_B)

    for _ in range(10):
        A.append(A[-1]+mean_A)
        B.append(B[-1]+mean_B)
    # print(A)
    plt.plot(A)
    plt.plot(B)
    plt.show()

def task02():
    x = np.arange(0, 5, 0.1)
    y = np.sin(x)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    plt.show()

task02()
