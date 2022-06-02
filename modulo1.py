def ingresar_pasajeros (pasajeros):
  nombre = input('Escriba nombre pasajero o escriba X para finalizar. ')
  while nombre != "X":
    cc = int(input('Escriba cédula del pasajero: '))
    destino = input('Escriba destino: ')
    pasajeros.append ((nombre, cc, destino))
    nombre = input('Escriba nombre pasajero o escriba X para finalizar. ')
  return pasajeros