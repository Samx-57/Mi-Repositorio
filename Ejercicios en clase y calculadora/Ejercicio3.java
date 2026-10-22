import java.util.Scanner;

public class Ejercicio3 {
    public static void main(String[] args) {
        Scanner lector = new Scanner(System.in);
        
        System.out.print("Ingrese x1: ");
        double x1 = lector.nextDouble();
        
        System.out.print("Ingrese y1: ");
        double y1 = lector.nextDouble();
        
        System.out.print("Ingrese x2: ");
        double x2 = lector.nextDouble();
        
        System.out.print("Ingrese y2: ");
        double y2 = lector.nextDouble();
        
        double distancia = Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
        
        System.out.println("La distancia entre los dos puntos es: " + distancia);
    }
}