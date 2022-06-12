SuperficieSinaloa = 57365

Clima = ["CALIDO", "SUBHUMEDO", "SECO", "SEMISECO"]
TemperaturaMA = "25.45"

PrecipitacionAP = 790.1

#NUMERO DE PERSONAS
PoblacionM = 1532128
PoblacionH = 1494815

#PORCENTAJE DE PERSONAS
PorcentajeM = 16.57
PorcentajeC = 33.15

#NUEVAS VARIABLES
PoblacionT = PoblacionH + PoblacionM

PorcentajeT = PorcentajeC + PorcentajeM

TemperaturaMATC = TemperaturaMA + " GRADOS. LOS TIPOS DE CLIMAS SON: "+ Clima[0] +", " +Clima[1] +", "+ Clima[2] +", "+ Clima[3]

print("LA POBLACION TOTAL ES: ")
print(PoblacionT)
print("PORCENTAJE POBLACION CULIACAN Y MAZATLAN: ")
print(PorcentajeT)
print("TEMPERATURA MEDIA ANUAL: ")
print(TemperaturaMATC)