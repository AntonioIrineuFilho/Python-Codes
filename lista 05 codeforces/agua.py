N = int(input())
if (N <= 10):
    print("7")
elif (N <= 30):
    C = ((N - 10) * 1) + 7
    print(C)
elif (N <= 100):
    C = ((N - 30) * 2) + 27
    print(C)
else:
    C = ((N - 100) * 5) + 167
    print(C)