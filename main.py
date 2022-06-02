'''Escribir un programa que permita procesar datos de pasajeros de viajes en tren en una lista de tuplas con la siguiente forma: (nombre, identificación, destino) Ejemplo: [("Manuel Suarez", 989092, "Liverpool"), 
("Silvia Paredes", 1342134, "Buenos Aires"), 
("Rosa Ortiz", 5877373, "Glasgow"), 
("Luciana Hernandez", 4533234, "Lisboa")]

Ademas, en otra lista de tuplas se almancenan los datos de cada ciudad y el pais al que pertenecen. Ejemplo:
[("Buenos Aires", "Argentina"),
("Glasgow", ("Escocia"),
("Lisboa", "Portugal")]

Hacer un menu interativo que permita al usuario realizar las siguientes operaciones:

- Agregar pasajeros a la lista de viajeros
- Agregar ciudades a la lista de ciudades
- Dado la identificación de un pasajero, ver a que ciudad viaja
- Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad.
- Dada la identificación de un pasajero, ver a que pais viaja.
- Dado un pais, mostrar cuantos pasajeron viajan a ese pais-
-Salir del programa'''

pasajeros = []
ciudades = []
import modulo1

while True:
  opc = int(input('¿Que desea hacer?\n1.Agregar pasajeros a la lista de viajeros.\n2.Agregar ciudades a lista de ciudades.\n3.Buscar ciudad por identificación.\n4.Mostrar pasajeros que van a una ciudad.\n5.Buscar pais destino mediante identificación.\n6.Cantidad de pasajeros que viajan a un país.\n7.Salir \nSeleccione su opción: '))
  if opc == 1:
    pasajeros = modulo1.ingresar_pasajeros (pasajeros)
  print (pasajeros)
  
#elif opc==2:

#elif opc==3:

#elif opc==4:

#elif opc==5:

#elif opc==6:

#elif opc==7:
  break
else:
  print('Opción no valida')