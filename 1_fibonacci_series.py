# Fibonacci series
a, b = 0, 1
while b < 20:
    print(b)
    a, b = b, a+b

a, b = 0, 1
while b < 20:
    print(b, end=', ')
    a, b = b, a + b