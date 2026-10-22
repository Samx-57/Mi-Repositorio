import java.util.Scanner;

public class Ejercicio2 {
    public static void main(String[] args) {
        Scanner lector = new Scanner(System.in);
        
        System.out.print("Ingrese la distancia en kilómetros: ");
        double kilometros = lector.nextDouble();
        
        double metros = kilometros * 1000;
        double centimetros = metros * 100;
        
        System.out.println("Equivalente en metros: " + metros);
        System.out.println("Equivalente en centímetros: " + centimetros);
    }
}
