import java.util.*;
class Sample {
    public static void main(String[] args){
        Scanner obj=new Scanner(System.in);
       //system.out.println("Enter row column values");
        /*int marks[][]={{40,70,60},{28,47,50}};
        System.out.println(marks.length);
        System.out.println(marks[0].length);
        for(int i=0;i<marks.length;i++){
            for(int j=0;j<marks[0].length;j++){
                System.out.print(marks[i][j]+" ");
            }
            System.out.println();
        }
    }
}
        int r=sc.nextInt();
        int c=sc.nextInt();
        int mat[][]=new int[r][c];
        System.out.println("enter mat values");
        for(int i=0;i<r;i++)
        {
            for(int j=0;j<c;j++)
            {
                mat[i][j]=sc.nextInt();
            }
        }
        int sum=0;
        System.out.println("printing");
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                sum=sum+mat[i][j];
            }
            System.out.println(sum);
        }
        int x=5;
        System.out.print("enter");
        System.out.print(x);
		System.out.println("Enter the value of N: ");
		int a=obj.nextInt();
		for(int i=0;i<a;i++){
			for(int j=0;j<a;j++){
				if(j<=i){
				System.out.print("*");
				}
			}
		System.out.println();
		}
        System.out.print("Enter the value of N: ");
	int n=obj.nextInt();
	int i=0;
	
	while(i<n){
		int j=0;
		while(j<=i){
			System.out.print("* ");
			j++;
		}
	System.out.println();
	i++;
	}
    System.out.println("enter the size");
    
	int n = obj.nextInt();
	if((n>=3 && n<=49) & n%2==1){
		for(int i=0;i<n;i++){
			for (int j=0;j<n;j++){
				if(i==n/2 && j==n/2){
					System.out.print("X");
				}
				else if(j==n-i-1){
					System.out.print("/");
				}
				else if(i==j){
					System.out.print("\\");
				}
				else{
					System.out.print("*");
				}
				
			}
		System.out.println();
		}
    }
    //avg of 2-dimensional arrays
    System.out.println("enter size of a array");
    int r=obj.nextInt();
    int c=obj.nextInt();
    int mat[][]=new int[r][c];
    System.out.println("enter array elements");
    for(int i=0;i<r;i++){
        for(int j=0;j<c;j++){
            mat[i][j]=obj.nextInt();

        }
    }
    int max=r*c;
    //int min=mat[0][0];
    for (int i=0;i<r;i++){
        for(int j=0;j<c;j++){
            //if(mat[i][j]>=6){
            if(i==j || i+j==max-1){
                System.out.println(mat[i][j]) ;

            }
    }
    }
    System.out.println("enter size of a array");
    int r=obj.nextInt();
    int c=obj.nextInt();
    int mat[][]=new int[r][c];
    
    System.out.println("enter array elements");
    for(int i=0;i<r;i++){
        for(int j=0;j<c;j++){
            mat[i][j]=obj.nextInt();
            //mat1[i][j]=obj.nextInt();

        }
    }
    int mat1[][]=new int[r][c];
    System.out.println("enter array elements");
    for(int i=0;i<r;i++){
        for(int j=0;j<c;j++){
             mat1[i][j]=obj.nextInt();
        }
    }
    
    //int min=mat[0][0];
    int res[][]=new int[r][c];
    for (int i=0;i<r;i++){
        for(int j=0;j<c;j++){
            res[i][j]=mat[i][j]+mat1[i][j];
	}
}
    for (int i=0;i<r;i++){
        for(int j=0;j<c;j++){
            System.out.print(res[i][j]+" ");

    }

    System.out.println();
}
System.out.println("enter size of a array");
int r=obj.nextInt();
int c=obj.nextInt();
int mat[][]=new int[r][c];
System.out.println("enter array elements");
for(int i=0;i<r;i++){
    for(int j=0;j<c;j++){
        mat[i][j]=obj.nextInt();

    }
}
int max=r*c;
//int min=mat[0][0];
for (int i=0;i<r;i++){
    for(int j=0;j<c;j++){
        
        System.out.print(mat[j][i]+" ");

    }
System.out.println();
}
System.out.println("enter size of a array1");
    int r1=obj.nextInt();
    int c1=obj.nextInt();
    int mat[][]=new int[r1][c1];
    
    System.out.println("enter array1 elements");
    for(int i=0;i<r1;i++){
        for(int j=0;j<c1;j++){
            mat[i][j]=obj.nextInt();
            //mat1[i][j]=obj.nextInt();

        }
    }
    int r2=obj.nextInt();
    int c2=obj.nextInt();
    int mat1[][]=new int[r2][c2];
    System.out.println("enter array2 elements");
    for(int i=0;i<r2;i++){
        for(int j=0;j<c2;j++){
             mat1[i][j]=obj.nextInt();
        }
    }
    
    //int min=mat[0][0];
    int res[][]=new int[r1][c1];
    if(c1==r2){
     for (int i=0;i<r1;i++){
         for(int j=0;j<c1;j++){
             for(int k=0;k<r2;k++){
               res[i][j]+=mat[i][k]*mat1[k][j];
	}
}
 }
    for (int c=0;c<r2;c++){
        for(int j=0;j<c1;j++){
            System.out.print(res[c][j]+" ");

    }

    System.out.println();
}
    }
    //int[] arr={4,3,9,6,0};
    //int[] arr2={4,3,9,6,0};
   // Arrays.sort(arr);
    //System.out.println(Arrays.equals(arr,arr2));
    //for(int i:arr){
        //System.out.println(i+" ");
   // }
   System.out.println("enter size of a array");
int r=obj.nextInt();
//int c=obj.nextInt();
int[][] mat=new int[r][];
System.out.println("enter array elements");
for(int i=0;i<r;i++){
    System.out.println("Enter columns");
      int colsize=obj.nextInt();
      mat[i]=new int[colsize];

    }

//int max=r*c;
//int min=mat[0][0];
for (int i=0;i<r;i++){
    for(int j=0;j<mat[i].length;j++){
        mat[i][j]=obj.nextInt();
    }

}
for (int i=0;i<r;i++){
    for(int j=0;j<mat[i].length;j++){
        System.out.print(mat[i][j]+" ");
        }
        System.out.println();

    }int r=obj.nextInt();
    int c=obj.nextInt();
    
    int mat[][]=new int[r][c];
    System.out.println("enter mat values");
    for(int i=0;i<r;i++)
    {
        for(int j=0;j<c;j++)
        {
            mat[i][j]=obj.nextInt();
        }
    }
    int sum=0;
    System.out.println("printing");
    for(int i=0;i<r;i++){
        sum=0;
        for(int j=0;j<c;j++){
            sum=sum+mat[i][j];
        //System.out.println(sum);
        }
        System.out.println(sum);
        
    }
    System.out.println("enter size of a array");
    int r=obj.nextInt();
    //int c=obj.nextInt();
    int[][] mat=new int[r][];
    System.out.println("enter array elements");
    for(int i=0;i<r;i++){
        System.out.println("Enter columns");
          int colsize=obj.nextInt();
          mat[i]=new int[colsize];
    
        }
    
    //int max=r*c;
    //int min=mat[0][0];
    for (int i=0;i<r;i++){
        for(int j=0;j<mat[i].length;j++){
            mat[i][j]=obj.nextInt();
        }
    
    }
    int sum=0;
    for (int i=0;i<r;i++){
        //sum=0;
        for(int j=0;j<mat[i].length;j++){
           //System.out.print(mat[i][j]+" ");
           if (mat[i][j]==1){
            System.out.println(i+" "+j);
            //sum=mat[i][j];
           }
           //sum=sum+mat[i][j];
            }
        //System.out.println(sum);
    
    int r=obj.nextInt();
    
    int arr[]= new int[n];
    int n=arr.length;
    for(int i=0;i<r;i++){
        arr[i]=obj.nextInt();
    }
    int n=arr.length;
    int brr[]=new int[r];
    int temp=arr[n-1];
    int j=0;
    for (int i=1;i<arr.length;i++){
        brr[i]=arr[j];
        j++;

        
    }
    brr[0]=temp;*/
    System.out.println("enter size of a array");
    int r=obj.nextInt();
    int c=obj.nextInt();
    int mat[][]=new int[r][c];
    System.out.println("enter array elements");
    for(int i=0;i<r;i++){
        for(int j=0;j<c;j++){
            mat[i][j]=obj.nextInt();

        }
    }
    int max=r*c;
    //int min=mat[0][0];
    for (int i=0;i<r;i++)
    {
        for(int j=0;j<c;j++)
        {
            //if(mat[i][j]>=6){
            if(i==j )
            {
                System.out.println(mat[i][j]) ;

            }
        }
    }
    for (int i=0;i<r;i++)
    {
        for(int j=0;j<c;j++)
        {
            //if(mat[i][j]>=6){
            if(i+j==r-1)
            {
                System.out.println(mat[i][j]) ;

            }
        }
    }
}

}






        

