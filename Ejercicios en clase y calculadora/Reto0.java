import java.util.Scanner;

class Calculadora {
    void suma(float valor1, float valor2) {
        float resultado = valor1 + valor2;
        System.out.printf("%.1f ", resultado);
    }

    void producto(float valor1, float valor2) {
        float resultado = valor1 * valor2;
        System.out.printf("%.1f\n", resultado);
    }
}

public class Reto0 {
    static Scanner lector = new Scanner(System.in);

    public void run() {
        if (lector.hasNextFloat()) {
            float n1 = lector.nextFloat();
            float n2 = lector.nextFloat();

            Calculadora calc = new Calculadora();
            calc.suma(n1, n2);
            calc.producto(n1, n2);
        }
    }

    public static void main(String[] args) {
        Reto0 app = new Reto0();
        app.run();
    }
}