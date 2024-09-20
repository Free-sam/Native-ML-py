from scipy import stats
import numpy as np

t = [34, 66, 42, 57, 52, 123, 564, 224, 679, 224]

x = stats.mode(t)
y = np.mean(t)
z = np.percentile(t,50)
print(z)
print(x)
print(y)
