import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))



def step_function(x):
    return np.array(x > 0, dtype=np.int)


x = np.arange(-5.0,5.0,0.1)
y = sigmoid(x)
t = step_function(x)
plt.plot(x, y)
plt.plot(x, t)
plt.ylim(-0.1,1.1)
plt.show()
