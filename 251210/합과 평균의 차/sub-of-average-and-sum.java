import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        int a, b, c, sum, average;
        Scanner sc = new Scanner(System.in);
        a = sc.nextInt();
        b = sc.nextInt();
        c = sc.nextInt();

        sum = a + b + c;
        average = sum / 3;
        System.out.print(sum + "\n" + average + "\n" + (sum-average));

        
    }
}