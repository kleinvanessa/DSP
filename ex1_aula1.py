# -*- coding: utf-8 -*-
"""
Aula 1

13/03/2020
"""


import matplotlib.pyplot as plt
import numpy as np

n=np.arange(0,40)


x=np.cos(np.pi/4*n)
plt.stem(n,x)
plt.show()