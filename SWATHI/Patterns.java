import java.util.*;
public class Patterns {
    public static void main(String[] args){
       //index element length   
         /*int maxi=0;
       String[] c={"alice and bob love leetcode","i am here","i am swathi i here to tell"};
       for(int i=0;i<c.length;i++){
        String[] c1=c[i].split(" ");
          if(c1.length>maxi){
            maxi=c1.length;
       
          }
       
       
        }
        System.out.println(i+" "+maxi);
       //square pattern and change some it is right angle triagle
        int n=5;
       for(int i=0;i<=n;i++){
         for(int j=0;j<=i;j++){
            System.out.print("*");
         }
        System.out.println();
       }*/
       //pyramid
      /*  int n=5;
       for(int i=0;i<=n;i++){
         for(int j=n-1;j>i;j++){
            System.out.print("*");
         }
        System.out.println();
       }
      String s="word";
      int n=s.length();
      int c=n-2;

      if(n>10){
      System.out.println(s.charAt(0)+""+c+""+s.charAt(n-1));
      }
      else{
        System.out.println(s);
      }
      String s="we are a happy family";
      String res="";
      String[] s1=s.split(" ");
      for(int i=0;i<s1.length;i++){
        StringBuffer c=new StringBuffer(s1[i]);
        c.reverse();
        res+=c+" ";


    
      }

      //bubble sort
      System.out.println(res);
      int[] arr={4,6,8,9,1};
      int temp=0;
      for(int i=0;i<arr.length;i++){
        for(int j=0;j<arr.length-1;j++){
            if(arr[j+1]<arr[j]){
                temp=arr[j];
                arr[j]=arr[j+1];
                arr[j+1]=temp;

            }
        }
        
      }
     for(int k=0;k<arr.length;k++){
        System.out.println(arr[k]);
     }
     int[] arr={4,6,8,9,1};
     int[] brr={1,6,7,8,9};
     int[] crr=new int[arr.length+brr.length];
     int k=0;
     for(int i=0;i<arr.length;i++){
        for(int j=0;j<brr.length-1;j++){
            if(arr[i]<brr[j]){
               crr[k]=arr[i];

            }
            else{
              crr[k]=brr[j];
            }
            k++;
        }
     }
     for(int l=0;l<crr.length;l++){
        System.out.println(crr[l]);
     }
    //pyramid
    int n=5;
    for(int i=0;i<n;i++){
      for(int k=0;k<n-i;k++){
        System.out.print(" ");
      }
      for(int j=0;j<=i;j++){
        System.out.print("* ");
      }
    System.out.println();
    }
    //reverse pyramid
    int n=5;
    for(int i=0;i<n;i++){
      for(int k=0;k<=i;k++){
        System.out.print(" ");
      }
      for(int j=i;j<n;j++){
        System.out.print(" *");
      }
    System.out.println();
    }
    int n=6;
    for(int i=0;i<n;i++){
      for(int k=0;k<n-i;k++){
        System.out.print(" ");
      }
      for(int j=0;j<=i;j++){
        System.out.print("* ");
      }
    System.out.println();
    }
    //reverse pyramid
    for(int i=0;i<n;i++){
      for(int k=0;k<=i;k++){
        System.out.print(" ");
      }
      for(int j=i;j<n-1;j++){
        System.out.print(" *");
      }
    System.out.println();
    }
    int[] arr={17,19,25,34,52};
    int target=3;
    Boolean flag=false;
    for(int i=0;i<arr.length;i++){
      if(arr[i]==target){
        flag=true;
        break;
      }
    }
    if(flag){
      System.out.println("element is found");
      
    }
      else{
        System.out.println("element is not found");
       
    }
    int[] arr={17,19,25,34,52,46,7};
    Arrays.sort(arr);
    int target=3;
    int l=0;
    int h=arr.length-1;
    boolean flag=false;
    while(l<=h){
      int mid=(l+h)/2;
      if(arr[mid]==target){
        flag=true;
        break;
      }
      
      else if(arr[mid]>target){
        h=mid-1;
      }
      else if(arr[mid]<target){
        l=mid+1;
      }

    
  } 
  if(flag){
    System.out.println("element is found");
      
  }
    else{
      System.out.println("element is not found");
     
  }
  //assigment numbers printling
  int n=5;
  for(int i=1;i<=n;i++){
    for(int j=0;j<n-i;j++){
      System.out.print("1");
    }
    int num=1;
    for(int k=0;k<i;k++){
      System.out.print(i);
      num+=2;
    }
  System.out.println();
  
  }
  Scanner sc=new Scanner(System.in);
  int n=sc.nextInt();
  int temp=n;
  int rem=0;
  int sum=0;
  while(n>0){
    rem=n%10;
    sum=sum*10+rem;
    n=n/10;
  }
  if(temp==sum){
    System.out.println("Palindrome");
  }
  else{
    System.out.println("not a palindrome");
  }*/
  char c='A';
  
  int v=(int)c+1;
  for(int i=0;i<5;i++){
    
    char s=(char)v;
    for(int j=i;j<i;j++){
      System.out.print(" "+s+" ");
    }
   
    System.out.println();
    v=v+1;
  }
 


  }

    
}


    

