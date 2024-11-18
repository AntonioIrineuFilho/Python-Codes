class Data:
    def __init__(self, data):
        self.setData(data)
    def setData(self, data):
        if (len(data) != 10):
            raise ValueError("INVALID DATE")
        dia = int(data[0:2])
        mes = int(data[3:5])
        ano = int(data[6:])
        if (ano < 0): raise ValueError("INVALID DATE")
        if (mes < 1 or mes > 12): raise ValueError("INVALID DATE")
        if ((ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0):
            if (mes == 2 and dia > 29): raise ValueError("INVALID DATE")
        elif (mes == 2 and dia > 28): raise ValueError("INVALID DATE")
        if (mes == 3 or mes == 5 or mes == 9 or mes == 11):
            if (dia > 30): raise ValueError("INVALID DATE")
        else:
            if (dia > 31): raise ValueError("INVALID DATE")
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano
    def getDia(self):
        return self.__dia
    def getMes(self):
        return self.__mes
    def getAno(self):
        return self.__ano
    def __str__(self):
        return f'Data = {self.__dia:02d}/{self.__mes:02d}/{self.__ano:04d}'
        