interface nikitha{
    int A=10;
    void meet();
 }

 public class Inheritance implements nikitha{
    public void meet(){
        System.out.println("Hello"+A);
    }
    public static void main(String[] args) {
        Inheritance obj=new Inheritance();
        obj.meet();
    }   

 }                           