#EJERCICIO RETADOR 3

PesoCemento = input("INGRESA EL PESO DEL COSTAL DE CEMENTO: ")
PesoYeso = input("INGRESA EL PESO DEL COSTAL DE YESO: ")
print("")

CostalesCemento = input("¿CUANTOS COSTALES DE CEMENTO SON?: ")
CostalesYeso = input("¿CUANTOS COSTALES DE YESO SON?: ")
print("")

Peso_Total = ((int(PesoCemento) * int(CostalesCemento)) + (int(PesoYeso) * int(CostalesYeso)))

print ("EL PESO TOTAL EN KG: " + str(Peso_Total))

if(Peso_Total >= 3254/2 and Peso_Total <= 3254):
  print("EL ENVIO SI SE PUEDE ENVIAR")
else:
  print("EL ENVIO NO SE PUEDE ENVIAR")