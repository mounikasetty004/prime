public class EvenLengthWords {
    public static void main(String[] args) {
        
        String str = "This is a simple example string with even and odd words";
        
        
        String[] words = str.split(" ");
        
        
        for (String word : words) {
            
            if (word.length() % 2 == 0) {
                
                System.out.print(word+" ");
            }
        }
    }
}
