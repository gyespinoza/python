# numeros impares de un rango de numeros
numeroInicial = int(input("Escribe el valor inicial "))
numeroFinal = int(input("Escribe el valor final "))
resultado = []

for i in range(numeroInicial, numeroFinal):
    if(i % 2 != 0):
        resultado.append(i)

print(resultado)