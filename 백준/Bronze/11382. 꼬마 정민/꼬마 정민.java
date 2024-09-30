import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        long A = scanner.nextLong(); // long 타입으로 변경
        long B = scanner.nextLong(); // long 타입으로 변경
        long C = scanner.nextLong(); // long 타입으로 변경
        
        System.out.println(A + B + C);

        scanner.close();
    }
}
