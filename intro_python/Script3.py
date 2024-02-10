import matplotlib.pyplot as plt
import numpy as np

def funcion(x):
    return x ** 2 + 3

x = np.linspace(-5, 5, 10)
y = funcion(x)

plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("x^2 + 3 ")
plt.grid(True)
plt.savefig('grafica.png')
