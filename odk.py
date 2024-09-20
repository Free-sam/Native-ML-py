#lets take 250 random floats under 0 to 5 that showing in histogramme#
import numpy as np
import matplotlib.pyplot as plt

x = np.random.uniform(0.0,5.0,250)
plt.hist(x,100)
plt.show()