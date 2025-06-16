public class Encap {
    private int value;
    private String name; 

    public Encap(int value, String name) {
        this.value = value;
        this.name = name;
    }

    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }

    public String getName() {
        return name; 
    }

    public void setName(String name) {
        this.name = name; 
    }

    public static void main(String[] args) {
        Encap obj = new Encap(10, "John");
        System.out.println("Initial Value: " + obj.getValue());
        System.out.println("Initial Name: " + obj.getName());
        obj.setValue(20);
        obj.setName("Doe");
        System.out.println("Updated Value: " + obj.getValue());
        System.out.println("Updated Name: " + obj.getName());
    }
}