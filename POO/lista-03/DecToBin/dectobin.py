class DecToBin:
    def __init__(self, num):
        self.setNum(num)
    def setNum(self, num):
        if (num < 0):
            raise ValueError("NEGATIVE VALUE NOT ALLOWED")
        else:
            self.num = num
    def getNum(self):
        return self.num
    def __str__(self):
        return f'Valor decimal = {self.num}'
    def Bin(self):
        n = self.num
        if (n == 0):
            binario = "0"
        else:
            l = []
            binarioInv = ""
            binario = ""
            while (n > 0):
                binarioInv = binarioInv + str((n % 2))
                n = n // 2
            for i in range(len(binarioInv)-1, -1, -1):
                binario = binario + binarioInv[i]
        return binario
