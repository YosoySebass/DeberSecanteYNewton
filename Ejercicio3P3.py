import matplotlib.pyplot as plt
import numpy as np


def s(t):
  return 1.2 * np.exp(-t / 2) + np.exp(-t / 2) * np.cos(2 * t)


def s_escalada(t):
  return 1.2 + np.cos(2 * t)


ts = np.linspace(0, 12, 600)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.5))

# Izquierda: s(t) en [0, 12]
ax1.plot(ts, s(ts), color="tab:blue", linewidth=2, label="$s(t)$")
ax1.axhline(0, color="black", linewidth=1)
ax1.set_xlim(0, 12)
ax1.set_xlabel("t")
ax1.set_ylabel("s(t)")
ax1.set_title("Señal amortiguada $s(t)$")
ax1.grid(True, alpha=0.3)
ax1.legend()

# Derecha: s(t) * exp(t/2) = 1.2 + cos(2t) con recta y = 0.2
ax2.plot(
    ts,
    s_escalada(ts),
    color="tab:orange",
    linewidth=2,
    label="$s(t)e^{t/2} = 1.2 + \\cos(2t)$",
)
ax2.axhline(0.2, color="red", linestyle="--", linewidth=1.3, label="$y = 0.2$")
ax2.set_xlim(0, 12)
ax2.set_ylim(0, 2.4)
ax2.set_xlabel("t")
ax2.set_ylabel("$s(t)e^{t/2}$")
ax2.set_title("Señal sin amortiguar y cota inferior $y = 0.2$")
ax2.grid(True, alpha=0.3)
ax2.legend()

plt.tight_layout()
plt.show()