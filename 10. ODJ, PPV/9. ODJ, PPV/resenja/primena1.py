import numpy as np
import matplotlib.pyplot as plt
import eulerN, rk4N



ns0T = 0
v0T = 0

F = 10
m = 1

#  s"(t) = a
#  s(0) = 0, s'(0) = 0
#  resenje: s(t) = v0.*t + F/m*0.5*t.^2

ddsT = lambda *args: F/m
# ddsT = lambda t, v: F/m

ns0T = np.array([ns0T, v0T])

ta = 0
tb = 10
h = (tb - ta)/10

t = np.arange(ta, tb+h, h)
f_true = np.dot(v0T,t) + F/m*0.5*np.power(t,2)
f_x_euler, sss = eulerN.eulerN(ta, tb, h, ns0T, ddsT, 0.0)
f_x_rk4, sss1 = rk4N.rk4N(ta, tb, h, ns0T, ddsT, 0.0)

print(f_true)
print(f_x_euler)
print(f_x_rk4)

plt.plot(t, f_true, 'green')
plt.plot(t, f_x_euler, 'blue')
plt.plot(t, f_x_rk4, 'red')
plt.show()