import numpy as np
from scipy import stats

speed = [12,55,39,233,52,23,44,68]

x = np.median(speed)
y = stats.mode(speed)
p = np.std(speed)
z = np.var(speed)

print(f'the value will  be :-> {x} and {y}')

print(f'the value of standard deviation is : {p} and the variance will be : {z}')

