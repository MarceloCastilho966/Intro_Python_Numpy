import numpy as np
km = np.loadtxt('/home/marcelo/Downloads/Numpy/data/carros-km.txt')
anos = np.loadtxt(
    '/home/marcelo/Downloads/Numpy/data/carros-anos.txt', dtype=int)

km_media = km / (2019 - anos)
print(km_media)
