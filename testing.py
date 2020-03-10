
import numpy as np


def signedToBinary(num, size):
    return np.binary_repr(int(num), width=size)



print(signedToBinary('-36', 16))