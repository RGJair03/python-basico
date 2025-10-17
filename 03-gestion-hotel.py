# Se crea una funcion llamada hotel, aqui vamos hacer el
# sistema de las reservaciones del mismo
def hotel():

    # Usamos la estructura diccionario, donde se almacenan las
    # habitaciones de camas individuales y dobles disponibles
    habitaciones = {"individual": 3, "doble": 2}

    # usamos un while para dejar ciclo infinito, que nos permitira
    # usar las veces que queramos el sistema
    while True:

        # Declaramos una variable como entrada de valor, donde se
        # guardara el mismo
        accion = input("¿Reservar o liberar?")

        # Con la variante anterior se ocupara un match que nos permita
        # escoger una accion entre reservar o liberar
        match accion:
            case "reservar":

                # Para reservar pedimos que tipo de habitacion quiere
                # el cliente y se almacena en una variante
                print(" qué tipo de habitación quiere")
                tipo = input("Tipo: ")

                # Se ocupa un condicional if para preguntar si el tipo de
                # habitacion se encuentra en el diccionario " habitaciones " y
                # si la cantidad se mayor a 0
                if tipo in habitaciones and habitaciones[tipo] > 0:

                    # cuando se cumpla la condicion se le estara -1 a la cantidad
                    # del tipo de habitacion que se escogio y se manda mensaje que
                    # su habitacion fue reservada
                    habitaciones[tipo] -= 1
                    print(f"Habitacion {tipo} reservada")

                # si la condicion no se cumple manda este mensaje
                else:
                    print("No disponible")

            case "liberar":

                # Para liberar pedimos que tipo de habitacion quiere liberar
                # y se almacena en un variable
                print("Que tipo de habitación quiere")
                tipo = input("tipo: ")

                # cuando se cumpla la condicion se le suma 1 a la cantidad del tipo
                # de habitacion que se escogio y se manda mensaje que su habitacion
                # fue liberada
                if tipo in habitaciones:
                    habitaciones[tipo] += 1
                    print(f"Habitacion {tipo} liberada")

            # este codigo sirve para cerrar el sistema
            case "salir":
                break

            # este codigo sirve para que, cuando se coloca un dato que no
            # corresponda a los anteriores casos, mande un mensaje
            case _:
                print("Acción no reconocida")

        # imprime las habitaciones disponibles
        print("Estado:", habitaciones)


# se escribe el nombre de la funcion que se va a llamar a ejecutar
hotel()
