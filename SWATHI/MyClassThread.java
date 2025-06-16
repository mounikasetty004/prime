/*class  MyClassThread implements Runnable {//extends Thread
    public void run(){
        System.out.println("Thread is executed");
    }
    public static void main(String[] args){
        MyClassThread e1=new MyClassThread();
        Thread v=new Thread(e1);//when extends use it is no need
        v.setName("swathi");//e1.setNmae("hi")
        System.out.println(v.getName());//e1.getName
        v.start();*/
class  MyClassThread implements Runnable {//extends Thread
        public void run(){
                for(int i=0;i<10;i++){
                    if(i%2==0){
                        try{
                            Thread.sleep(1000);
                            System.out.println(i);
                            
                        }
                        catch(Exception e){
                            System.out.println(e);
                        }
                       
                    }
                  
                    
                }
                System.out.println(Thread.currentThread().getName());
            }
        public static void main(String[] args){
                MyClassThread e1=new MyClassThread();
                Thread v=new Thread(e1);//when extends use it is no need
                v.setName("swathi");//e1.setNmae("hi")
                System.out.println(v.getName());//e1.getName
                //System.out.println(v.isAlive());//flase
                //System.out.println(Thread.currentThread());

                v.start();
                System.out.println(v.isAlive());//true
              //  System.out.println(Thread.currentThread().getName());
       
    }
    
}
