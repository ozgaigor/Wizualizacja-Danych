# Wygeneruj wykres punktowy 
# dla 5 różnych losowych serii z użyciem różnych znaczników i kolorów: https://matplotlib.org/api/markers_api.html

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

np.random.seed( 8241 )

def randrange(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin


fig = plt.figure()
ax = fig.add_subplot(111 , projection = '3d')
n = 100

for c, m, zlow, zhigh in [('r', 'o', -50, -35), ( 'b', '^', -30, -5), ('g', '*', -5, 25), ( 'pink', 'X', 10, 20), ( 'y', '8', -6, 0)]:
    xs = randrange(n, 0, 10)
    ys = randrange(n, 0, 10)
    zs = randrange(n, zlow, zhigh)
    ax.scatter(xs, ys, zs, c=c, marker=m)

ax.set_xlabel('Oś X')
ax.set_ylabel('Oś Y')
ax.set_zlabel('Oś Z')
plt.show()