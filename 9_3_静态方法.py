from math import sqrt

# 静态方法，就是在类没有实例化的时候就能通过类名直接调用的方法
class Triangle(object):
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod # 静态方法
    def is_valid(a, b, c):
        return a+b >c and a+c >b and b+c >a

    def perimeter(self):  # 计算周长的方法
        return self._a + self._b + self._c
    
    def area(self): # 海伦公式计算
        half = self.perimeter()/2
        return sqrt(half*(half - self._a)*(half - self._b)*(half - self._c))
    


def main():
    a, b, c = 3, 4, 5
    if Triangle.is_valid(a, b, c):
        t = Triangle(a, b, c)
        print(t.perimeter())
        print(t.area())
    else:
        print("不能构成三角形")

if __name__ == "__main__":
    main()