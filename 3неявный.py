import numpy as np
import matplotlib.pyplot as plt
import math

a = 1
ei_dop = 10e-3
t0 = 0
T = 1
u0 = [1, 1, 1]
tmax = 0.01


def F(t, u):
    u1, u2, u3 = u
    k = 3
    a = 1
    r = [
        (k - a) / a * u2 * u3,
        (a + k) / k * u1 * u3,
        (a - k) / a * u1 * u2
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
        print(f"t = {t[n + 1]:.6f}, u1 = {u[n + 1, 0]:.6f}, u2 = {u[n + 1, 1]:.6f}, u3 = {u[n + 1, 2]:.6f}")

    return u, t


us, ts = backward_euler(F, u0, tmax, T)

plt.plot(ts, us[:, 0], label='u1')
plt.plot(ts, us[:, 1], label='u2')
plt.plot(ts, us[:, 2], label='u3')
plt.xlabel('Ось t')
plt.ylabel('Ось u')
plt.title('Неявный метод Эйлера для 3 задачи')
plt.show()
