import math
M = [9000]
m = 127
W = 2050
p1 = 0.5
p2 = 1
step = 0
S = math.pi * (1.65 ** 2) * 0.25
while M[step] >= 0:
    P = W * m + S * (p1 - p2)
    M_new = M[step] - m
    M.append(M_new)
    step += 1
    print(M_new)