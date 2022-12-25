public class Element {
    public static void main(String[] args) {
        double ans = flower(200);
        System.out.println(ans);
        System.out.println("test");
    }

    public static double flower(double x) {
        double buff = x * 0.007;
        return 4300 * buff;
    }
}