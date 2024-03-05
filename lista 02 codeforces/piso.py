L = int(input())
C = int(input())
Area = L * C
t1 = 0.5
t2 = t1 / 2
t3 = t2 / 2
lajotas_t1 = (Area - 4*t3) // t1
lajotas_t2 = ((Area - 4*t3) - lajotas_t1 * t1) // t2
print(int(lajotas_t1))
print(int(lajotas_t2))
