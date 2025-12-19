import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int wide = sc.nextInt();
        int height = sc.nextInt();
        wide += 8;
        height *= 3; 
        System.out.println(wide);
        System.out.println(height);
        System.out.println(wide * height);
    }
}