#complexnumber

class Complex():
    def __init__ (self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other_complex_number):
        real_result = self.real + other_complex_number.real
        imag_result = self.imag + other_complex_number.imag
        return Complex(real_result, imag_result)

    def __repr__ (self):
        return ( (f'{self.real}') + ('+' if self.imag >= 0 else '-' ) + (f'{self.imag}i'))

c1 = Complex(5, 10)
c2 = Complex(2, 4)

print(c1 + c2)
