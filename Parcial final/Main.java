import java.util.Scanner;
import java.util.Random;

public class Main {
    public static void main(String[] args) {
        // Samuel David Cantillo Santos
        Scanner lector = new Scanner(System.in);
        Random aleatorio = new Random();

        // Matriz para hasta 10 personas y 5 datos por persona: 
        // [0: cedula, 1: nombre, 2: anoNacimiento, 3: genero, 4: profesion]
        String[][] matrizAspirantes = new String[10][5];
        int contadorPersonas = 0;

        int opcion = 0;
        do {
            System.out.println("\n--- MENU DE ASPIRANTES ---");
            System.out.println("1. Adicionar persona");
            System.out.println("2. Mostrar personas ingresadas");
            System.out.println("3. Seleccionar persona aleatoria y comparar promedio de edad");
            System.out.println("4. Extraer cedulas a un vector y mostrar");
            System.out.println("5. Terminar");
            System.out.print("Seleccione una opcion: ");
            
            opcion = lector.nextInt();
            lector.nextLine(); // Limpiar el buffer

            switch (opcion) {
                case 1:
                    if (contadorPersonas >= 10) {
                        System.out.println("Error: La matriz ya esta llena (maximo 10 personas).");
                    } else {
                        System.out.print("Ingrese numero de cedula: ");
                        matrizAspirantes[contadorPersonas][0] = lector.nextLine();

                        System.out.print("Ingrese nombre: ");
                        matrizAspirantes[contadorPersonas][1] = lector.nextLine();

                        System.out.print("Ingrese ano de nacimiento (ej. 2004): ");
                        matrizAspirantes[contadorPersonas][2] = lector.nextLine();

                        System.out.print("Ingrese genero: ");
                        matrizAspirantes[contadorPersonas][3] = lector.nextLine();

                        System.out.print("Ingrese profesion: ");
                        matrizAspirantes[contadorPersonas][4] = lector.nextLine();

                        contadorPersonas++;
                        System.out.println("¡Persona agregada con exito!");
                    }
                    break;

                case 2:
                    if (contadorPersonas == 0) {
                        System.out.println("No hay ninguna persona ingresada en este momento.");
                    } else {
                        System.out.println("\n--- LISTA DE ASPIRANTES INGRESADOS ---");
                        for (int i = 0; i < contadorPersonas; i++) {
                            System.out.println("Aspirante " + (i + 1) + ":");
                            System.out.println("  Cedula: " + matrizAspirantes[i][0]);
                            System.out.println("  Nombre: " + matrizAspirantes[i][1]);
                            System.out.println("  Ano Nacimiento: " + matrizAspirantes[i][2]);
                            System.out.println("  Genero: " + matrizAspirantes[i][3]);
                            System.out.println("  Profesion: " + matrizAspirantes[i][4]);
                            System.out.println("-----------------------------------");
                        }
                    }
                    break;

                case 3:
                    if (contadorPersonas == 0) {
                        System.out.println("No hay personas registradas para hacer la seleccion.");
                    } else {
                        // Generar numero aleatorio entre 0 y contadorPersonas - 1 (para evitar posiciones vacias)
                        int indiceAleatorio = aleatorio.nextInt(contadorPersonas);
                        
                        System.out.println("\n--- PERSONA SELECCIONADA AL AZAR ---");
                        String nombreSeleccionado = matrizAspirantes[indiceAleatorio][1];
                        int anoNacimiento = Integer.parseInt(matrizAspirantes[indiceAleatorio][2]);
                        int edadSeleccionada = 2026 - anoNacimiento; // Tomando anio actual 2026

                        System.out.println("Nombre: " + nombreSeleccionado);
                        System.out.println("Cedula: " + matrizAspirantes[indiceAleatorio][0]);
                        System.out.println("Edad estimada: " + edadSeleccionada + " anos");

                        // Calcular promedio de edad de todos los ingresados
                        int sumaEdades = 0;
                        for (int i = 0; i < contadorPersonas; i++) {
                            int anoPersona = Integer.parseInt(matrizAspirantes[i][2]);
                            sumaEdades += (2026 - anoPersona);
                        }
                        double promedioEdad = (double) sumaEdades / contadorPersonas;
                        System.out.println("Promedio de edad del grupo: " + promedioEdad + " anos");

                        if (edadSeleccionada > promedioEdad) {
                            System.out.println("Mensaje: " + nombreSeleccionado + " tiene una edad MAYOR que el promedio del grupo.");
                        } else if (edadSeleccionada < promedioEdad) {
                            System.out.println("Mensaje: " + nombreSeleccionado + " tiene una edad MENOR que el promedio del grupo.");
                        } else {
                            System.out.println("Mensaje: " + nombreSeleccionado + " tiene EXACTAMENTE la misma edad que el promedio del grupo.");
                        }
                    }
                    break;

                case 4:
                    if (contadorPersonas == 0) {
                        System.out.println("No hay datos para extraer cedulas.");
                    } else {
                        String[] vectorCedulas = new String[contadorPersonas];
                        for (int i = 0; i < contadorPersonas; i++) {
                            vectorCedulas[i] = matrizAspirantes[i][0];
                        }

                        System.out.println("\n--- VECTOR DE CEDULAS EXTRAIDAS ---");
                        for (int i = 0; i < vectorCedulas.length; i++) {
                            System.out.println("Posicion " + i + ": " + vectorCedulas[i]);
                        }
                    }
                    break;

                case 5:
                    System.out.println("Terminando el programa. ¡Mucho exito con el parcial!");
                    break;

                default:
                    System.out.println("Opcion no valida, intente de nuevo.");
            }
        } while (opcion != 5);
    }
}