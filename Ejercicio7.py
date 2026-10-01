presion = float(input("Ingrese la presión: "))
volumen = float(input("Ingrese el volumen: "))
temperatura = float(input("Ingrese la temperatura: "))

if presion > 0 and volumen > 0 and (temperatura + 460) != 0:
    masa = (presion * volumen) / (0.37 * (temperatura + 460))
    print("La masa de aire es:", masa)
else:
    print("Error: Verifique los valores ingresados.")