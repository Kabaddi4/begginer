import java.util.Scanner;
// 宣言
public class Scan {
    public static void main(String[] args) {
        // 
        Scanner scan = new Scanner(System.in); 
        int num = scan.nextInt();

        System.out.println(num);
        scan.close();
    }
}