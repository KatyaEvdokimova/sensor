import numpy as np

def f(x, y):
    return 2*x - np.exp(-2*x) + 7

def runge_kutta_merson(x0, y0, h, xf):
    x_values = [x0]
    y_values = [y0]

    while x0 > xf:
        k1 = h * f(x0, y0)
        k2 = h * f(x0 + 0.5*h, y0 + 0.5*k1)
        k3 = h * f(x0 + 0.5*h, y0 + 0.5*k2)
        k4 = h * f(x0 + h, y0 + k3)

        y_temp = y0 + (k1 + 4*k3 + k4) / 6
        k5 = h * f(x0 + h, y_temp)

        y_next = y0 + (k1 + 4*k3 + k5) / 6
        x0 -= h
        y0 = y_next

        x_values.append(x0)
        y_values.append(y_next)

    return x_values, y_values

# Начальные условия и параметры
x0 = -0.1
y0 = 7.8
h = 0.03
xf = -0.84

# Решение дифференциального уравнения методом Рунге-Кутты-Мерсона
x_values, y_values = runge_kutta_merson(x0, y0, h, xf)

# Вывод значений x и y
for i in range(len(x_values)):
    print(f"x = {x_values[i]:.2f}, y = {y_values[i]:.4f}")
