'''
f = w0x0 + w1x1
g = sig(f)
'''

import numpy as np
import math

num_samples = 10000 #10,000
x0 = np.random.uniform(0, 1, num_samples)
x1 = np.random.uniform(0, 1, num_samples)
x2 = np.random.uniform(0, 1, num_samples)
y = np.empty_like(x0)

def Init():
    w0, w1, w2 = 1, 2, 3
    for i in range(num_samples):
        y[i] = w0*x0[i] + w1*x1[i]

class Tensor:
    def __init__(self, val):
        self.val = val
    def forward(self):
        return self.val
    def backward(self, val, lrate):
        print val

class Weight:
    def __init__(self, val):
        self.val = val
    def forward(self):
        return self.val
    def backward(self, val, lrate):
        self.val = self.val - lrate * val.sum()

class Mul:
    def __init__(self, w, x):
        self.w = w
        self.x = x
    def forward(self):
        self.wval = self.w.forward()
        self.xval = self.x.forward()
        return self.wval * self.xval
    def backward(self, val, lrate):
        self.w.backward(self.xval * val, lrate)
        self.x.backward(self.wval * val, lrate)

class Add:
    def __init__(self, w, x):
        self.w = w
        self.x = x
    def forward(self):
        self.wval = self.w.forward()
        self.xval = self.x.forward()
        return self.wval + self.xval
    def backward(self, val, lrate):
        self.w.backward(val, lrate)
        self.x.backward(val, lrate)

class Square:
    def __init__(self, x):
        self.x = x
    def forward(self):
        self.val = self.x.forward()
        return self.val * self.val
    def backward(self, val, lrate):
        self.x.backward(2 * self.val * val, lrate)


if __name__ == '__main__':
    Init()
    w0, w1 = 3, 4
    X0 = Tensor(x0)
    X1 = Tensor(x1)
    W0 = Weight(w0)
    W1 = Weight(w1)
    Z = Add(Mul(W0, X0), Mul(W1, X1))
    lrate = 0.01
    print y
    for i in range(1000):
        s = Z.forward()
        diff = s - y
        print "Loss: ", (0.5*np.square(diff)).sum()
        Z.backward(diff, 1e-4)
        print W0.val, W1.val
