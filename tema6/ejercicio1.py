class Vehiculo():
    color = ""
    ruedas = 0
    puertas = 0

    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
    def getColor(self):
        return self.color
    def getRuedas(self):
        return self.ruedas
    def getPuertas(self):
        return self.puertas
    
class Coche(Vehiculo):
    velocidad = 0
    cilindrada = 0

    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def getVelocidad(self):
        return self.velocidad
    def getCilindrada(self):
        return self.cilindrada

coche = Coche("Negro", 4, 4, 100, 1000);
print("Color: ", coche.getColor())
print("Puertas: ", coche.getPuertas())
print("Ruedas: ", coche.getRuedas())
print("Velocidad: ", coche.getVelocidad())
print("Cilindrada: ", coche.getCilindrada())
