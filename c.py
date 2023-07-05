# import numpy as np

# import cplot


# def f(z):
#     return (z + 2) / (3 * z + 4)
#     # return np.sin(z**3) / z


# plt = cplot.plot(
#     f,
#     (-2.0, +2.0, 400),
#     (-2.0, +2.0, 400),
# )
# plt.savefig("c.jpg")

import numpy as np
from mpl_toolkits.mplot3d import Axes3D  # don't move this
import matplotlib.pyplot as plt
from matplotlib import cm

def f(z):
    return ((z + 2) / (3 * z + 4)).real
    # return z.real ** 2 + z.imag

range_split = (-3.0, 3.0, 0.05)
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
X, Y = np.meshgrid(np.arange(*range_split), np.arange(*range_split))
z = np.asarray([x + eval(f"{y}j") for (x, y) in zip(np.ravel(X), np.ravel(Y))])
Z = f(z).reshape(X.shape)  # 1d to square

surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)
ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_zlabel("z")

plt.savefig("surface.jpg")