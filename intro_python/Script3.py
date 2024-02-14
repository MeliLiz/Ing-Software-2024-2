import matplotlib.pyplot as plt
import numpy as np


x = np.arange(-5,5,0.1)
y = x**3 + 5

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('x**3 + 5')
plt.show()
