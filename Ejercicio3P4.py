import numpy as np
from scipy.optimize import newton

raiz, info = newton(
    np.exp, 0, fprime=np.exp, maxiter=1000, full_output=True
)  #
print(raiz, info.converged, np.exp(raiz))  #