class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
        print(f"Complex number created: {self.real} + {self.imag}i")

    def __del__(self):
        print(f"Complex number {self.real} + {self.imag}i is destroy.")

    def __add__(self, other):
        result = ComplexNumber(self.real + other.real, self.imag + other.imag)
        return result
    
    def __sub__(self, other):
        result = ComplexNumber(self.real - other.real, self.imag - other.imag)
        return result
    
    def __str__(self):
        return f"{self.real} + {self.imag}i"
    
c1 = ComplexNumber(5, 3)
c2 = ComplexNumber(2, 4)

print("\nAddition: ")
c3 = c1 + c2
print(c3)

print("\nSubstraction: ")
c4 = c1 - c2
print(c4)