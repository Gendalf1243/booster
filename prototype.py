# m = int(input())
# n = int(input())
# t = 1
# a = 0
# max = -1
# while m > 0:
#     b = m % n
#     a += b * t
#     t = t * 10
#     m = m // n
#     if b % 10 > max:
#      max = b
# print(max)
m = int(input())
n = 2
t = 1
a = 0
c = 0
d = 0
while m > 0:
    b = m % n
    a += b * t
    t = t * 10
    m = m // n
    if b == 1:
        c +=1
    else:
        d += 1
print(c)
print(d)