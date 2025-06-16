public class Captalize {
    public static void main(String[] args) {
        
        String str = "This is a simple example string with even and odd words";
        
      
        String[] words = str.split(" ");
        
       
        for (String word : words) {
            
            if (word.length() % 2 == 0) {
                
                String capitalizedWord = word.substring(0, 1).toUpperCase() + word.substring(1);
                
                System.out.println(Word);
            }
        }
    }
                      