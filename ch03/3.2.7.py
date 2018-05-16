import numpy as np
import matplotlib.pylab as plt

from relu import relu

x = np.arange(-1.0, 1.0, 0.1)
y = relu(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()
