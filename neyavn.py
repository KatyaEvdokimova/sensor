import numpy as np
import scipy.optimize as optimize

def du1_dt(u1, u2, t):
    return -u1 * u2 + np.sin(t)/(t if t != 0 else 1e-12)

def du2_dt(u1, u2, t, a):
    return -u2 + a * t / (1 + t**2)

def implicit_euler(u1, u2, t, dt, a, e):
    t_max = t + dt
    while t < t_max:
        u1_old, u2_old = u1, u2
        # Установить начальные значения переменных y_k+1
        u1_new, u2_new = u1_old, u2_old
        # Решить систему нелинейных алгебраических уравнений методом Ньютона
        def equations(delta_u1_u2):
            delta_u1, delta_u2 = delta_u1_u2
            return [
                delta_u1 - du1_dt(u1_old + delta_u1, u2_old + delta_u2, t_max) * dt,
                delta_u2 - du2_dt(u1_old + delta_u1, u2_old + delta_u2, t_max, a) * dt
            ]
        initial_guess = [0, 0]
        delta_u1, delta_u2 = optimize.root(equations, initial_guess).x
        u1_new += delta_u1
        u2_new += delta_u2
        # Вычислить ошибку
        error = max(abs(delta_u1), abs(delta_u2))
        # Если ошибка больше заданной погрешности, уменьшаем шаг
        while error > e:
            dt /= 2
            t_max = t + dt
            delta_u1, delta_u2 = optimize.root(equations, initial_guess).x
            u1_new = u1_old + delta_u1
            u2_new = u2_old + delta_u2
            error = max(abs(delta_u1), abs(delta_u2))
        # Вывести на печать новые значения переменных и t_k+1
        print_results(t_max, u1_new, u2_new)
        # Сделать сдвиг переменных и шагов интегрирования
        t = t_max
        u1, u2 = u1_new, u2_new

def print_results(t, u1, u2):
    print(f"t = {t:.6f}, u1 = {u1:.6f}, u2 = {u2:.6f}")

# Исходные данные
t_min = 0
t_max = 1
e = 1e-3
t_0 = 0
T = 1
dt = 0.1
a = 1

# Начальные условия
u1 = 0
u2 = 0
t = t_0

# Вызов неявного метода Эйлера
implicit_euler(u1, u2, t, dt, a, e)