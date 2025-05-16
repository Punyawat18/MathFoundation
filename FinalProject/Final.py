import sympy
import matplotlib.pyplot as plt

rate = 0.01
precision = 0.000001
start_x = 10

### For Momentum method
beta = 0.5

### For ADMM method
start_z = 0
strength = 0.5

def function_x():
    x = sympy.symbols('x')
    return (x*x) - (8*x) + 6

def derivative_of_function_x():
    x = sympy.symbols('x')
    return sympy.diff(function_x(), x)

def f(x):
    return function_x().subs({sympy.symbols('x'): x})

def df(x):
    return derivative_of_function_x().subs({sympy.symbols('x'): x})


def gradient(start_x, rate, precision):
    x = start_x
    iterations = 0
    data = []
    while abs(rate * df(x)) > precision:
        x = x - (rate * df(x))
        iterations += 1
        data.append([iterations, f(x)])
    return data

def momentum(start_x, rate, beta, precision):
    x = start_x
    iterations = 0
    data = []
    v = 0
    while True:
        v = (beta * v) + (rate * df(x))
        x = x - v
        iterations += 1
        data.append([iterations, f(x)])
        if abs(v) < precision:
            break
    return data

def admm(start_x, start_z, rate, strength, precision):
    x = start_x
    z = start_z
    data_x = []
    data_z = []
    u = 0
    iterations_x = 0
    iterations_z = 0
    while abs(x - z) > precision:
        x = x - (rate * (df(x) + (strength * (x - z + u))))
        z = z - (rate * (df(z) + (strength * (z - x - u))))
        u = u + x - z
        iterations_x += 1
        iterations_z += 1
        data_x.append([iterations_x, f(x)])
        data_z.append([iterations_z, f(z)])
    return data_x, data_z

def plot_graph(data, method_name):
    x = []
    y = []
    for i in data:
        x.append(i[0])
        y.append(i[1])
    plt.plot(x, y, label=method_name)
    plt.xlabel('Iterations')
    plt.ylabel('Value of Function')
    plt.title(f'Comparison Graph')
    plt.legend()

gradient_data = gradient(start_x, rate, precision)
plot_graph(gradient_data, 'Gradient Descent')
momentum_data = momentum(start_x, rate, beta, precision)
plot_graph(momentum_data, 'Momentum Method')
admm_data_x, admm_data_z = admm(start_x, start_z, rate, strength, precision)
plot_graph(admm_data_x, 'ADMM Method (x)')
plot_graph(admm_data_z, 'ADMM Method (z)')
plt.grid()
plt.show()
