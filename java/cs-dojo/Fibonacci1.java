import java.util.Scanner;

public class Fibonacci1 {

    // Iterative method to compute nth Fibonacci number
    static int fib(int n) {
        if (n <= 1) return n;

        int a = 0, b = 1, c = 1;
        for (int i = 2; i <= n; i++) {
            c = a + b;
            a = b;
            b = c;
        }
        return c;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of terms: ");
        int n = sc.nextInt();

        System.out.println("Fibonacci series up to " + n + " terms:");
        for (int i = 0; i < n; i++) {
            System.out.println("Fibonacci of " + i + " is " + fib(i));
        }
    }
}
