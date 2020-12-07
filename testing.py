# import math
#
#
# S_middle = math.pi * (0.1 ** 2)
# S_sopla = math.pi * (1.65 ** 2) * 0.25
# g = 9.81
# M_start = 3500
# M_fuel = [9000]
# m = 127
# p_S = 0.5
# p_Atm = 1
# W = 2050
# C = 1
# dt = 0.0001
# speed = [1]
# teta = [0]
# dist = [0]
# height = [0]
# step = 0
# density = [1.225 * math.exp(-1 * height[0] / 10000)]
#
# while height[step] >= 0 and  M_fuel[step] >= 0:
#     forceAero = -0.5 * C * S_middle * density[step] * (speed[step] ** 2)
#     forceG = -g * (M_start + M_fuel[step]) * math.sin(teta[step])
#     density_new = 1.225 * math.exp(-1 * height[step] / 10000)
#     P = W * (M_start + M_fuel[step]) + S_sopla * (p_S - p_Atm)
#     M_new = M_fuel[step] - m
#     speed_new = speed[step] + (forceG + forceAero + P) / (M_start + M_fuel[step]) * dt
#     teta_new = teta[step] + (-g * (M_start + M_fuel[step]) * math.cos(teta[step])) / ((M_start + M_fuel[step]) * speed[step]) * dt
#     dist_new = dist[step] + speed[step] * dt * math.cos(teta[step])
#     height_new = height[step] + speed[step] * dt * math.sin(teta[step])
#     dist.append(dist_new)
#     M_fuel.append(M_new)
#     height.append(height_new)
#     speed.append(speed_new)
#     teta.append(teta_new)
#     density.append(density_new)
#     step += 1
#     print(speed_new)
a = int(input())
max = -1
while a > 0:
    if a % 10 > max and (a % 10) % 3  == 0:
        max = a % 10
    a = a // 10
if max == -1:
    print('Таких цифр нет')
else:
    print(max)