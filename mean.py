import numpy as np
import matplotlib

list = np.arange(0, 21)

mean  = np.mean(list)
std = np.std(list)
variance = np.var(list)

print(mean)
print(std)
print(variance)