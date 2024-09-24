import numpy as np

def F(x, f):
    if x <= 4:
        return 2 * x - np.exp(-2 * x) + 7 - f
    elif x <= 6:
        return 3 * x**3 - 2 * np.arctan(x) - 178 - np.exp(-8) + 2 * np.arctan(4) - f
    else:
        return x**3 + np.sqrt(x) + 254 - np.exp(-8) - np.sqrt(6) - 2 * np.arctan(6) + 2 * np.arctan(4) - f

def dF(x):
    if x <= 4:
        return 2 + 2 * np.exp(-2 * x)
    elif x <= 6:
        return 9 * x**2 - 2 / (1 + x**2)
    else:
        return 3 * x**2 + 1 / (2 * np.sqrt(x))

def explicit_iteration(x0, f, epsilon):
    x_prev = x0
    x_curr = x_prev - F(x_prev, f) / dF(x_prev)
    iteration = 1
    while abs(x_curr - x_prev) >= epsilon:
        x_prev = x_curr
        x_curr = x_prev - F(x_prev, f) / dF(x_prev)
        iteration += 1
    return x_curr, iteration

# Начальное приближение и погрешность
x0 = 0
epsilon = 1e-2
f = 0

root, iterations = explicit_iteration(x0, f, epsilon)
print("Корень:", root)
print("Число итераций:", iterations)
