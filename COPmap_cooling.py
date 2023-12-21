import matplotlib.pyplot as plt
import numpy as np
import matplotlib.tri as mtri
from mpl_toolkits.mplot3d import Axes3D
plt.style.use('ggplot')
plt.rcParams["axes.facecolor"] = 'white'
fig = plt.figure(figsize=plt.figaspect(0.5))

#make data
load = [10, 25, 50, 75, 100, 10, 25, 50, 75, 100, 10, 25, 50, 75, 100, 10, 25, 50, 75, 100, 10, 25, 50, 75, 100]
temp = [26, 26, 26, 26, 26, 29, 29, 29, 29, 29, 32, 32, 32, 32, 32, 35, 35, 35, 35, 35, 38, 38, 38, 38, 38]
cop = [5.22, 6.02, 6.43, 5.18, 5.10, 4.62, 5.45, 5.95, 4.77, 4.72, 4.32, 4.89, 5.31, 4.34, 4.30, 3.69, 4.36, 4.44, 3.90, 3.87, 3.57, 3.85, 3.75, 3.41, 3.31]

LOAD = np.array(load)
TEMP = np.array(temp)
COP = np.array(cop)

# Create the Triangulation; no triangles so Delaunay triangulation created.
triang = mtri.Triangulation(LOAD, TEMP)

# Plot the surface.
ax = fig.add_subplot(projection='3d')
cm = plt.cm.get_cmap('jet')
copmap = ax.plot_trisurf(LOAD, TEMP, COP, triangles=triang.triangles, cmap = cm)
fig.colorbar(copmap, ax = ax)
ax.set_xlabel("Load[%]", rotation = "horizontal")
ax.set_ylabel("Temperature[℃]", rotation = "horizontal")
ax.set_zlabel("COP[-]", rotation = "horizontal")
ax.set_xticks([10, 25, 50, 75, 100])
ax.set_yticks([26, 29, 32, 35, 38])


plt.show()
