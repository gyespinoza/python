import math

def areaTriangulo(altura, base):
    return ((altura*base)/2)


def areaCirculo(radio):
    return(math.pi*(radio*2))


altura = float(input("Altura del triangulo? "))
base = float(input("Base del triangulo? "))


radio = float(input("Cual es el radio del circulo? "))

print(f"Area del triangulo: {areaTriangulo(altura, base)}")
print(f"Area del circulo: {areaCirculo(radio)}")
