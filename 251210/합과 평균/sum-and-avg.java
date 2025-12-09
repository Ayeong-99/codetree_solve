import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        int A, B;
        Scanner sc = new Scanner(System.in);
        A = sc.nextInt();
        B = sc.nextInt();
        double average = (A+B) / 2.0;
        System.out.printf((A+B) + " %.1f", average);
    }
}