import math

f = lambda x: x**3 + 4*(x**2) -10
f_prime= lambda x: 3*(x**2)
x0 = 2
epsilon = 0.0001

def newton_method(f, f_prime, x0, epsilon):
    x = x0
    iterations = 0
    while True:
        fx = f(x)
        fpx = f_prime(x)
        if abs(fx / fpx) < epsilon:
            break
        x = x - fx / fpx
        iterations += 1
    return x, iterations

def secant_method(f, x0, x1, epsilon):
    fx0 = f(x0)
    fx1 = f(x1)
    iterations = 0
    while abs(fx1) > epsilon:
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        x0, x1 = x1, x2
        fx0, fx1 = fx1, f(x2)
        iterations += 1
    return x1, iterations

def secant_newton_method(f, f_prime, x0, x1, epsilon):
    iterations = 0
    while True:
        fx0 = f(x0)
        fx1 = f(x1)
        if abs(fx1) < epsilon:
            return x1, iterations
        elif abs(fx0) < epsilon:
            return x0, iterations
        x2, n_iterations = newton_method(f, f_prime, x1, epsilon)
        x0, x1 = x1, x2
        iterations += n_iterations
        if abs(f(x1)) < epsilon:
            return x1, iterations
        x2, n_iterations = secant_method(f, x0, x1, epsilon)
        x0, x1 = x1, x2
        iterations += n_iterations