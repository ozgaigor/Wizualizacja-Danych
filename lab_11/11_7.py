from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.gca(projection = '3d')

t = np.linspace(0 , 20)
z = t
x = np.sin(t)*10
y = np.cos(t)*10
ax.plot(x, y, z)
#------------------------------------------------------
np.random.seed( 8241677 )

def randrange(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin

n = 100

for c, m, zlow, zhigh in [('r', 'o', -13, 44),('pink', 'o', -5, 40)]:
    xs = randrange(n, -30, 30)
    zs = randrange(n, -10, 50)
    ax.scatter(xs, zs,c=c, marker=m)
plt.show()