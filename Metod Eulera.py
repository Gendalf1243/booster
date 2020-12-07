import math
import matplotlib.pyplot as plt
S = math.pi * (0.1 ** 2)
g = 9.81
m = 85
C = 1
dt = 0.0001
speed = [85]
teta = [45]
dist = [0]
height = [0]
step = 0
time = [0]
density = [1.225 * math.exp(-1 * height[0] / 10000)]
while height[step] >= 0:
    forceAero = -0.5 * C * S * density[step] * (speed[step] ** 2)
    forceG = -g * m * math.sin(teta[step])
    density_new = 1.225 * math.exp(-1 * height[step] / 10000)
    speed_new = speed[step] + (forceG + forceAero) / m * dt
    teta_new = teta[step] + (-g * m * math.cos(teta[step]))/(m * speed[step]) * dt
    dist_new = dist[step] + speed[step] * dt * math.cos(teta[step])
    height_new = height[step] + speed[step] * dt * math.sin(teta[step])
    dist.append(dist_new)
    height.append(height_new)
    speed.append(speed_new)
    teta.append(teta_new)
    density.append(density_new)
    time.append(time[step]+dt)
    step += 1
def create_plot(title, xl, yl, x, y):
    plt.title(title)
    plt.xlabel(xl)
    plt.ylabel(yl)
    plt.grid()
    plt.plot(x, y)
    plt.show()
create_plot("Эйлер", "Дальность (м)", "Высота (м)", dist, height)

