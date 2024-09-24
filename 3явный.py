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
    u1, u2, u3 = u
    k = 3
    a = 1
    dudt = np.array([
        (k - a) / a * u2 * u3,
        (a + k) / k * u1 * u3,
        (a - k) / a * u1 * u2
    ])
    return dudt

# Начальные условия
u0 = [1, 1, 1]
t0 = 0
T = 1
dt_max = 0.01
E = 1e-3

# Решение системы
t_values, u_values = euler_explicit(my_system, u0, t0, T, dt_max, E)

# Вывод результатов
for t, u1, u2, u3 in zip(t_values, u_values[:, 0], u_values[:, 1], u_values[:, 2]):
    print(f"t = {t:.6f}, u1 = {u1:.6f}, u2 = {u2:.6f}, u3 = {u3:.6f}")

plt.plot(t_values, u_values[:, 0], label='u1')
plt.plot(t_values, u_values[:, 1], label='u2')
plt.plot(t_values, u_values[:, 2], label='u3')
plt.xlabel('Ось t')
plt.ylabel('Ось u')
plt.title('Явный метод Эйлера для задачи 3')
plt.legend()
plt.grid(True)
plt.show()
