# y = Ax+b
class Num:
    def __init__(self, val):
        self.val = val
    def forward(self):
        return self.val

class Mul:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def forward(self):
        return self.left.forward() * self.right.forward()

class Add:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def forward(self):
        return self.left.forward() + self.right.forward()

if __name__ == '__main__':
    x = Num(1)
    a = Num(2)
    b = Num(3)
    m = Mul(a, x)
    y = Add(m, b)
    print y.forward()
