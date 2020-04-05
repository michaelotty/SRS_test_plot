#!/usr/bin/python

from SRS import SRS
import numpy as np


f0 = 600.0
fs = 9600.0
T = 2  # s
a = SRS([np.sin(2*np.pi*f0*t) for t in np.linspace(0, T, round(fs/T))], fs)

