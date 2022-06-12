#EJERCICIO RETADOR 2

ListaMunicipios = []
ListaHabitantes = []

#INGRESAR MUNICIPIOS
print("INGRESE 3 MUNICIPIOS")
print("")

NombreMunicipio = input("PRIMER MUNICIPIO: ")
ListaMunicipios.append(NombreMunicipio)
NumeroHabitantesMunicipio = input("HABITANTES DEL PRIMER MUNICIPIO: ")
ListaHabitantes.append(NumeroHabitantesMunicipio)
print("")

NombreMunicipio = input("SEGUNDO MUNICIPIO: ")
ListaMunicipios.append(NombreMunicipio)
NumeroHabitantesMunicipio = input("HABITANTES DEL SEGUNDO MUNICIPIO: ")
ListaHabitantes.append(NumeroHabitantesMunicipio)
print("")

NombreMunicipio = input("TERCER MUNICIPIO: ")
ListaMunicipios.append(NombreMunicipio)
NumeroHabitantesMunicipio = input("HABITANTES DEL TERCER MUNICIPIO: ")
ListaHabitantes.append(NumeroHabitantesMunicipio)
print("")

SumaHabitantes = int(ListaHabitantes[0]) + int(ListaHabitantes[1]) + int(ListaHabitantes[2])

PromedioHabitantes = SumaHabitantes/3

print("TOTAL DE HABITANTES: "), print(SumaHabitantes)

print("")

print ("PROMEDIO DE HABITANTES: "), print(PromedioHabitantes)