public class Methods {
    public static void main(String[] args) {
        
        int[] numbers = {5, 3, 8, 1, 2};
        System.out.println("Original array: ");
        printArray(numbers);
        
        selectionSort(numbers);
        System.out.println("Sorted array: ");
        printArray(numbers);
        
        int number = 5;
        System.out.println("Factorial of " + number + " is: " + factorial(number));
    }


    public static void printArray(int[] arr) {
        for (int num : arr) {
            System.out.print(num + " ");
        }
     system.out.println();
    }

    
    public static void selectionSort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n - 1; i++) {
            int minIndex = i;
            for (int j = i + 1; j < n; j++) {
                if (arr[j] < arr[minIndex]) {
                    minIndex = j;
                }
            }
            int temp = arr[minIndex];
            arr[minIndex] = arr[i];
            arr[i] = temp;
        }
    }

    
    public static int factorial(int n) {
        if (n == 0 || n == 1) {
            return 1;
        } else {
            return n * factorial(n - 1);
            
        }
    }
    
}
