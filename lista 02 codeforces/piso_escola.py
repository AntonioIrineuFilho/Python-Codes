L = int(input())
C = int(input())
Area = L * C
t1 = 0.5
t2 = t1 / 2
t3 = t2 / 2
lajolas_t1 = (Area - 4*t3) // t1
lajolas_t2 = ((Area - 4*t3) - lajolas_t1 * t1) // t2
print(int(lajolas_t1))
print(int(lajolas_t2))

