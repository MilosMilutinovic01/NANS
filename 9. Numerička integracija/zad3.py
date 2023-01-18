import numpy as np
import integrate_simpson as int

def f(x):
    return x**2

def g(x):
    return np.sqrt(x)

def func(x):
    return abs(f(x)-g(x))

I = int.integrate_simpson_no_plot(func,0,2,100)
print(I)