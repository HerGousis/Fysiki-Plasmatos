import numpy as np
import matplotlib.pyplot as plt

q = 1
m = 1
Bz = 4*pow(10,-2)
Ex = 2*pow(10,3)
Ey = 2*pow(10,3)

x0 = 0.0
y0 = 0.0
z0 = 0.0
vx0 = 2.0*pow(10,5)
vy0 = 2.0*pow(10,5)
vz0 = 2.0*pow(10,5)


dt = 0.01
timesteps = 50000
t = np.linspace(0, timesteps * dt, timesteps)


x_list = []
y_list = []
z_list = []
vx_list = []
vy_list = []
vz_list = []

for i in range(timesteps):
    x_list.append(x0)
    y_list.append(y0)
    z_list.append(z0)
    vx_list.append(vx0)
    vy_list.append(vy0)
    vz_list.append(vz0)


    ax = (q / m) * (Ex + vy0 * Bz)
    ay = (q / m) * (Ey-vx0*Bz)
    az =0


    vx0 = vx0 + ax * dt
    vy0 = vy0 + ay * dt
    vz0 = vz0 + az * dt
    x0 = x0 +  vx0 * dt
    y0 = y0 +  vy0 * dt
    z0 = z0 +  vz0 * dt

figure = plt.figure()
ax = figure.add_subplot(111, projection='3d')
ax.plot(x_list, y_list, z_list)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Κίνηση Φορτισμένου Σωματιδίου')
plt.show()
