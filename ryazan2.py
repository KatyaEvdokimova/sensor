import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Функции
def f1(x):
    return x**3 + 2*x - 21

def f2(x):
    return x**5 + np.cos(np.pi*x/2)

def f3(x):
    return x + x**(1/3) + 240 - 3**(1/3)

# Диапазоны x
x1 = np.linspace(-5, -2, 400)    # Для x <= -2
x2 = np.linspace(-2, 3, 400)     # Для -2 < x <= 3
x3 = np.linspace(3, 10, 400)     # Для x > 3

# Вычисление значений функций
y1 = f1(x1)
y2 = f2(x2)
y3 = f3(x3)

# Построение графиков
plt.figure(figsize=(10, 6))

plt.plot(x1, y1, label=r'$x^3 + 2x - 21$', color='blue')
plt.plot(x2, y2, label=r'$x^5 + \cos(\frac{\pi x}{2})$', color='green')
plt.plot(x3, y3, label=r'$x + x^{1/3} + 240 - 3^{1/3}$', color='red')

# Находим и отмечаем точку пересечения с осью x
intersection_points = [(-0.79, 0)]

for point in intersection_points:
    plt.scatter(point[0], point[1], color='black', marker='x', label=f'Intersection Point ({point[0]:.2f}, 0)')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Graphs of Given Functions with Intersection Points')
plt.axvline(x=-2, color='gray', linestyle='--')
plt.axvline(x=3, color='gray', linestyle='--')
plt.legend()
plt.grid(True)
plt.show()
