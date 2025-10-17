def evaluar_alumnos():

    # Se define una funcion interna para validar que el nombre solo contenga letras y espacios
    def nombre_valido(texto):

        # Se definen los caracteres permitidos: letras mayusculas, minusculas y espacios
        letras = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ "

        # Validamos que el texto no este vacio
        if texto == "":
            return False

        # Recorre cada caracter del texto
        for caracter in texto:

            # Si el caracter no esta en la lista de letras permitidas, retorna False
            if caracter not in letras:
                return False

        # Si todos los caracteres son validos, retorna True
        return True

    # Se define una funcion para verificar si un texto representa un numero entero positivo
    def es_entero_positivo(texto):

        # validamos que la entrada no puede estar vacia
        if texto == "":
            return False

        # recorremos caracter por caracter
        for caracter in texto:

            # aqui validamos que el caracter sea un digito entre 0 y 9
            # si se encuentra otro valor este retornara falso
            if caracter < "0" or caracter > "9":
                return False

        # convertimos el texto a int y se verifica que este sea mayor a 0
        if int(texto) <= 0:
            return False

        # si pasa todas las validaciones retornara como verdadero
        return True

    # Se define una funcion para verificar si un texto representa una calificacion
    # valida entre 1 y 10 y que no se repita un punto
    def es_calificacion_valida(texto):

        if texto == "":
            return False

        # variable para detectar si ya se encontro un punto decimal
        punto_encontrado = False

        for caracter in texto:

            # verifica si el caracter es un punto
            if caracter == ".":

                # aqui comprueba si el punto fue encontrado antes
                # si es asi entonces retorna false ya que no puede
                # ser valida una calificacion por ejemplo de 3.3.3
                if punto_encontrado:
                    return False

                # aqui valida que la calificacion si puede contener un punto
                punto_encontrado = True

            # validamos que el caracter sea un numero
            elif caracter < "0" or caracter > "9":
                return False

        # convertimos el valor a un dato de tipo float para aceptar decimales
        valor = float(texto)

        # si este valor es menor a 1 o mayor a 10 sera invalidado
        if valor < 1 or valor > 10:
            return False

        # si pasa las validaciones entonces retornara como verdadero
        return True

    # ciclo para validar correctamente
    # la cantidad de alumnos que se evaluaran
    while True:

        print("\n === EVALUADOR DE ALUMNOS PRO ===")

        # primera consideracion para sacar promedios
        num_alumnos = input("\nCuantos alumnos desea evaluar?: ")

        # Verifica que la entrada sea un numero entero positivo
        if es_entero_positivo(num_alumnos):
            # rompera el ciclo si es valido el dato ingreasado
            # volveremos a un numero entero el numero de alumnos
            num_alumnos = int(num_alumnos)
            break

        # en caso de que se ingrese mal el dato se repetira siempre
        else:
            print("\nError: Ingrese un numero positivo de alumnos.")

    # Solicitaremos al usuario el numero de evaluaciones
    while True:

        num_evaluaciones = input("Ingresa la cantidad de evaluaciones: ")

        # Verifica que la entrada sea un numero entero positivo
        if es_entero_positivo(num_evaluaciones):

            # volvemos de str a int el numero de evaluaciones
            num_evaluaciones = int(num_evaluaciones)
            # si es valida la entrada rompera el ciclo
            break

        else:
            print("\nError: Ingrese un numero positivo de evaluaciones.")

    # Solicitamos al usuario el nombre de cada evaluacion
    nombres_evaluaciones = []

    print("\nIngrese el nombre de cada evaluacion:")

    contador_evaluaciones = 0

    while contador_evaluaciones < num_evaluaciones:

        nombre_eval = input(f"Nombre para evaluacion {contador_evaluaciones + 1}: ")

        if nombre_eval != "":
            nombres_evaluaciones.append(nombre_eval)
            contador_evaluaciones += 1

        else:
            print("\nError: El nombre de la evaluacion no puede estar vacio.")

    # Inicializamos las listas vacias para despues clasificar alumnos y controlar matriculas
    aprobados = []  # Alumnos con promedio >= 6
    reprobados = []  # Alumnos con promedio < 6
    matriculas_registradas = []  # Para evitar matriculas duplicadas

    # Inicializa contador de alumnos
    alumno_actual = 0

    # Ciclo para capturar datos de cada alumno
    while alumno_actual < num_alumnos:

        # Muestra encabezado del alumno actual
        print(f"\n=== Alumno {alumno_actual + 1} ===")

        # Solicita y valida el nombre del alumno
        while True:

            nombre = input("Nombre del alumno: ")

            # Usa la funcion nombre_valido para validar el formato
            # utilizando solo letras y espacios
            if nombre_valido(nombre):
                break

            else:
                print("\nError: El nombre debe contener solo letras y espacios.")

        # Solicita y valida la matricula del alumno
        while True:

            matricula = input("Matricula del alumno: ")

            # Verifica que no este vacia
            if matricula == "":
                print("\nError: La matricula no puede estar vacia.")

            # Verifica que no este repetida
            elif matricula in matriculas_registradas:
                print("\nError: Esta matricula ya fue registrada.")

            else:
                # Si es valida, la agrega a la lista de matriculas registradas
                matriculas_registradas.append(matricula)
                break

        # Inicializa lista para almacenar las calificaciones del alumno
        calificaciones = []

        # inicializamos el contador de evaluaciones en 0
        evaluacion_actual = 0

        # Ciclo para capturar cada calificacion
        while evaluacion_actual < num_evaluaciones:

            while True:

                # Solicita la calificacion de la evaluacion actual
                calificacion = input(
                    f"Calificacion en '{nombres_evaluaciones[evaluacion_actual]}' (1 a 10): "
                )

                # Verifica que la entrada sea una calificacion valida
                if es_calificacion_valida(calificacion):

                    # Si es valida, la agrega a la lista
                    calificaciones.append(float(calificacion))
                    break

                else:
                    print("\nError: Ingrese una calificacion valida entre 1 y 10.")

            evaluacion_actual += 1  # Pasa a la siguiente evaluacion

        # Calcula el promedio del alumno
        promedio = sum(calificaciones) / num_evaluaciones

        # Crea un diccionario con los datos del alumno
        alumno_info = {
            "nombre": nombre,
            "matricula": matricula,
            "promedio": promedio,
        }

        # Clasifica al alumno segun su promedio
        if promedio >= 6:
            aprobados.append(alumno_info)

        else:
            reprobados.append(alumno_info)

        alumno_actual += 1  # Pasa al siguiente alumno

    # Muestra la lista de alumnos aprobados
    print("\n=== LISTA DE APROBADOS ===")

    if aprobados:

        # Recorre la lista de aprobados y muestra sus datos
        for alumno in aprobados:

            print(
                f"{alumno['nombre']} | Matricula: {alumno['matricula']} | Promedio: {alumno['promedio']:.2f}"
            )

    else:
        # Si no hay aprobados, muestra mensaje
        print("+++ No hay alumnos aprobados D: +++")

    # Muestra la lista de alumnos reprobados
    print("\n=== LISTA DE REPROBADOS ===")

    if reprobados:

        # Recorre la lista de reprobados y muestra sus datos
        for alumno in reprobados:

            print(
                f"{alumno['nombre']} | Matricula: {alumno['matricula']} | Promedio: {alumno['promedio']:.2f}"
            )

    else:
        # Si no hay reprobados, muestra el mensaje
        print("+++ No hay alumnos reprobados :D +++")

    print("\nGracias por utilizar el programa, nos vemos pronto :D")


# Llama a la funcion principal para iniciar el programa
evaluar_alumnos()
