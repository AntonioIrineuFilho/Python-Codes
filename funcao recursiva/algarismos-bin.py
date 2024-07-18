def conta_bits(b):
    if (b < 1):
        return 0
    else:
        return 1 + conta_bits(b//10)

def binario(n):
    b = int(bin(n)[2:])
    return conta_bits(b)

print(binario(128564))


