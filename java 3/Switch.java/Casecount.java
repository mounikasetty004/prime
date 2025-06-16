public class Casecount{
    public static void main(String[] args) {
       
        String str = "This is a Simple Example String with Even and Odd Words";
        
        
        String[] words = str.split("    ");
        
        
        for (String word : words) {
            int uppercaseCount = 0;
            int lowercaseCount = 0;
            
            
            for (char c : word.toCharArray()) {
                if (Character.isUpperCase(c)) {
                    uppercaseCount++;
                } else if (Character.isLowerCase(c)) {
                    lowercaseCount++;
                }
            }

            
           
            System.out.println("Word: " + word);
            System.out.println("Uppercase Count: " + uppercaseCount);
            System.out.println("Lowercase Count: " + lowercaseCount);
            System.out.println();
        }
    }
}                          
