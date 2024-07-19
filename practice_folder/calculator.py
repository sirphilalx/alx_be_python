class Calculator:
    
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def multiply(x, y):
        return x * y
    
first = Calculator(3, 7)

additioin = first.add(2, 6)
multiplication = first.multiply(2, 6)

print(additioin)
print(multiplication)