a, b, c = map(int, input().split())

# Please write your code here.

d = a - 11
h = b - 11
m = c - 11

if m < 0:
    h -= 1
    m += 60

if h < 0:
    d -= 1
    h += 24

if d < 0:
    print(-1)
else:
    print(d * 24 * 60 + h * 60 + m)