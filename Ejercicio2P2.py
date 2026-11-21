import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import brentq


# Definición del polinomio
def P(x):
  return 230 * x**4 + 18 * x**3 + 9 * x**2 - 221 * x - 9


# Método de la secante
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


# Obtener las aproximaciones p0, p1, p2, p3, p4
_, hist_sec = secante(P, p0=0, p1=1, TOL=1e-6, N0=50)
p_0_a_4 = hist_sec[:5]

# Obtener los dos ceros reales
cero_1 = brentq(P, -1.0, 0.0)
cero_2 = brentq(P, 0.0, 1.0)

# Malla para graficar la curva
xs = np.linspace(-1.4, 1.1, 600)
ys = P(xs)

plt.figure(figsize=(10, 6))
plt.plot(xs, ys, color="tab:blue", linewidth=2, label="$P(x)$")
plt.axhline(0, color="black", linewidth=1)

# 1. Marcar los dos ceros reales
ceros_x = [cero_1, cero_2]
plt.scatter(
    ceros_x,
    [0, 0],
    color="green",
    s=75,
    zorder=5,
    label="Ceros reales de $P$",
)
plt.annotate(
    f"Cero 1 ≈ {cero_1:.4f}",
    (cero_1, 0),
    textcoords="offset points",
    xytext=(-45, -18),
    ha="center",
    fontsize=9,
    color="green",
    fontweight="bold",
)
plt.annotate(
    f"Cero 2 ≈ {cero_2:.4f}",
    (cero_2, 0),
    textcoords="offset points",
    xytext=(35, -18),
    ha="center",
    fontsize=9,
    color="green",
    fontweight="bold",
)

# 2. Marcar y numerar p0 a p4 de la secante
pts_x = np.array(p_0_a_4)
pts_y = P(pts_x)
plt.plot(
    pts_x,
    pts_y,
    "o--",
    color="tab:red",
    markersize=7,
    zorder=4,
    label="Secante ($p_0$ a $p_4$)",
)

# Desplazamientos personalizados para evitar que los textos se traslapen
offsets = [
    (28, -12),  # p0 = 0
    (-28, 12),  # p1 = 1
    (38, 10),  # p2 ≈ -0.34
    (42, -12),  # p3 ≈ -0.17
    (45, 5),  # p4 ≈ -1.29
]

for k, (xk, yk) in enumerate(zip(pts_x, pts_y)):
  plt.annotate(
      f"$p_{k}$ ({xk:.2f})",
      (xk, yk),
      textcoords="offset points",
      xytext=offsets[k],
      ha="center",
      fontsize=9,
      color="tab:red",
      fontweight="bold",
  )

# Configuración de ejes y títulos según rúbrica
plt.xlim(-1.4, 1.1)
plt.ylim(-130, 160)
plt.xlabel("x", fontsize=11)
plt.ylabel("P(x)", fontsize=11)
plt.title(
    "Polinomio $P(x)$ en $[-1.4, 1.1]$ y aproximaciones de la secante"
    " ($p_0=0, p_1=1$)",
    fontsize=12,
)
plt.grid(True, alpha=0.3)
plt.legend(loc="upper center")
plt.tight_layout()

# Guardar imagen en alta calidad para subir a la plataforma
plt.savefig("grafica_polinomio_secante.png", dpi=200)
plt.show()