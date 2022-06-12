#EJERCICIO INTEGRADOR

VentaP = [ [2, 122], [1, 89], [1, 22], [3, 48], [1, 75], [3, 322], [2, 95], [1, 148], [1, 83], [3, 100]]

IDProducto = [1, 2, 3]
TipoProducto = ["Maiz grano", "Pepino", "Tomate verde"]
CostoCaja = [285.55, 334.72, 129.0]

print(IDProducto)
print(TipoProducto)
print(CostoCaja)
print("")

ObtenerID = input("INGRESA EL ID DEL PRODUCTO: ")
NumeroCajas = input("INGRESA EL NUMERO DE CAJAS A VENDER: ")
print("")

Total = CostoCaja[int(ObtenerID)-1] * int(NumeroCajas)

VentaP.append([int(ObtenerID), int(NumeroCajas)])

TamañoLista = len(VentaP)

x = 0
T = 0

while x < TamañoLista:
  T = (VentaP[x][1]) + (T)
  x +=1

SumaCaja = VentaP[0][1]

if(int(NumeroCajas) <= 100):
  Total = Total + 1500
  print("SE TE AGREGARAN 1500 AL PRECIO ORIGINAL POR HABER COMPRADO MENOS DE 100 CAJAS O HABER COMPRADO 100")
  print("")
else:
  Total = Total

if(T>1500):
  Descuento = (Total*20)/100
else:
  Descuento = 0

Total = Total - Descuento

print("NOMBRE DEL PRODUCTO: " + TipoProducto[int(ObtenerID)-1])
print("PRECIO POR CAJA: $" + str(CostoCaja[int(ObtenerID)-1]))

if(T>1500):
  print("LA SUMA DE LAS CAJAS SI SON SUFICIENTES PARA APLICARTE EL 20% DE DESCUENTO")
  print("SE TE DESCONTARON $" + str(Descuento) + " DE TU PRECIO TOTAL")
else:
  print("LA SUMA DE LAS CAJAS NO SON SUFICIENTES PARA APLICARTE EL 20% DE DESCUENTO")

print("TOTAL A PAGAR: $"+ str(Total))