import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


Lx = 50  # Длина области по x
Ly = 50  # Длина области по y
T = 1  # Время интегрирования
Nx = 50  # Количество точек по x
Ny = 50  # Количество точек по y
Nt = 100  # Количество шагов по времени
c = 2 # Коэффициент теплопроводности
f = lambda t: 30 * np.log(1 + t)


# Функция для решения уравнения теплопроводности с использованием неявной схемы
def solve_heat_equation_implicit(Lx, Ly, T, Nx, Ny, Nt, c, f):
    # Шаги по координатам
    dx = Lx / Nx
    dy = Ly / Ny
    dt = T / Nt

    # Инициализация сетки
    x_values = np.linspace(0, Lx, Nx + 1)
    y_values = np.linspace(0, Ly, Ny + 1)
    t_values = np.linspace(0, T, Nt + 1)
    u = np.zeros((Nx + 1, Ny + 1, Nt + 1))

    # Начальные и краевые условия
    u[:, :, 0] = 30  # Начальная температура
    u[0, :, :] = 30  # Граничное условие на левой границе
    u[-1, :, :] = 100  # Граничное условие на правой границе
    u[:, 0, :] = 30  # Граничное условие на нижней границе
    u[:, -1, :] = 30  # Граничное условие на верхней границе

    # Численное решение
    for n in range(Nt):
        A = np.eye(Nx - 1) * (1 + 2 * c * dt / dx ** 2) - np.eye(Nx - 1, k=1) * (c * dt / dx ** 2) - np.eye(Nx - 1,
                                                                                                            k=-1) * (
                        c * dt / dx ** 2)
        for j in range(1, Ny):
            b = np.zeros(Nx - 1)
            for i in range(1, Nx):
                b[i - 1] = u[i, j, n] + c * dt * (u[i, j - 1, n] - 2 * u[i, j, n] + u[i, j + 1, n]) / dy ** 2 + f(
                    t_values[n])
            b[0] += c * dt * u[0, j, n] / dx ** 2
            b[-1] += c * dt * u[-1, j, n] / dx ** 2
            u[1:-1, j, n + 1] = np.linalg.solve(A, b)
    return x_values, y_values, t_values, u


# Решение уравнения теплопроводности с неявной схемой
x_values_imp, y_values_imp, t_values_imp, u_imp = solve_heat_equation_implicit(Lx, Ly, T, Nx, Ny, Nt, c, f)

# Создание анимации для неявной схемы
fig, ax = plt.subplots(figsize=(10, 7))
contour = ax.contourf(x_values_imp, y_values_imp, u_imp[:, :, 0], cmap='coolwarm', alpha=0.5)


def update_imp(frame):
    global contour
    for coll in contour.collections:
        coll.remove()
    contour = ax.contourf(x_values_imp, y_values_imp, u_imp[:, :, frame], cmap='coolwarm', alpha=0.5)
    return contour


anim_imp = FuncAnimation(fig, update_imp, frames=Nt + 1, repeat=False)
plt.colorbar(contour, label='Температура')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Распределение температуры по времени (Неявная разностная схема)')
plt.show()
