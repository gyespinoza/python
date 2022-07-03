class Alumno:
    nombre = ""
    nota = 0
    
    # definir nombre y nota
    def setNombre(self, nombre):
        self.nombre = nombre
    def setNota(self, nota):
        self.nota = nota

    # obtener nombre y nota
    def getNombre(self):
        return self.nombre
    def getNota(self):
        return self.nota

    # calcular nota
    def resultado(self):
        if self.nota >= 7:
            print("El alumno aprobo")
        else:
            print("El alumno reprobo")

# utilizando clase
alumno1 = Alumno();
alumno1.setNombre("Jose Alfredo Gonzales");
alumno1.setNota(8)
print(alumno1.getNombre())
print(alumno1.getNota())
alumno1.resultado()

alumno2 = Alumno();
alumno2.setNombre("Fabio Lopez");
alumno2.setNota(6)
print(alumno2.getNombre())
print(alumno2.getNota())
alumno2.resultado()