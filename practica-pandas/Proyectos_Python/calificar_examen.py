import pandas as pd


# === 1 - Cargar archivos ===
df_estudiantes = pd.read_csv("./archivos/respuestas_estudiantes.csv")
df_correctas = pd.read_excel("./archivos/respuestas_correctas.xlsx")


# 2 - === Obtener las preguntas usando metodos ===
preguntas = df_correctas["Pregunta"].values  # usando values


# 3 - === crear diccionario vacio con las respuestas correctas ===
clave_respuestas = {}
for i in range(df_correctas.shape[0]):

    # Extraemos pregunta y respuesta
    pregunta = df_correctas["Pregunta"].iloc[i]
    respuesta = df_correctas["Respuesta"].iloc[i]

    # Almacenamos en el diccionario
    clave_respuestas[pregunta] = respuesta


# 4 - === calcular puntuacion para cada estudiante ===

df_estudiantes["Puntuación"] = 0  # Inicializa la columna de puntuacion

for p in preguntas:  # Recorre cada pregunta
    respuesta_correcta = clave_respuestas[p]  # obtiene la respuesta correcta

    # compara respuestas y suma 1 punto por cada acierto
    df_estudiantes["Puntuación"] = df_estudiantes["Puntuación"].add(
        (df_estudiantes[p] == respuesta_correcta).astype(int)
    )


# 5 - === Mostrar detalle completo de respuestas ===
df_detalle = df_estudiantes.copy()  # copia el dataFrame original

for p in preguntas:
    # Marca errores añadiendo X donde no coinciden:
    df_detalle[p] = df_detalle[p].where(
        df_detalle[p] == clave_respuestas[p], df_detalle[p] + " X"
    )

# Ordena por puntuacion (mayor a menor):
df_detalle = df_detalle.sort_values("Puntuación", ascending=False)
print("Leyenda: RespuestaX = incorrecta")
print(df_detalle.to_string(index=False))  # Muestra sin indices


# 6 -  Mostrar resultados resumidos
print("\n=== RESULTADOS DE LOS ESTUDIANTES ===")

print(
    df_estudiantes[["Nombre", "Puntuación"]]
    .sort_values("Puntuación", ascending=False)
    .to_string(index=False)
)


# 7 - Preguntar formato de guardado en bucle
while True:
    print("\n¿En qué formato deseas guardar los resultados?")
    print("\n === Indica el numero deseado ===")
    print("\nOpciones: 1 = CSV (.csv) | 2 = Excel (.xlsx)")

    opcion = input("Ingresa tu elección: ")

    if opcion == "1":
        df_estudiantes.to_csv("resultados_examen.csv", index=False)
        print("Resultados guardados en 'resultados_examen.csv'")
        break

    elif opcion == "2":
        df_estudiantes.to_excel(
            "resultados_examen.xlsx", sheet_name="Hoja 1", index=False
        )
        print("Resultados guardados en 'resultados_examen.xlsx'")
        break

    else:
        print("\nOpción no válida!!! Intenta nuevamente.")
