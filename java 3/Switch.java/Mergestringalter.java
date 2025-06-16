import java.util.Scanner;

public class Mergestringalter {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter the first string: ");
        String str1 = scanner.nextLine();
        
        System.out.print("Enter the second string: ");
        String str2 = scanner.nextLine();
        
        String mergedString = " ";
        
        int length1 = str1.length();
        int length2 = str2.length();
        int maxLength = Math.max(length1, length2);
        
        for (int i = 0; i < maxLength; i++) {

            if (i < length1) {
                mergedString += str1.charAt(i);
            }
            if (i < length2) {
                mergedString += str2.charAt(i);
            }
        }
        
        System.out.println("Merged string: " + mergedString);
        
        scanner.close();
    }
}

