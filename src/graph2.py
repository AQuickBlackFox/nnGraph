# t = 2 * (x*y + max(z,w))

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

if __name__ == '__main__':
    x = Num(3)
    y = Num(-4)
    z = Num(2)
    w = Num(-1)
    p = Mul(x, y)
    q = Max(z, w)
    r = Add(p, q)
    t = Factor(r, 2)
    print t.forward()
    t.backward(1)
