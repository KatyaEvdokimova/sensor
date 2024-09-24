import numpy as np

# Функции для системы уравнений
def f(x):
    if x <= 4:
        return 2*x - np.exp(-2*x) + 7
    elif 4 < x <= 6:
        return 3*x**3 - 2*np.arctan(x) - 178 - np.exp(-8) + 2*np.arctan(4)
    else:
        return x**3 + np.sqrt(abs(x)**4) + 254 - np.exp(-8) - np.sqrt(6) - 2*np.arctan(6) + 2*np.arctan(4)

# Производная функции для неявного метода
def df(x):
    if x <= 4:
        return 2 + 2*np.exp(-2*x)
    elif 4 < x <= 6:
        return 9*x**2 - 2/(1 + x**2)
    else:
        return 3*x**2 + 1/(2*np.sqrt(x**3))

# Неявный итерационный метод
def implicit_iteration(x0, tol, max_iter):
    x_old = x0
    for i in range(max_iter):
        x_new = x_old - f(x_old) / df(x_old)
        if abs(x_new - x_old) < tol:
            return x_new, i+1
        x_old = x_new
    return None, max_iter

# Начальное приближение
x0 = 4

# Параметры метода
tolerance = 1e-2
max_iterations = 1000

# Применение метода Ньютона
solution_newton, iterations_newton = implicit_iteration(x0, tolerance, max_iterations)

# Вывод результатов
print("Неявный метод:")
if solution_newton is not None:
    print("Решение:", solution_newton)
    print("Количество итераций:", iterations_newton)
else:
    print("Метод не сошелся")