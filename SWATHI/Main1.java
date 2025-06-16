class Main1
{
    static int a=3;
    static int b;
    static void meth(int x)
    {
        System.out.println("x="+x);
        System.out.println("a="+a);
        System.out.println("b="+b);
    }
    static 
    {
        b=a*4;
        System.out.println("static block"+b);
    }
    public static void main(String[] args) {
        meth(55);
    }
}
