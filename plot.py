from SRS import SRS
import numpy as np


f0 = 100
fs = 10e3
T = 2  # s
a = SRS([np.sin(2*np.pi*f0*t) for t in np.linspace(0, T, round(fs/T))], fs)

