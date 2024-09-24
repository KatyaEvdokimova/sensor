import numpy as np

def F(x, f):
    if x <= 4:
        return 2 * x - np.exp(-2 * x) + 7 - f
    elif x <= 6:
        return 3 * x**3 - 2 * np.arctan(x) - 178 - np.exp(-8) + 2 * np.arctan(4) - f
    else:
        return x**3 + np.sqrt(x) + 254 - np.exp(-8) - np.sqrt(6) - 2 * np.arctan(6) + 2 * np.arctan(4) - f

def explicit_iteration(x0, f, epsilon, max_iter=1000):
    x_curr = x0
    iteration = 0
    while iteration < max_iter:
        x_next = x_curr - F(x_curr, f)
        if abs(x_next - x_curr) < epsilon:
            return x_next, iteration + 1
        x_curr = x_next
        iteration += 1
    raise ValueError("Метод не сошелся после максимального числа итераций")

# Начальное приближение и погрешность
x0 = 0
epsilon = 1e-2
f = 2

# Запуск явного итерационного метода
root, iterations = explicit_iteration(x0, f, epsilon)
print("Корень:", root)
print("Число итераций:", iterations)
