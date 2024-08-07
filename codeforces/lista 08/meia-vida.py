s, m = map(int, input().split())
t = 0
while True:
    if (m < 0.5):
        break
    m = m / 2
    t = t + s

d = t // 86400
h = (t % 86400) // 3600
m = ((t % 86400) % 3600) // 60
s = ((t % 86400) % 3600) % 60

print(f'{d} dias {h:02d}:{m:02d}:{s:02d}')