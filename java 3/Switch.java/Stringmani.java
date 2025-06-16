import java.util.Scanner;

public class Stringmani {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String input = scanner.nextLine();
        
        if (input.length() < 10) {
            System.out.println(input);
        } else {
            System.out.println(input.charAt(0) + "" + (input.length() - 2) + input.charAt(input.length() - 1));
        }

        scanner.close();
    }
}
