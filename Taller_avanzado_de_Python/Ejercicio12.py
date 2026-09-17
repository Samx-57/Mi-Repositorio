usuario_correcto = "administrador"
clave_correcta = "Python2026"
acceso = False

for i in range(3):
    print("\nIntentos restantes:", 3 - i)
    usuario = input("Usuario: ")
    clave = input("Contraseña: ")
    
    if usuario == usuario_correcto and clave == clave_correcta:
        acceso = True
        break
    else:
        print("Error: Usuario, contraseña o ambos son incorrectos.")

if not acceso:
    print("\nSistema bloqueado por exceder los 3 intentos fallidos.")
else:
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Consultar información")
        print("2. Cambiar contraseña")
        print("3. Cerrar sesión")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            print("Información del sistema: Operativo y seguro.")
        elif opcion == "2":
            actual = input("Ingrese la contraseña actual: ")
            if actual == clave_correcta:
                clave_correcta = input("Ingrese la nueva contraseña: ")
                print("Contraseña cambiada con éxito.")
            else:
                print("Error: Contraseña actual incorrecta.")
        elif opcion == "3":
            print("Sesión cerrada.")
            break
        else:
            print("Opción inválida.")