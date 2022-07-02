peso = input("Escriba su peso en kg? ")
estatura = input("Cual es su estatura en mt? ")
imc = round(float(peso)/float(estatura)*2,2)
print("Tu índice de masa corporal es " + str(imc))