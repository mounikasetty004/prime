import java.util.Scanner;

public class FirstLetter {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a sentence: ");
        String sentence = scanner.nextLine();

        String[] words = sentence.split(" ");
        System.out.print("First letters of each word: ");
        for (String word : words) {
            if (!word.isEmpty()) {
                System.out.print(word.charAt(0) + " ");
            }
        }

        scanner.close();
    }
}
