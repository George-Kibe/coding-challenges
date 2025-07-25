// Write a program to print the fibonacci series up to n terms

import java.util.Scanner;

public class Fibonacci {
    static int fib(int n) {
        if (n >= 3) {
            return fib(n-1) + fib(n-2);
        } else {
            return 1;
        }
    }   
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of terms: ");
        int n = sc.nextInt();

        System.out.println("Fibonacci series up to " + n + " terms:");
        for (int i = 1; i < n; i++) {
            System.out.println("Fibonacci of " + i + " is " + fib(i));
        }
    }
}