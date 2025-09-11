class Calculator:
    def add(self, array):
        if len(array) < 2:
            raise ValueError("Bad number of params")
        return sum(array)

    def subtract(self, array):
        if len(array) < 2:
            raise ValueError("Bad number of params")
        result = array[0]
        for i in range(1, len(array)):
            result -= array[i]
        return result

    def multiply(self, array):
        if len(array) < 2:
            raise ValueError("Bad number of params")
        result = 1
        for i in array:
            result *= i
        return result

    def divide(self, a, b):
        if len(array) != 2:
            raise ValueError("Bad number of params")
        if b == 0:
            raise ValueError("Division by zero")
        return a / b
