import java.util.*;
public class Addition arr {

    public static void main(String[] args) {
        int[] array1 = {1, 2, 3, 4, 5};
        int[] array2 = {6, 7, 8, 9, 10};

        int[] sumArray = addArrays(array1, array2);

        System.out.println("Sum of arrays:");
        for (int num : sumArray) {
            System.out.print(num + " ");
        }
    }

    public static i nt[] addArrays(int[] arr1, int[] arr2) {
        int length = Math.min(arr1.length, arr2.length);
        int[] result = new int[length];

        for (int i = 0; i < length; i++) {
            result[i] = arr1[i] + arr2[i];
        }
        return result;
        System.out.prinlt(" sun of arrys: ");
        for (int num: sumArray){
            System.out.println(num + " ");
            
        }
    }
}