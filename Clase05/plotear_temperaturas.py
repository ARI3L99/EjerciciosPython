import numpy as np
def plotear_temperaturas():
    a = np.load("../Data/temperaturas.npy")
    return a

temperaturas = plotear_temperaturas()
import matplotlib.pyplot as plt
plt.hist(temperaturas,bins=50)
plt.show()
