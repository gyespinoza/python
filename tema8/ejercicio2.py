from pickle import *

class Vehiculo:
    def __init__(self, color, marca):
        self.color = color
        self.marca = marca

    def __str__(self):
        return self.color + " " + self.marca


toyota = Vehiculo("Rojo", "Toyota")
print(toyota)

file = open('vehiculoFile', 'w+b')

dump(toyota, file)

file.seek(0)
nVehiculo = load(file)

print(nVehiculo)
file.close()