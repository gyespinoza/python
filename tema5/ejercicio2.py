def numeroPrimo():
    numero = int(input("Escriba el numero a evaluar: "))

    if numero>1:
        for i in range(2, numero):
            if(numero % i) == 0:
                print(f"El {numero} no es primo")
                break
            else:
                print(f"El {numero} es primo")
    else:
        print(f"El {numero} no es primo")       

numeroPrimo()     