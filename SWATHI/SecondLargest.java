import java.util.*;
public class SecondLargest {
    public static void main(String[] args){
        Scanner obj=new Scanner(System.in);
        //Scanner s=new Scanner(System.in);
       // System.out.println("Enter size of an array");
        int[] arr={1,1,0,1,0,1,1,1,1,1,1};
        int[] arr1={2,3,4};
        /*int first=arr[0];
        int second=arr[0];
        int firsts=arr[0];
        int largests=arr[0];
        for(int i=0;i<arr.length;i++){
            if(first<arr[i]){
                second=first;
                first=arr[i];
            }
            else if(arr[i]>second && arr[i]!=first){
                    second=arr[i];
                }
            if(firsts>arr[i]){
                largests=firsts;
                firsts=arr[i];
            
            }
            else{
                if(arr[i]<largests && arr[i]!=firsts){
                    largests=arr[i];
                    
                }
            }
            }
        
        
        System.out.println("second largest:"+second);
        System.out.println("second small:"+largests);
        for(int i=0;i<arr.length;i++){
            if(arr[i+1]>arr[i]){
                System.out.println("Yes");
                break;

            }
            else{
                System.out.println("No");
                break;
            }
        }
        int n=obj.nextInt();
        int arr1[]=new int[n];


        for(int i=0;i<arr.length;i++){
            if (arr[i]==0){
                arr1[i]=arr[i];
                
            }
            else{
                System.out.println(arr[i]+" ");
                
            }
    
        }
        for(int i=0;i<arr1.length;i++){
            System.out.println(arr1[i]);
            break;
        


    }
    int c=0;
    int maxi=0;
    for(int i=0;i<arr.length;i++){
       
        if(arr[i]==1){
            c++;
        }
        else{
           c=0;
        }
        if(c>maxi){
            maxi=c;
        }
    //maxi=Math.max(maxi,c);
    }

    System.out.println(maxi);*/ 
   
     int n=arr.length;
     int m=arr1.length;
     int  v=n+m;
     int c[]=new int[v];
      int k=0;
      for(int i=0; i<n;i++){
        c[k]=arr[i];
        k++;

      }
      for(int j=0;j<m;j++){
        c[k]=arr1[j];
        k++;

      }
      for(int i=0;i<c.length;i++){
        System.out.print(c[k]);
      }
    }
}

