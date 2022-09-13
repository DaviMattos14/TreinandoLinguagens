from ast import Pow
numero = int(input())
binario = int(0)
p = 0

while numero > 0:
    binario += ((numero % 2) * (pow(10,p)))
    numero = int((numero - (numero % 2))/2)
    p += 1
print(binario)
