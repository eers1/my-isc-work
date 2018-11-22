import numpy as np


def total_wind(u, v):
    total = (u**2 + v**2)**(1/2)
    condition = np.less(total, 0.1)
    resultant = np.where(condition, 0.1, total)

    return resultant


u = np.array([[4, 5, 0.01], [2, 3, 4]])
v = np.array([[2, 2, 0.03], [1, 1, 1]])
new = total_wind(u, v)
print(new)
