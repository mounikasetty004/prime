import java.util.*;
public class EvenLength {
    public static void main(String[] args){
        //evn length
        /*String s="Welcome to the Qiscet";
        String[] arr=s.split(" ");
        for(int i=0;i<arr.length;i++){
            if((arr[i].length())%2==0){
                System.out.println(arr[i]);
            }
           
        }

        //anagram
        String s="at";
        String s1="cat";
        char ch[]=s1.toCharArray();
        char c1[]=s.toCharArray();
        Arrays.sort(ch);
        Arrays.sort(c1);
        System.out.println(Arrays.equals(ch,c1));
        char[] ch={'A','B'};
        System.out.println(ch);

        // array substrings
        int[] arr={1,2,3,4,5};
        for(int i=0;i<arr.length;i++){
            for(int j=i;j<arr.length;j++){
                for(int k=i;k<=j;k++){
                    System.out.print(arr[k]+" ");
                }
            System.out.println();
            }
        }
        StringBuilder sb=new StringBuilder("Hello");
        System.out.println(sb);
        sb.append("world");
        System.out.println(sb);
        sb.insert(5," ");
        System.out.println(sb);
        int n=sb.length();
        System.out.println(n);
        sb.reverse();
        sb.reverse();
        System.out.println(sb);
        sb.delete(0,5);
        System.out.println(sb);
        sb.replace(6,15,"developer");
        System.out.println(sb);
        String s="nabllonoballonballoon";
        String res="";
        int b=0;
        int a=0;
        int l=0;
        int o=0;
        int n=0;
        char[] ch=s.toCharArray();
        for(int i=0;i<ch.length;i++){
            if(ch[i]=='b'){
                b++;

            }
            else if(ch[i]=='a'){
                a++;

            }
            else if(ch[i]=='l'){
               
                l++;

            }
            else if(ch[i]=='o'){
                
                o++;
            }
            else if(ch[i]=='n'){
                n++;
            }
        }
        o/=2;
        l/=2;

            
        System.out.println(l);
//even numbers in array  
int[] arr={19,27,32,8,12,14};
for(int i=0;i<arr.length;i++){
    if(arr[i]%2!=0){
        System.out.println(i+" "+arr[i]);
    }
    else{
        System.out.println(arr[i]+" "+i);
    }
}
//columns highest value
Scanner sc=new Scanner(System.in);
int r=sc.nextInt();
int c=sc.nextInt();
int[][] arr=new int[r][c];
int[] cols=new int[c];
for(int i=0;i<r;i++){
    for(int j=0;j<c;j++){
        arr[i][j]=sc.nextInt();
    }
}

for(int j=0;j<c;j++){
       int max=arr[0][j];
    for(int i=0;i<r;i++){
        if(arr[i][j]>max){
            max=arr[i][j];

        }
    }
    //System.out.println(max);
    cols[j]=max;

}
for(int max:cols){
    System.out.println(max);
}*/

        



       
    }
    
}
