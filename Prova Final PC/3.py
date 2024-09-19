d = int(input())
a = list(map(int, input().split()))
m_de_d = []
for i in a:
    if (i % d == 0):
        m_de_d.append(i)

print(m_de_d)