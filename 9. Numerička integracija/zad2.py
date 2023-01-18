import numpy as np
import integrate_simpson as int

def f(x):
    return np.exp(-x**2/2)

I = int.integrate_simpson_no_plot(f,0,0.2,100)
print(2/np.sqrt(2*np.pi)*I)