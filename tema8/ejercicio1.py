file = open('archivo.txt', 'w')
file.write('Archivo txt!\n')
file.close()

file = open('archivo.txt', 'r+')
file.readline()
file.write('Segunda línea.\n')

file.seek(0)
print(file.read())
file.close()