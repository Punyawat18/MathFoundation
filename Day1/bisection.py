def f(x):
    return x**2 - 2

interval = [0, 2]
precision = 0.000001

def bisection(interval, precision):
    a,b = interval
    iterations = 0
    if f(a) * f(b) >= 0:
       raise ValueError("f(a) and f(b) must have different signs")
    while abs(b - a) > precision:
        c = (a + b) / 2
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iterations += 1
        print(f'Iteration[{iterations}] : [{a}, {b}]')
    print(f'Final Iteration[{iterations}] : [{a}, {b}]')
    print(f'Final Approximation : {c}, Value of Function : {f(c)}')

bisection(interval, precision)