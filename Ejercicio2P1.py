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


def newton_raphson(f, df, p0, TOL=1e-6, N0=50):
  historia = [p0]
  i = 1
  while i <= N0:
    d = df(p0)
    if d == 0:
      raise ZeroDivisionError("La tangente es horizontal.")
    p = p0 - f(p0) / d
    historia.append(p)
    if abs(p - p0) < TOL:
      return p, historia
    p0 = p
    i += 1
  raise RuntimeError("No convergió.")


def P(x):
  return 230 * x**4 + 18 * x**3 + 9 * x**2 - 221 * x - 9


def dP(x):
  return 920 * x**3 + 54 * x**2 + 18 * x - 221


try:
  raiz_sec, hist_sec = secante(P, p0=0, p1=1, TOL=1e-6, N0=50)
  print("Secante -> raíz:", f"{raiz_sec:.6f}", "| pasos:", len(hist_sec) - 2)
  print("Historia secante:", hist_sec)
except Exception as e:
  print("Secante falló o lanzó error:", e)

try:
  raiz_new, hist_new = newton_raphson(P, dP, p0=0.5, TOL=1e-6, N0=50)
  print("Newton  -> raíz:", f"{raiz_new:.6f}", "| pasos:", len(hist_new) - 1)
  print("Historia newton:", hist_new)
except Exception as e:
  print("Newton falló o lanzó error:", e)

raiz_ok, hist_ok = newton_raphson(P, dP, p0=0.9, TOL=1e-6, N0=50)
print(
    "Arranque [0, 1] -> raíz:",
    f"{raiz_ok:.6f}",
    "| pasos:",
    len(hist_ok) - 1,
)
print("Historia arranque:", hist_ok)

xs = np.linspace(-0.2, 1.1, 400)
ys = P(xs)

plt.figure(figsize=(8, 5))
plt.plot(xs, ys, label="P(x)")
plt.axhline(0, color="black", linewidth=1)
plt.axvline(0, color="gray", linestyle="--", linewidth=0.8)
plt.axvline(1, color="gray", linestyle="--", linewidth=0.8)

pts_x = np.array(hist_ok)
plt.plot(pts_x, P(pts_x), "o--", color="red", label="Iteraciones (p0=0.9)")
for k, val in enumerate(pts_x):
  plt.annotate(
      f"p{k}",
      (val, P(val)),
      textcoords="offset points",
      xytext=(0, 8),
      ha="center",
  )

plt.xlim(-0.2, 1.1)
plt.ylim(-120, 60)
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()