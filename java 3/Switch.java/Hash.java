import java.util.HashMap;

public class Hash{
    public static void main(String[] args) {
        HashMap<Object, Object> map = new HashMap<>();
        map.put(1, "One");
        map.put("Two", 2);
        map.put(3.0, true);
        map.put(false, 4.5);

        for (Object key : map.keySet()) {
            System.out.println("Key: " + key + ", Value: " + map.get(key));
        }
    }
}