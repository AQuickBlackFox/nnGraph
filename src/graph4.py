import numpy as np
import math

num_samples = 10000 #10,000
x = np.random.uniform(0, 1, num_samples)
y = np.empty_like(x)

def Init():
    p, q = 1, 2
    for i in range(num_samples):
        y[i] = p * x[i] * x[i] + q * x[i]

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
    p, q = 3, 4
    X = Tensor(x)
    Q = Weight(q)
    P = Weight(p)
    Z = Add(Mul(P, Square(X)), Mul(Q, X))
    lrate = 0.01
    print y
    for i in range(1000):
        s = Z.forward()
        diff = s - y
        print "Loss: ", (0.5*np.square(diff)).sum()
        Z.backward(diff, 1e-4)
        print P.val, Q.val
