import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        String date = sc.next();
        String[] dateArr = date.split("\\.");
        System.out.print(dateArr[1] + "-" + dateArr[2] + "-" + dateArr[0]);
    }
}