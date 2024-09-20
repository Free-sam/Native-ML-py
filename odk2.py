import numpy as np
import matplotlib.pyplot as plt
x = np.random.normal(1.0,5.0,10000)
plt.hist(x,100)
plt.show()