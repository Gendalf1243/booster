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
# m = int(input())
# n = 5
# a = 0
# while m > 0:
#     d = m % n
#     if d % 2 == 1:
#         a += 1
#     m = m // n
# print(a)
m = int(input())
n = 14
a = 0
while m > 0:
    d = m % n
    if d > 9:
        a += 1
    m = m // n
print(a)