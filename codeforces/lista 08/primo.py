def primo(n):
    for i in range(2, n+1):
        if (i == n):
            return True
        elif (n % i == 0):
            return False
        
n = int(input())

while True:
    n = n + 1
    if (primo(n)):
        print(n)
        break
