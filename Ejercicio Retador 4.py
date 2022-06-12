#EJERCICIO RETADOR 4

IDProducto = [1, 2, 3]
TipoProducto = ["MAIZ GRANO", "PEPINO", "TOMATE VERDE"]
CostoCaja = [285.55, 334.72, 129.0]

print(IDProducto)
print(TipoProducto)
print(CostoCaja)
print("")

ObtenerID = input("INGRESA EL ID DEL PRODUCTO: ")
ObtenerCajas = input("INGRESA EL NUMERO DE CAJAS A VENDER: ")
print("")

Total = CostoCaja[int(ObtenerID)-1] * int(ObtenerCajas)

if(int(ObtenerCajas) <=100):
  Total = Total + 1500
  print("SE TE AGREGARAN 1500 AL PRECIO ORIGINAL POR HABER COMPRADO MENOS DE 100 CAJAS")
  print("")
else:
  Total = Total

print("NOMBRE DEL PRODUCTO: " + TipoProducto[int(ObtenerID)-1])
print("PRECIO POR CAJA: " + str(CostoCaja[int(ObtenerID)-1]))
print("TOTAL A PAGAR: "+ str(Total))