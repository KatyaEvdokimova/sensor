import numpy as np
import matplotlib.pyplot as plt
import math

a = 2.25
ei_dop = 10e-3
t0 = 0
T = 1
u0 = [1, 0]
tmax = 0.01


def F(t, u):
    u1, u2 = u
    r = [
        u2 - (2.25 * u1 + u2 / 2) * u1,
        np.exp(u1) - (u1 + 2.25 * u2) * u1
    ]
    return r


tk = 10e-9
yk = np.array(u0)


def backward_euler(F, u0, tau, T):
    from scipy import optimize
    N_t = int(round(T / tau))
    F_ = lambda t, u: np.asarray(F(t, u), dtype=float)
    t = np.linspace(10e-9, N_t * tau, N_t + 1)
    u = np.zeros((N_t + 1, len(u0)))
    u[0] = np.array(u0)

    def Phi(z, t, v):
        return z - tau * F_(t, z) - v

    for n in range(N_t):
        u[n + 1] = optimize.fsolve(Phi, u[n], args=(t[n], u[n]))
        print(f"t = {t[n + 1]:.6f}, u1 = {u[n + 1, 0]:.6f}, u2 = {u[n + 1, 1]:.6f}")

    return u, t


us, ts = backward_euler(F, u0, tmax, T)

plt.plot(ts, us[:, 0])
plt.plot(ts, us[:, 1])
plt.xlabel('Ось t')
plt.ylabel('Ось u')
plt.title('Неявный метод Эйлера для 2 задачи')
plt.show()
