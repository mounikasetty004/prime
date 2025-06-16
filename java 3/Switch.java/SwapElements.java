public class SwapElements {

    public static void main(String[] args) {
        int[] arr = {10, 20, 30, 40, 50};
        int index1 = 1;
        int index2 = 3;

        System.out.println("Array before swapping:");
        printArray(arr);

        swap(arr, index1, index2);

        System.out.println("Array after swapping:");
        printArray(arr);
    }

    public static void swap(int[] arr, int index1, int index2) {
        if (index1 >= 0 && index1 < arr.length && index2 >= 0 && index2 < arr.length) {
            int temp = arr[index1];
            arr[index1] = arr[index2];
            arr[index2] = temp;
        } else {
            System.out.println("Invalid indices for swapping.");
        }
    }

    public static void printArray(int[] arr) {
        for (int num : arr) {
            System.out.print(num + " ");
        }
        System.out.println();
    }
}