import matplotlib.pyplot as plt
import numpy as np


def secante(f, p0, p1, TOL=1e-6, N0=50):
  historia = [p0, p1]
  q0, q1 = f(p0), f(p1)
  i = 2
  while i <= N0:
    if q1 == q0:
      raise ZeroDivisionError("La secante es horizontal.")
    p = p1 - q1 * (p1 - p0) / (q1 - q0)
    historia.append(p)
    if abs(p - p1) < TOL:
      return p, historia
    p0, q0 = p1, q1
    p1, q1 = p, f(p)
    i += 1
  raise RuntimeError("No convergió.")


def f(x):
  return np.log(x**2 + 1) - np.exp(0.4 * x) * np.cos(np.pi * x)


# Gráfica en [-1, 5]
xs = np.linspace(-1, 5, 600)
plt.figure(figsize=(8, 4.5))
plt.plot(xs, f(xs), label="f(x)")
plt.axhline(0, color="black", linewidth=1)
plt.xlim(-1, 5)
plt.ylim(-10, 10)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("f(x) en [-1, 5]")
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()

# 25.º cero positivo (n = 25 -> cerca de 24.5)
raiz_25, hist_25 = secante(f, p0=24.49, p1=24.51, TOL=1e-6)
print(f"25.º cero positivo: {raiz_25:.6f}")