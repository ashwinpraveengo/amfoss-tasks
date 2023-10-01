import java.util.Scanner;

class GFG {
    static boolean Prime(int n) {
        if (n == 1 || n == 0)
            return false;

        for (int i = 2; i < n; i++) {
            if (n % i == 0)
                return false;
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a value for N: ");
        int N = scanner.nextInt();

        for (int i = 1; i <= N; i++) {
            if (Prime(i)) {
                System.out.print(i + " ");
            }
        }
        scanner.close();
    }
}
