# === INVENTARIO DE BILLETES ===
billetes_1000 = 10
billetes_500 = 10
billetes_200 = 10
billetes_100 = 10
billetes_50 = 10

print("\n=== Dispensadora de Billetes ===")

# === BUCLE PRINCIPAL ===
# este bucle se ejecutara hasta que el usuario decida salir
while True:

    # crear entrada para el cliente
    print("\nIngrese el monto a retirar (0 para salir): ")
    entrada = input()

    # === VALIDACION ===
    # Para que la entrada solo contenga numeros
    es_numero = True
    for numero in entrada:
        if numero < "0" or numero > "9":
            es_numero = False
            break

    # de esta forma controlamos si el usuario ingresa datos sin sentido
    if not es_numero or entrada == "":
        print("\nEntrada invalida. Por favor, ingrese solo números enteros positivos")
        continue

    # volvemos la entrada a integer ya que por defecto esta es de tipo string
    monto = int(entrada)

    # control para terminar la operacion
    if monto == 0:
        print("Gracias por usar la dispensadora. ¡Hasta pronto!")
        break

    # Inicializacion de las variables de entrega
    # estas variables almacenaran cuantos billetes se entregaran de cada tipo
    entregar_1000 = 0
    entregar_500 = 0
    entregar_200 = 0
    entregar_100 = 0
    entregar_50 = 0

    # esta variable se ira reduciendo conforme se le asignen billetes
    monto_restante = monto

    # === PROCESO DE ASIGNACION DE BILLETES ===
    # verificaremos para cada denominacion si se pueden utilizar billetes para
    # cubrir parte del monto o el monto total en su caso

    # Billetes de 1000
    if monto_restante >= 1000 and billetes_1000 > 0:
        # se crea una variable para almacenar los billetes que se necesitan
        cantidad = monto_restante // 1000
        # entregamos la cantidad de billetes disponibles en el inventario
        # conforme a lo que pida el usuario
        # si hacen falta mas billetes solo entregaremos los que esten dispobibles
        entregar_1000 = cantidad if cantidad <= billetes_1000 else billetes_1000
        # actualizamos el monto restante
        monto_restante -= entregar_1000 * 1000

    # Billetes de 500
    if monto_restante >= 500 and billetes_500 > 0:
        cantidad = monto_restante // 500
        entregar_500 = cantidad if cantidad <= billetes_500 else billetes_500
        monto_restante -= entregar_500 * 500

    # Billetes de 200
    if monto_restante >= 200 and billetes_200 > 0:
        cantidad = monto_restante // 200
        entregar_200 = cantidad if cantidad <= billetes_200 else billetes_200
        monto_restante -= entregar_200 * 200

    # Billetes de 100
    if monto_restante >= 100 and billetes_100 > 0:
        cantidad = monto_restante // 100
        entregar_100 = cantidad if cantidad <= billetes_100 else billetes_100
        monto_restante -= entregar_100 * 100

    # Billetes de 50
    if monto_restante >= 50 and billetes_50 > 0:
        cantidad = monto_restante // 50
        entregar_50 = cantidad if cantidad <= billetes_50 else billetes_50
        monto_restante -= entregar_50 * 50

    # actualizamos el inventario
    if monto_restante == 0:
        billetes_1000 -= entregar_1000
        billetes_500 -= entregar_500
        billetes_200 -= entregar_200
        billetes_100 -= entregar_100
        billetes_50 -= entregar_50

        # Mostrar la cantidad de billetes a entregar
        print("\nBilletes entregados:")
        if entregar_1000 > 0:
            print(f"1000 x {entregar_1000}")
        if entregar_500 > 0:
            print(f"500 x {entregar_500}")
        if entregar_200 > 0:
            print(f"200 x {entregar_200}")
        if entregar_100 > 0:
            print(f"100 x {entregar_100}")
        if entregar_50 > 0:
            print(f"50 x {entregar_50}")

    # si el monto restante supera la cantidad de billetes que se pueden entregar
    # se ejecutara esta porcion del codigo
    else:
        print("\nNo hay suficiente combinación de billetes para dispensar ese monto.")
