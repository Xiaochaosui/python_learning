import numpy as np

a = np.array([(range(pow(2,8)))], dtype=np.uint8)
b = np.unpackbits(a.T, axis=1)

print("a", a)
print("b", b)

import matplotlib.pyplot as plt

