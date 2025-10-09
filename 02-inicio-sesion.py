# Credenciales validas (como variables individuales)
usuario_correcto = "admin"
clave_correcta = "123"
intentos = 3

print("\n === Sistema de Inicio de Sesión ===")
print(f"Intentos restantes: {intentos}")

# Solicitar credenciales
# Se crea un bucle el cual dara oportunidad de ingresar la
#  contraseña hasta que el numero de intentos llegue a 0
while intentos > 0:

    # guardamos lo que escriba el usuario en variables
    # utilizando la funcion input para que el usuario pueda
    # escribir
    print("Usuario: ")
    usuario = input()
    print("Contraseña: ")
    clave = input()

    # Obligamos al usuario que no deje vacias las entradas
    if usuario == "" or clave == "":
        print("Error: los campos no pueden estar vacios")

    # Si el usuario ingresa una credencial distinta a la valida mostrara error
    elif usuario != usuario_correcto or clave != clave_correcta:
        print("\nError: usuario o contraseña incorrecta")
        print(f"\nNúmero de intentos {intentos - 1}")

    # Si no es indistinto entonces mostrara un mensaje el cual indicara
    # que las credenciales que ingreso son validas y terminara la ejecucion del
    # programa
    else:
        print("Inicio de sesion exitoso")
        break

    # Si el inicio de sesion no tuvo exito el numero de intentos:
    # se reduce una oportunidad
    intentos -= 1

# si el numero de intentos llego a 0 saldra del bucle while
# ejecutara la siguiente linea de codigo que indicara que el acceso quedara bloqueado
if intentos == 0:
    print(
        "\n Has excedido el numero permitido de intentos. El acceso quedara bloqueado"
    )
