import math

def addiction(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("devision by zero")
    return a / b

def power(a, b):
    if b < 0:
        raise ValueError('not avalible')
    return math.pow(a, b)

def sqroot(a):
    if a < 0:
        raise ValueError("must be positive")
    return math.sqrt(a)

