import csv
personas = []
for x in range(3):
    persona =  []
    nombre = input("Ingrese Nombre: ")
    apellido = input("Ingrese Apellido: ")
    persona.append(nombre)
    persona.append(apellido)
    personas.append(persona)
with open ("nombres_y_apellidos.csv","w",newline="")as archivo:
    escritor =csv.writer(archivo)
    escritor.writerows(personas)