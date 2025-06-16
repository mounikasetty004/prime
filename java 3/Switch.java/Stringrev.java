import java.util.Scanner;

public class Stringrev {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a sentence: ");
        String input = scanner.nextLine();
        
        String[] words = input.split(" ");
        StringBuilder reversedSentence = new StringBuilder();
        
        for (String word : words) {
            StringBuilder reversedWord = new StringBuilder(word);
            reversedSentence.append(reversedWord.reverse().toString()).append(" ");
        }
        
        System.out.println("Reversed words: " + reversedSentence.toString().trim());
        
        scanner.close();
    }
}
