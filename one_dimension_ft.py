import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt

f = 1 # frequency
t = np.arange(0, 5, 0.0001)
y = np.sin(2 * np.pi * f * t)

freq = np.linspace(0, 5.0, 2**20)

y_ft = fft(y)

plt.figure(2)
plt.subplot(2, 1, 1)
plt.plot(t, y)
plt.xlim(0, 6)
plt.xlabel("time")
plt.ylabel("amplitude")

plt.subplot(2, 1, 2)
plt.plot(freq, np.abs(y_ft))
plt.xlabel("frequency")
plt.ylabel("amplitude")
plt.show()