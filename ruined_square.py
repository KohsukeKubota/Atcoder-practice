import math


x1, y1, x2, y2 = map(int, input().split())

x3 = x2
x4 = x1

dist = math.sqrt((x2-x1)**2)

y4 = y1 - dist
y3 = y4

print('{} {} {} {}'.format(x3, y3, x4, y4))

