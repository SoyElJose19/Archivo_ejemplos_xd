import csv
def buscar_nom_largo(p_lista_nombres):
    for x in range(3):
        if x == 0:
            nombre_mas_largo = p_lista_nombres[0]
        else:
            if len(p_lista_nombres[x])>len(nombre_mas_largo):
                nombre_mas_largo=p_lista_nombres[x]
    print("El nombre mas largo es:",nombre_mas_largo)

def crear_csv_nombres  (p_lista_nombres):
    with open ("nombres.csv","w",newline="") as archivo:
        escritor =csv.writer(archivo)
        escritor.writerow(p_lista_nombres)