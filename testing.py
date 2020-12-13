import math
import matplotlib.pyplot as plt

S_middle = math.pi * (0.1 ** 2)
S_sopla = math.pi * (1.65 ** 2) * 0.25
g = 9.81
Massa = [12500]
m = 127
p_S = 0.5
p_Atm = 1
W = 2050
C = 1
dt = 0.1
speed = [0]
teta = [90]
dist = [0]
height = [0]
step = 0
density = [1.225 * math.exp(-1 * height[0] / 10000)]
P = W * m + S_sopla * (p_S - p_Atm)

while height[step] >= 0 and  Massa[step] >= 3500:
    forceAero = -0.5 * C * S_middle * density[step] * (speed[step] ** 2)
    forceG = -g * Massa[step] * math.sin(teta[step])
    density_new = 1.225 * math.exp(-1 * height[step] / 10000)
    M_new = Massa[step] - m * dt
    speed_new = speed[step] + (forceG + forceAero + P) / Massa[step] * dt
    if speed[step] == 0:
        teta_new = 0
    else:
        teta_new = teta[step] - (-g * Massa[step] * math.cos(teta[step])) / (Massa[step] * speed[step]) * dt
    dist_new = dist[step] + speed[step] * dt * math.sin(teta[step])
    height_new = height[step] + speed[step] * dt * math.cos(teta[step])
    dist.append(dist_new)
    Massa.append(M_new)
    height.append(height_new)
    speed.append(speed_new)
    teta.append(teta_new)
    density.append(density_new)
    step += 1
def create_plot(title, xl, yl, x, y):
    plt.title(title)
    plt.xlabel(xl)
    plt.ylabel(yl)
    plt.grid()
    plt.plot(x, y)
    plt.show()
create_plot("Эйлер", "Дальность (м)", "Высота (м)", height, dist)