taller = []
limite = 30

while True:
    print("\n--- SISTEMA DEL TALLER ---")
    print("1. Registrar ingreso de vehículo")
    print("2. Registrar salida de vehículo")
    print("3. Reporte de vehículos terminados")
    print("4. Reporte general de todos los vehículos")
    print("5. Salir")
    
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        if len(taller) >= limite:
            print("Error: Se ha alcanzado el límite máximo de 30 vehículos.")
        else:
            placa = input("Placa del vehículo: ")
            propietario = input("Nombre del propietario: ")
            celular = input("Número de celular: ")
            
            while True:
                diaingreso = int(input("Día de ingreso (1 a 31): "))
                if diaingreso >= 1 and diaingreso <= 31:
                    break
                print("Día inválido. Debe ser entre 1 y 31.")

            vehiculo = [placa, propietario, celular, diaingreso, "Pendiente", "En reparación"]
            taller.append(vehiculo)
            print("Vehículo registrado exitosamente.")

    elif opcion == "2":
        if len(taller) == 0:
            print("No hay vehículos registrados en el taller.")
        else:
            busqueda = input("Ingrese la placa del vehículo a entregar: ")
            encontrado = False
            
            for v in taller:
                if v[0] == busqueda:
                    encontrado = True
                    if v[4] != "Pendiente":
                        print("Este vehículo ya fue entregado anteriormente.")
                    else:
                        while True:
                            diasalida = int(input("Día de salida (1 a 31): "))
                            if diasalida >= v[3] and diasalida <= 31:
                                break
                            print("Error: El día de salida debe ser igual o mayor al día de ingreso")
                        
                        diasdemora = diasalida - v[3]
                        v[4] = diasalida
                        v[5] = diasdemora
                        print("Salida registrada con éxito. Días en reparación:", diasdemora)
                    break
            
            if not encontrado:
                print("No se encontró ningún vehículo con esa placa.")

    elif opcion == "3":
        terminados = 0
        print("\n--- REPORTE DE VEHÍCULOS TERMINADOS ---")
        for v in taller:
            if v[4] != "Pendiente":
                terminados = terminados + 1
                print("Placa:", v[0], "| Propietario:", v[1], "| Días en taller:", v[5])
        
        if terminados == 0:
            print("Aún no hay vehículos terminados.")
        else:
            print("Total vehículos terminados:", terminados)

    elif opcion == "4":
        if len(taller) == 0:
            print("No hay vehículos ingresados en el mes.")
        else:
            print("\n--- REPORTE GENERAL DE VEHÍCULOS INGRESADOS ---")
            for v in taller:
                print("Placa:", v[0], "| Propietario:", v[1], "| Celular:", v[2])

    elif opcion == "5":
        print("Cerrando aplicación...")
        break

    else:
        print("Opción inválida. Intente de nuevo.")