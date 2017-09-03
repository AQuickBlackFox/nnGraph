# f(x,w) = 1 / (1 + exp(-(w0*x0 + w1*x1 + w2)))

import math

class Num:
    def __init__(self, val):
        self.val = val
    def forward(self):
        return self.val
    def backward(self, val):
        print val

class Mul:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def forward(self):
        self.left_fw = self.left.forward()
        self.right_fw = self.right.forward()
        return self.left_fw * self.right_fw
    def backward(self, val):
        self.left.backward(val * self.right_fw)
        self.right.backward(val * self.left_fw)

class Factor:
    def __init__(self, center, factor):
        self.center = center
        self.factor = factor
    def forward(self):
        return self.factor * self.center.forward()
    def backward(self, val):
        self.center.backward(val * self.factor)

class Add:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def forward(self):
        return self.left.forward() + self.right.forward()
    def backward(self, val):
        self.left.backward(val)
        self.right.backward(val)

class Inv:
    def __init__(self, center):
        self.center = center
    def forward(self):
        self.out = 1 / self.center.forward()
        return self.out
    def backward(self, val):
        self.center.backward(val * (-1/self.out**2))

class Max:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def forward(self):
        self.left_fw = self.left.forward()
        self.right_fw = self.right.forward()
        self.out = 0
        if self.left_fw > self.right_fw:
            self.out = 1
            return self.left_fw
        return self.right_fw
    def backward(self, val):
        self.left.backward(val * self.out)
        self.right.backward(val * (1 - self.out))

class Exp:
    def __init__(self, center):
        self.center = center
    def forward(self):
        return math.exp(self.center.forward())
    def backward(self, val):
        self.center.backward(math.exp(val))

class Sigmoid:
    def __init__(self, center):
        self.center = center
    def forward(self):
        self.out = (1 / (1 + math.exp(-self.center.forward())))
        return self.out
    def backward(self, val):
        self.center.backward(val * (1 - self.out)*self.out)

if __name__ == '__main__':
    w0 = Num(+2.0)
    x0 = Num(-1.0)
    w1 = Num(-3.0)
    x1 = Num(-2.0)
    w2 = Num(-3.0)
    one = Num(+1.0)
    p = Mul(w0, x0)
    q = Mul(w1, x1)
    r = Add(p, q)
    s = Add(r, w2)
    w = Sigmoid(s)
    print w.forward()
    w.backward(1)
