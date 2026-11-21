import matplotlib.pyplot as plt
import numpy as np


def f(x):
  return 3 * x - np.exp(x)


def df(x):
  return 3 - np.exp(x)


def biseccion(f, a, b, TOL=1e-12, N0=30):
  historia = []
  fa = f(a)
  for _ in range(N0):
    p = a + (b - a) / 2
    fp = f(p)
    historia.append(p)
    if fp == 0 or (b - a) / 2 < TOL:
      return p, historia
    if fa * fp > 0:
      a = p
      fa = fp
    else:
      b = p
  return historia[-1], historia


def newton_raphson(f, df, p0, TOL=1e-12, N0=50):
  historia = [p0]
  for _ in range(N0):
    d = df(p0)
    if d == 0:
      raise ZeroDivisionError("Tangente horizontal.")
    p = p0 - f(p0) / d
    historia.append(p)
    if abs(p - p0) < TOL:
      return p, historia
    p0 = p
  return p0, historia


def secante(f, p0, p1, TOL=1e-14, N0=50):
  historia = [p0, p1]
  q0, q1 = f(p0), f(p1)
  for _ in range(2, N0 + 1):
    if q1 == q0:
      raise ZeroDivisionError("Secante horizontal.")
    p = p1 - q1 * (p1 - p0) / (q1 - q0)
    historia.append(p)
    if abs(p - p1) < TOL:
      return p, historia
    p0, q0 = p1, q1
    p1, q1 = p, f(p)
  return p1, historia


p_ref, _ = secante(f, p0=1.0, p1=2.0, TOL=1e-14, N0=50)
_, hist_bis = biseccion(f, a=1.0, b=2.0, TOL=1e-16, N0=30)
_, hist_new = newton_raphson(f, df, p0=1.5, TOL=1e-15, N0=30)
_, hist_sec = secante(f, p0=1.0, p1=2.0, TOL=1e-15, N0=30)


def curva_error(historia, p_exacta, empezar_en=1):
  ns, errs = [], []
  for idx, pn in enumerate(historia):
    if idx < empezar_en:
      continue
    err = abs(pn - p_exacta)
    if err > 0:
      ns.append(idx)
      errs.append(err)
  return ns, errs


ns_bis, err_bis = curva_error(hist_bis, p_ref, empezar_en=0)
ns_bis = [n + 1 for n in ns_bis]
ns_new, err_new = curva_error(hist_new, p_ref, empezar_en=1)
ns_sec, err_sec = curva_error(hist_sec, p_ref, empezar_en=1)

ns_cota = np.arange(1, len(hist_bis) + 1)
cota_bis = (2.0 - 1.0) / (2.0**ns_cota)

plt.figure(figsize=(9, 5.5))
plt.semilogy(ns_bis, err_bis, "o-", label="Bisección $|p_n - p|$")
plt.semilogy(ns_new, err_new, "s-", label="Newton $|p_n - p|$")
plt.semilogy(ns_sec, err_sec, "^-", label="Secante $|p_n - p|$")
plt.semilogy(
    ns_cota, cota_bis, "--", color="gray", label="Cota bisección $(b-a)/2^n$"
)
plt.axhline(1e-8, color="red", linestyle=":", linewidth=1.3, label="$10^{-8}$")

plt.xlabel("Iteración $n$")
plt.ylabel("Error $|p_n - p|$ (escala log)")
plt.title("Convergencia en $3x - e^x = 0$ sobre $[1, 2]$")
plt.grid(True, which="both", alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()