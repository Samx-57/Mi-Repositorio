import java.util.Scanner;

public class Ejercicio1 {
    public static void main(String[] args) {
        Scanner lector = new Scanner(System.in);
        
        System.out.print("Ingrese el primer número entero: ");
        int numero1 = lector.nextInt();
        
        System.out.print("Ingrese el segundo número entero: ");
        int numero2 = lector.nextInt();
        
        int suma = numero1 + numero2;
        
        System.out.println("El resultado de la suma es: " + suma);
    }
}