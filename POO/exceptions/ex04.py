dict = {"teste": 1234, "teste2": 5678}

try:
    print(dict["teste3"])
except KeyError:
    print("INVALID DICT KEY")

for key in dict.keys():
    print(key)