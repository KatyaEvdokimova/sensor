import numpy as np
import matplotlib.pyplot as plt

# Явный метод Эйлера
def euler_explicit(func, u0, t0, T, dt_max, E):
    t_values = [t0]
    u_values = [np.array(u0)]
    t = t0

    while t < T:
        dt = min(dt_max, E / (np.max(abs(func(t, u_values[-1]))) + E / dt_max))
        u_next = u_values[-1] + dt * func(t, u_values[-1])
        t_next = t + dt
        if t_next >= T:
            break
        t = t_next
        t_values.append(t)
        u_values.append(u_next)

    return np.array(t_values), np.array(u_values)

# Функция, задающая правую часть системы дифференциальных уравнений
def my_system(t, u):
    u1, u2 = u
    dudt = np.array([
        u2 - (2.25*u1 + u2 / 2) * u1,
        np.exp(u1) - (u1 + 2.25*u2) * u1
    ])
    return dudt

# Начальные условия
u0 = [1, 0]
t0 = 0
T = 1
dt_max = 0.01
E = 1e-3

# Решение системы
t_values, u_values = euler_explicit(my_system, u0, t0, T, dt_max, E)

# Вывод результатов
for t, u1, u2 in zip(t_values, u_values[:, 0], u_values[:, 1]):
    print(f"t = {t:.5f}, u1 = {u1:.6f}, u2 = {u2:.6f}")

# Построение графика для u1 и u2
plt.plot(t_values, u_values[:, 0], label='u1')
plt.plot(t_values, u_values[:, 1], label='u2')
plt.xlabel('Ось t')
plt.ylabel('Ось u')
plt.title('Явный метод Эйлера для задачи 2')
plt.legend()
plt.grid(True)
plt.show()
