def f(x):
    return x**3 - 3*x

precision = 0.000001
whole_interval = [-1000, 1000]

def finding_interval(whole_interval):
    a_whole, b_whole = whole_interval
    interval_list = []
    a = b_whole - 1
    b = b_whole
    while a > a_whole:
        if f(a) * f(b) <= 0:
            interval_list.append([a, b])
        a -= 1
        b -= 1
    if len(interval_list) == 0:
        raise ValueError("No intervals found where f(a) and f(b) have different signs")
    return interval_list



def bisection(interval, precision):
    a,b = interval
    iterations = 0
    if f(a) * f(b) > 0:
       raise ValueError("f(a) and f(b) must have different signs")
    elif f(a) == 0:
        print(f'Exact root found at a: {a}')
        return
    elif f(b) == 0:
        print(f'Exact root found at b: {b}')
        return
    else:
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

interval = finding_interval(whole_interval)

for i in interval:
    print(f'Finding root in interval: {i}')
    bisection(i, precision)
    print('-----------------------------------')