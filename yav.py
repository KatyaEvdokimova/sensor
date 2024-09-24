import numpy as np

# Функции для системы уравнений
def f(x):
    if x <= 4:
        return 2*x - np.exp(-2*x) + 7
    elif 4 < x <= 6:
        return 3*x**3 - 2*np.arctan(x) - 178 - np.exp(-8) + 2*np.arctan(4)
    else:
        return x**3 + 254 - np.exp(-8) - np.sqrt(6) - 2*np.arctan(6) + 2*np.arctan(4)

# Явный итерационный метод
def explicit_iteration_method(x0, f, tol, max_iter):
    x_old = x0
    for i in range(max_iter):
        x_new = f(x_old)
        if abs(x_new - x_old) < tol:
            return x_new, i+1
        x_old = x_new
    return None, max_iter

# Начальное приближение
x0 = 10

# Параметры метода
tolerance = 1e-8
max_iterations = 10000  # Увеличили количество итераций

# Применение явного метода
solution, iterations = explicit_iteration_method(x0, f, tolerance, max_iterations)

# Вывод результатов
print("Явный метод:")
if solution is not None:
    print("Решение:", solution)
    print("Количество итераций:", iterations)
else:
    print("Метод не сошелся")