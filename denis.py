import numpy as np

# Функция для оценки шага dt
def estimate_dt(t, u, dt_max, E):
    return min(dt_max, E / np.max(np.abs(u)))

# Явный метод Эйлера
def euler_explicit(func, u0, t0, T, dt_max, E):
    t_values = [t0]
    u_values = [np.array(u0)]
    t = t0

    while t < T:
        dt = min(dt_max, E / (np.linalg.norm(func(t, u_values[-1])) + E / dt_max))
        u_next = u_values[-1] + dt * func(t, u_values[-1])
        t_next = t + dt
        if t_next >= T:
            break  # Прекращаем цикл, если следующее время превышает T
        t = t_next
        t_values.append(t)
        u_values.append(u_next)

    return np.array(t_values), np.array(u_values)


# Функция, задающая правую часть системы дифференциальных уравнений
def my_system(t, u):
    u1, u2 = u
    a = 1  # параметр a
    dudt = np.array([
        -u1 * u2 + np.sin(t) / (t if t != 0 else 1e-12),
        -u2 ** 2 + (a * t) / (1 + t ** 2)
    ])
    return dudt

# Начальные условия
u0 = [0, -0.412]
t0 = 0
T = 1
dt_max = 0.2
E = 1e-3

# Решение системы
t_values, u_values = euler_explicit(my_system, u0, t0, T, dt_max, E)

# Вывод результатов
for t, u1, u2 in zip(t_values, u_values[:, 0], u_values[:, 1]):
    print(f"t = {t:.6f}, u1 = {u1:.6f}, u2 = {u2:.6f}")