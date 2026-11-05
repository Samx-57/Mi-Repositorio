import java.io.FileWriter;
import java.io.IOException;
import java.util.Arrays;
import java.util.Random;

public class Ordenamiento {

    // Cambia este valor según el método que le toque a tu grupo:
    // "burbuja", "insercion", "merge" o "quick"
    static final String METODO = "burbuja";

    static final int TAM = 100000;

    // ---------- Bubble sort ----------
    static void burbuja(int[] a) {
        int n = a.length;
        for (int i = 0; i < n - 1; i++) {
            boolean huboCambio = false;
            for (int j = 0; j < n - 1 - i; j++) {
                if (a[j] > a[j + 1]) {
                    int tmp = a[j];
                    a[j] = a[j + 1];
                    a[j + 1] = tmp;
                    huboCambio = true;
                }
            }
            if (!huboCambio) break;
        }
    }

    // ---------- Insertion sort ----------
    static void insercion(int[] a) {
        for (int i = 1; i < a.length; i++) {
            int clave = a[i];
            int j = i - 1;
            while (j >= 0 && a[j] > clave) {
                a[j + 1] = a[j];
                j--;
            }
            a[j + 1] = clave;
        }
    }

    // ---------- Merge sort ----------
    static void merge(int[] a) {
        if (a.length < 2) return;
        mergeSort(a, new int[a.length], 0, a.length - 1);
    }

    static void mergeSort(int[] a, int[] aux, int izq, int der) {
        if (izq >= der) return;
        int medio = (izq + der) / 2;
        mergeSort(a, aux, izq, medio);
        mergeSort(a, aux, medio + 1, der);
        int i = izq, j = medio + 1, k = izq;
        while (i <= medio && j <= der) {
            if (a[i] <= a[j]) aux[k++] = a[i++];
            else aux[k++] = a[j++];
        }
        while (i <= medio) aux[k++] = a[i++];
        while (j <= der) aux[k++] = a[j++];
        for (k = izq; k <= der; k++) a[k] = aux[k];
    }

    // ---------- Quick sort ----------
    static void quick(int[] a) {
        quickSort(a, 0, a.length - 1);
    }

    static void quickSort(int[] a, int bajo, int alto) {
        if (bajo >= alto) return;
        int pivote = a[(bajo + alto) / 2];
        int i = bajo, j = alto;
        while (i <= j) {
            while (a[i] < pivote) i++;
            while (a[j] > pivote) j--;
            if (i <= j) {
                int tmp = a[i];
                a[i] = a[j];
                a[j] = tmp;
                i++;
                j--;
            }
        }
        quickSort(a, bajo, j);
        quickSort(a, i, alto);
    }

    // ---------- Utilidades ----------
    static void ordenar(int[] a) {
        switch (METODO) {
            case "burbuja":   burbuja(a);   break;
            case "insercion": insercion(a); break;
            case "merge":     merge(a);     break;
            case "quick":     quick(a);     break;
            default: throw new IllegalArgumentException("Método inválido: " + METODO);
        }
    }

    // Copia los primeros n números del vector original, los ordena
    // en un segundo vector y devuelve el tiempo en milisegundos.
    static double medir(int[] original, int n) {
        int[] ordenado = Arrays.copyOf(original, n);
        long inicio = System.nanoTime();
        ordenar(ordenado);
        long fin = System.nanoTime();
        return (fin - inicio) / 1_000_000.0;
    }

    public static void main(String[] args) {
        Random rnd = new Random();

        // Vector de 100000 con números aleatorios entre 1 y 1000
        int[] vector = new int[TAM];
        for (int i = 0; i < TAM; i++) {
            vector[i] = rnd.nextInt(1000) + 1;
        }

        // Prueba con 30 números (para mostrarle al profesor)
        int[] prueba = Arrays.copyOf(vector, 30);
        int[] pruebaOrdenada = prueba.clone();
        ordenar(pruebaOrdenada);
        System.out.println("Método: " + METODO);
        System.out.println("Original : " + Arrays.toString(prueba));
        System.out.println("Ordenado : " + Arrays.toString(pruebaOrdenada));

        // Tiempos
        double t10k = medir(vector, 10000);
        double t100k = medir(vector, 100000);
        System.out.printf("10.000 números : %.2f ms%n", t10k);
        System.out.printf("100.000 números: %.2f ms%n", t100k);

        // Archivo de texto con los resultados
        try (FileWriter fw = new FileWriter("resultados.txt")) {
            fw.write("Integrantes: 1) ______  2) ______  3) ______\n");
            fw.write("Método: " + METODO + "\n");
            fw.write("Tiempo 10.000 números (ms): " + t10k + "\n");
            fw.write("Tiempo 100.000 números (ms): " + t100k + "\n");
            fw.write("(Pega aquí el código fuente del método)\n");
        } catch (IOException e) {
            System.out.println("No se pudo escribir resultados.txt: " + e.getMessage());
        }
    }
}
