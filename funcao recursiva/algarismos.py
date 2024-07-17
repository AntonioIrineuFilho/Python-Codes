def conta_algarismos(n):
    if (n < 1):
        return 0
    else:
        return 1 + conta_algarismos(n//10)

print(conta_algarismos(12345))