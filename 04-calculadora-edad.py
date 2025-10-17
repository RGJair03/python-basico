# Funcion principal
def calcular_edad():

    # Validacion de las entradas del usuario
    def es_entero(valor):

        # Verifica que la cadena no esté vacía
        if valor == "":
            return False

        # aqui validamos que la entrada contenga solo numeros enteros recorridendo cada carácter de la cadena
        for c in valor:
            # Si algún dato no es un dígito del 0 al 9, retornara False
            if c not in "0123456789":
                return False
        # Si todos los caracteres son válidos, retorna True
        return True

    # Diccionario que define cuántos días tiene cada mes
    dias_por_mes = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }

    # Ciclo principal para realizar los calculos de edad que se requieran
    while True:

        print("\n=== Captura de Fecha de Nacimiento ===")

        # Solicitamos al usuario la fecha de nacimiento en formato DD-MM-AAAA
        fecha_nacimiento = input(
            "\nIngrese su fecha de nacimiento en formato DD-MM-AAAA: "
        )

        # Valida que la cadena tenga exactamente 10 caracteres y guiones en las posiciones correctas
        # se ocupa len para contar la cantidad de datos que ingresara el usuario en este caso cuando ingrese las fechas
        if (
            len(fecha_nacimiento) != 10
            or fecha_nacimiento[2] != "-"
            or fecha_nacimiento[5] != "-"
        ):
            print(
                "\nError: El formato debe ser exactamente DD-MM-AAAA con los guiones en las posiciones correctas."
            )
            continue

        # Extrae manualmente las partes de la fecha usando índices
        dia_nacimiento_str = fecha_nacimiento[0] + fecha_nacimiento[1]
        mes_nacimiento_str = fecha_nacimiento[3] + fecha_nacimiento[4]
        anio_nacimiento_str = (
            fecha_nacimiento[6]
            + fecha_nacimiento[7]
            + fecha_nacimiento[8]
            + fecha_nacimiento[9]
        )

        # Se valida wue la entrada sea numerica utilizando la funcion es_entero(valor)
        if (
            not es_entero(dia_nacimiento_str)
            or not es_entero(mes_nacimiento_str)
            or not es_entero(anio_nacimiento_str)
        ):
            print("\nError: La fecha debe contener solo números en cada componente.")
            continue

        # Conviertimos las fechas de str a int
        dia_nacimiento = int(dia_nacimiento_str)
        mes_nacimiento = int(mes_nacimiento_str)
        anio_nacimiento = int(anio_nacimiento_str)

        # Valida que el mes esté en el rango establecido
        if mes_nacimiento < 1 or mes_nacimiento > 12:
            print("\nError: El mes debe estar entre 1 y 12.")
            continue

        # Valida que el día esté dentro del rango permitido para ese mes utilizando el diccionario creado anteriormente
        if dia_nacimiento < 1 or dia_nacimiento > dias_por_mes[mes_nacimiento]:
            print(f"\nError: El mes {mes_nacimiento} no tiene {dia_nacimiento} días.")
            continue

        # Valida que el año sea mayor a 1900)
        if anio_nacimiento <= 1900:
            print("\nError: El año debe ser mayor a 1900.")
            continue

        print("\n=== Captura de Fecha Actual ===")

        fecha_actual = input("Ingrese la fecha actual en formato DD-MM-AAAA: ")

        if len(fecha_actual) != 10 or fecha_actual[2] != "-" or fecha_actual[5] != "-":
            print(
                "\nError: El formato debe ser exactamente DD-MM-AAAA con guiones en las posiciones correctas."
            )
            continue

        dia_actual_str = fecha_actual[0] + fecha_actual[1]
        mes_actual_str = fecha_actual[3] + fecha_actual[4]
        anio_actual_str = (
            fecha_actual[6] + fecha_actual[7] + fecha_actual[8] + fecha_actual[9]
        )

        if (
            not es_entero(dia_actual_str)
            or not es_entero(mes_actual_str)
            or not es_entero(anio_actual_str)
        ):
            print(
                "\nError: La fecha actual debe contener solo números en cada componente."
            )
            continue

        dia_actual = int(dia_actual_str)
        mes_actual = int(mes_actual_str)
        anio_actual = int(anio_actual_str)

        if mes_actual < 1 or mes_actual > 12:
            print("\nError: El mes actual debe estar entre 1 y 12.")
            continue

        if dia_actual < 1 or dia_actual > dias_por_mes[mes_actual]:
            print(f"\nError: El mes actual {mes_actual} no tiene {dia_actual} días.")
            continue

        # Valida que el año actual no sea menor al año de nacimiento
        if anio_actual < anio_nacimiento:
            print("\nError: El año actual no puede ser menor al año de nacimiento.")
            continue

        # Verifica que la fecha de nacimiento no sea posterior a la fecha actual
        if (anio_nacimiento, mes_nacimiento, dia_nacimiento) > (
            anio_actual,
            mes_actual,
            dia_actual,
        ):
            print("\nError: El cliente aún no ha nacido.")
            continue

        # Cálculo de edad en años, meses y días
        edad_anios = anio_actual - anio_nacimiento
        edad_meses = mes_actual - mes_nacimiento
        edad_dias = dia_actual - dia_nacimiento

        # Ajuste si los días son negativos (no ha cumplido el día del mes)
        if edad_dias < 0:
            edad_meses -= 1
            # Se suma los días del mes anterior para compensar
            mes_anterior = mes_actual - 1 if mes_actual > 1 else 12
            edad_dias += dias_por_mes[mes_anterior]

        # Ajuste si los meses son negativos (no ha cumplido el mes)
        if edad_meses < 0:
            edad_anios -= 1
            edad_meses += 12

        # Muestra la edad en el formato más adecuado según el caso
        if edad_anios > 0:
            print(
                f"\nEdad del cliente: {edad_anios} año(s), {edad_meses} mese(s) y {edad_dias} día(s)"
            )

        elif edad_meses > 0:
            print(f"\nEdad del cliente: {edad_meses} mese(s) y {edad_dias} día(s)")

        else:
            print(f"\nEdad del cliente: {edad_dias} día(s)")

        # Pregunta si se desea realizar otra cotización
        continuar = input(
            "\n¿Desea realizar otra cotización? (s = sí ó cualquier otra/s tecla/s para salir): "
        )

        if continuar.lower() != "s":
            break


# Se llama a la función para iniciar el sistema
calcular_edad()
