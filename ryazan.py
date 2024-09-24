import numpy as np
import matplotlib.pyplot as plt

# Функции
def f1(x):
    return 2 * x - np.exp(-2 * x) + 7

def f2(x):
    return 3 * x**3 - 2 * np.arctan(x) - 178 - np.exp(-8) + 2 * np.arctan(4)

def f3(x):
    return x**3 + np.sqrt(x) + 254 - np.exp(-8) - np.sqrt(6) - 2 * np.arctan(6) + 2 * np.arctan(4)

# Диапазоны x
x1 = np.linspace(0, 4, 400)
x2 = np.linspace(4.01, 6, 400)
x3 = np.linspace(6.01, 10, 400)

# Вычисление значений функций
y1 = f1(x1)
y2 = f2(x2)
y3 = f3(x3)

# Построение графиков
plt.figure(figsize=(10, 6))

plt.plot(x1, y1, label=r'$f_1(x) = 2x - e^{-2x} + 7| x<=4$', color='blue')
plt.plot(x2, y2, label=r'$f_2(x) = 3x^3 - 2 \arctan(x) - 178 - e^{-8} + 2 \arctan(4)| 4<x<=6$ ', color='green')
plt.plot(x3, y3, label=r'$f_3(x) = x^3 + \sqrt[4]{x} + 254 - e^{-8} - \sqrt[4]{6} - 2 \arctan(6) + 2 \arctan(4)| x>6$', color='red')

# Точка пересечения в x = 2.01
x_intersection = 2.5
y_intersection = f1(x_intersection)

plt.scatter(x_intersection, y_intersection, color='black', label=f'Точка пересечения (x={x_intersection}, y={y_intersection:.2f})')
plt.xlabel('x')
plt.ylabel('y')
plt.title('График Ax=f=10')
plt.axvline(x=4, color='gray', linestyle='--')
plt.axvline(x=6, color='gray', linestyle='--')
plt.legend()
plt.grid(True)
plt.show()
