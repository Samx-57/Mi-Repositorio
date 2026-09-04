
# Taller práctico de Python.

# INTEGRANTES: {Yainer Barrios} {Samuel Cantillo}

# Parte 1. Conceptos basicos.
# 1.) ¿Que funcion utiliza python para pedir datos al usuario?
# R/= Python utiliza la funcion "input" para pedirle datos al usuario.

# 2.) ¿Que tipo de dato devuelve input por defecto?
#R/= Devuelte datos de tipo string (str)

# 3.) ¿Que diferencia existe entre int y float?
# R/= El int se utiliza para datos de tipo entero y el flot para datos con decimales

# 4.) ¿Para qué sirve el operador + cuando se trabaja con cadenas?
# R/= Sirve para concatenar dos o mas cadenas de texto en una sola

# 5.) ¿Cual es la diferencia entre / y // en python?
# R/= El / realiza una division y entrega los resultados con decimales y el // hace la division y entrega el resulltado redondeado hacia abajo al numero entero mas cercano

# Parte 2. Ejercicios practicos.
#Ejercicio 1:

nombre = str(input("Introduzca su nombre: "))
edad = int(input("Introduzca su edad: "))
ciudad = str(input("Introduzca su ciudad: "))
print("===========================================")
print("Hola " + str(nombre) + ", tienes " + str(edad) + " años y vives en " + ciudad + ".")