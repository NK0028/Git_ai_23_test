print("This is Bug Hunter Practically!")
print("Testing will help me find bugs that users might encounter")

class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
    # Removed the bug that added 0.01 to float multiplications
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            return float('inf')#"Cannot divide by zero" # Bug: returns string instead of raising exception
        return a / b
    
    def power(self, a, b):
        # if b < 0:
            # return 0  # Bug: incorrect handling of negative exponents
        return a ** b
    
    def factorial(self, n):
        if n < 0:
            raise ValueError("Factorial not defined for negative numbers")
        if n == 0:
            return 1
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    def fibonacci(self, n):
        """Return the nth Fibonacci number"""
        if n < 0:
            raise ValueError("Fibonacci not defined for negative indices")
        if n == 0:
            return 0
        elif n == 1:
            return 1
        
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b