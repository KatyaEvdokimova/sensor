import numpy as np
import matplotlib.pyplot as plt

# Задаем начальные условия и параметры
alpha_1 = 1
alpha_2 = 2
alpha_3 = 2
u0 = [10, 22, 9]
T = 1
E = 1e-3
t_max = 0.01


def F(t, u):
    u1, u2, u3 = u
    A = (1 / 6) * np.array([[2*alpha_1 + 4*alpha_2, 2*(alpha_1 - alpha_2), 2*(alpha_1 - alpha_2)],
                             [2*(alpha_1 - alpha_2), 2*alpha_1 + alpha_2 + 3*alpha_3, 2*alpha_1 + alpha_2 - 3*alpha_3],
                             [2*(alpha_1 - alpha_2), 2*alpha_1 + alpha_2 - 3*alpha_3, 2*alpha_1 + alpha_2 + 3*alpha_3]])
    b = -(1 / 6) * np.array([4*alpha_1 + 2*alpha_2, 4*alpha_1 - alpha_2 - 9*alpha_3, 4*alpha_1 - alpha_2 + 9*alpha_3])
    dudt = np.dot(A, u) - b
    return dudt


def backward_euler(F, u0, tau, T):
    from scipy import optimize
    N_t = int(round(T / tau))
    F_ = lambda t, u: np.asarray(F(t, u), dtype=float)
    t = np.linspace(0, N_t * tau, N_t + 1)
    u = np.zeros((N_t + 1, len(u0)))
    u[0] = np.array(u0)

    def Phi(z, t, v):
        return z - tau * F_(t, z) - v

    for n in range(N_t):
        u[n + 1] = optimize.fsolve(Phi, u[n], args=(t[n], u[n]))
        print(f"t = {t[n + 1]:.6f}, u1 = {u[n + 1, 0]:.6f}, u2 = {u[n + 1, 1]:.6f}, u3 = {u[n + 1, 2]:.6f}")

    return u, t


us, ts = backward_euler(F, u0, t_max, T)

plt.plot(ts, us[:, 0], label='u1')
plt.plot(ts, us[:, 1], label='u2')
plt.plot(ts, us[:, 2], label='u3')
plt.xlabel('Ось t')
plt.ylabel('Ось u')
plt.title('Неявный метод Эйлера для 4 задачи')
plt.legend()
plt.grid(True)
plt.show()
