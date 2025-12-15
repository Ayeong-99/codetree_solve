import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        String[] strArr = s.split(":");
        int h = Integer.parseInt(strArr[0]);
        System.out.print((h+1)+":"+ (strArr[1]));
    }
}