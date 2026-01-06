import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        System.out.print(N>=3000? "book":(N>=1000? "mask":"no"));
    }
}