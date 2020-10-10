import sys
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

def main():
    if len(sys.argv) != 3:
        print("usage: python source.py <dataset.csv> <integer order>")
        quit()
    dataset = pd.read_csv(sys.argv[1], header=0, names=["X", "Y"])
    order = int(sys.argv[2])
    synth = dataset.to_numpy()
    X = dataset.iloc[:, 0]
    Y = dataset.iloc[:, 1]

    thetas = gradientDescent(X, Y, order)
    # print(sys.argv[1], "order =", sys.argv[2])
    mse(synth, thetas)
    plotline(synth, thetas)
    
def gradientDescent(X, Y, order):
    thetas = [0] * (order + 1)
    alpha = 0.00001
    iterations = 1500
    n = float(len(X))

    y_hat = 0
    for i in range(iterations):
        for j in range(len(thetas)):
            y_hat = y_hat + thetas[j] * pow(X, j)
            thetas[j] = thetas[j] - (alpha * ((-2/n) * sum(pow(X, j) * (Y - y_hat))))
    return thetas

def plotline(dataset, thetas):
    y = 0
    x = np.linspace(min(dataset[:, 0]), max(dataset[:, 0]), 100)
    for coord in dataset:
        plt.scatter(float(coord[0]), float(coord[1]), None, 'c')
    for order in range(len(thetas)):
        y = y + (thetas[order] * pow(x, order))
    plt.plot(x, y, 'r')
    plt.show()

def mse(synth, thetas):
    '''
    Mean squared error formula

    MSE = 1/n(SUM(i=1 -> n)[Y_i - Y^_i]^2)
    '''
    sum = 0
    for pair in synth:
        y = pair[1]
        y_hat = 0
        for theta in thetas:
            y_hat += theta * pow(pair[0], thetas.index(theta))
        sum += pow((y - y_hat), 2)
    print("mse =", 1/len(synth) * sum)
    # return (1/len(X)) * sum

if __name__ == '__main__':
    main()
