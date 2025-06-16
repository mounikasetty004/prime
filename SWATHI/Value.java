public class Value{
    public static void main(String[] args){
        /*String s1=new String("hello");
        String s2=new String("hello");
        System.out.println(s1==s2);
        String s1="Welcome to the class";
        String[] s=s1.split(" ");
        String res="";
        int n=s.length;
        for(int i=n-1;i>=0;i--){
            res+=s[i]+" ";
        }
        System.out.println(res);
        String s="i love programming";
        String[] s1=s.split(" ");
        //String res="";
        int n=s1.length;
        for(int i=0;i<s1.length;i++){
            s1[i]=s1[i].substring(0,1).toUpperCase()+s1[i].substring(1).toLowerCase();
        }
        String res="";
        for(int i=0;i<s1.length;i++){
            res+=s1[i]+" ";
        }
        System.out.println(res.trim());
        String s="madam";
        //String temp=s;
        //String[] s1=s.split(" ");
        //String res="";
        int n=s.length();
        String res= "";
        for(int i=n-1;i>=0;i--){
            
                res+=s.charAt(i);
            }
        System.out.println(res.equals(s)?"palindrome":"not palindrome");
        //int c='A';
        String s="hello";
        //System.out.println(c);
        int c=s.length();
        int sum=0;
        for(int i=0;i<=c;i++){
           int j=s.charAt(i);
           int k=s.charAt(i+1);
        sum+=Math.abs(k-j);

        }
        System.out.println(sum);
        String s="Swathi";
        int n=s.length();
        System.out.println(n);*/
        int num=8;
        //int i=0;
        int count=0;
        while(num!=0){
            if(num%2==0){
                num/=2;
                count++;
            }
            else{
                
                //count++;
                num=num-1;
                count++;
            }


        //num=num-1;
        }
        System.out.println(count);
        String s="hello";
        //System.out.println(c);
        int c=s.length();
        int sum=0;
        for(int i=0;i<c;i++){
           int j=s.charAt(i);
           int k=s.charAt(i+1);
           sum+=Math.abs(k-j);

        }
        System.out.println(sum);

        
        
        
        
        
        String s1="Welcome to the class";
        String[] s2=s1.split(" ");
        String res="";
        int n=s2.length;
        for(int i=n-1;i>=0;i--){
            res+=s2[i]+" ";
        }
        System.out.println(res);
    
}
}
