import java.util.*;
public class Sample2 {
    public static void main(String[] args) {
        // int[] arr={1,2,3,4,5,6};
        // //=>6,1,2,3,4,5
        // int temp=arr[arr.length-1];
        // int[] brr=new int[arr.length];
        // int k=0;
        // for(int i=1;i<arr.length;i++)
        // {
        //     brr[i]=arr[k];
        //     k++;
        // }
        // brr[0]=temp;
        // System.out.println(Arrays.toString(brr));
        String s="hello";
        //System.out.println(c);
        int c=s.length();
        int sum=0;
        for(int i=0;i<c-1;i++){
           int j=s.charAt(i);
           int k=s.charAt(i+1);
           sum+=Math.abs(k-j);

        }
        System.out.println(sum);
    }
}
//4 5 6 
//1 2 3