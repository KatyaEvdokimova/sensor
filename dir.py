import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Функции
def f1(x):
    return 2 * x - np.exp(-2 * x) + 7

def f2(x):
    return 3 * x**3 - 2 * np.arctan(x) - 178 - np.exp(-8) + 2 * np.arctan(4)

def f3(x):
    return x**3 + np.sqrt(x) + 254 - np.exp(-8) - np.sqrt(6) - 2 * np.arctan(6) + 2 * np.arctan(4)

# Диапазоны x
x1 = np.linspace(-2, 4, 400)  # Для x <= 4
x2 = np.linspace(4, 6, 400)   # Для 4 < x <= 6
x3 = np.linspace(6, 10, 400)  # Для x > 6

# Вычисление значений функций
y1 = f1(x1)
y2 = f2(x2)
y3 = f3(x3)

# Построение графиков
plt.figure(figsize=(10, 6))

plt.plot(x1, y1, label=r'$2x - e^{-2x} + 7$', color='blue')
plt.plot(x2, y2, label=r'$3x^3 - 2 \arctan(x) - 178 - e^{-8} + 2 \arctan(4)$', color='green')
plt.plot(x3, y3, label=r'$x^3 + \sqrt{x} + 254 - e^{-8} - \sqrt{6} - 2 \arctan(6) + 2 \arctan(4)$', color='red')

# Находим и отмечаем точки пересечения с осью x
intersection_points = [(fsolve(f1, -0.84)[0], 0)]

for point in intersection_points:
    plt.scatter(point[0], point[1], color='black', marker='x', label=f'Intersection Point ({point[0]:.2f}, 0)')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Graphs of Given Functions with Intersection Points')
plt.axvline(x=4, color='gray', linestyle='--')
plt.axvline(x=6, color='gray', linestyle='--')
plt.legend()
plt.grid(True)
plt.show()
