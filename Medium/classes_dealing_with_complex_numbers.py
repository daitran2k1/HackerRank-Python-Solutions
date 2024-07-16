import math


class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        return Complex(self.real + no.real, self.imaginary + no.imaginary)

    def __sub__(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary)

    def __mul__(self, no):
        new_real = self.real * no.real - self.imaginary * no.imaginary
        new_imaginary = self.real * no.imaginary + self.imaginary * no.real
        return Complex(new_real, new_imaginary)

    def __truediv__(self, no):
        length = no.real**2 + no.imaginary**2
        new_real = (self.real * no.real + self.imaginary * no.imaginary) / length
        new_imaginary = (self.imaginary * no.real - self.real * no.imaginary) / length
        return Complex(new_real, new_imaginary)

    def mod(self):
        return Complex((self.real**2 + self.imaginary**2) ** 0.5, 0)

    def __str__(self):
        if self.imaginary == 0:
            result = f"{self.real:.2f}+0.00i"
        elif self.real == 0:
            if self.imaginary >= 0:
                result = f"0.00+{self.imaginary:.2f}i"
            else:
                result = f"0.00-{-self.imaginary:.2f}i"
        elif self.imaginary > 0:
            result = f"{self.real:.2f}+{self.imaginary:.2f}i"
        else:
            result = f"{self.real:.2f}-{-self.imaginary:.2f}i"

        return result


if __name__ == "__main__":
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x + y, x - y, x * y, x / y, x.mod(), y.mod()]), sep="\n")
