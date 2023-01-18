import numpy as np
import integrate_simpson as int

def f(x):
    return np.sin(x)

I = int.integrate_simpson_no_plot(f,0,3*np.pi/2,100)
print(I)