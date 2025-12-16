import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        String phone = sc.next();
        String[] phArr = phone.split("-");
        System.out.print(phArr[0]+"-"+phArr[2]+"-"+phArr[1]);
    }
}