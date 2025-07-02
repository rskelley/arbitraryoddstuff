public class Funcky {

    public static void sayHello() {
        sayHello("starshine");
    }

    public static void sayHello(String name) {
        System.out.println("Good morning "+name+" the earth says 'Hello'");
        name = "Ha Ha, I changed you";
    }


    public static void sayHelloYou(String name) {
        System.out.println("Hello, "+name+" I hope you're enjoying programming");
        name = "Ha Ha, I changed you";
    }

    public static Double calcPower(int base, int exponent) {
        Double result = Math.pow(base, exponent);
        System.out.println("The value of " + base + " to the " + exponent + " power is: ");
        System.out.println(result);
        return result;
    }

    public static void printArray(int[] neo) {
        for(int val : neo) {
            System.out.println(val);
        }
        neo[0] = -42;
    }


    public static void main(String args[]) {
        // String userName = "Mr. Nimoy";
        // String brokeMyShip = "KHAAAAAAAN";
        // sayHello();
        // sayHelloYou(userName);
        // sayHello(userName);
        // sayHelloYou(brokeMyShip);
        // System.out.println(brokeMyShip);
        Double myVar = 0.0;
        myVar = calcPower(2, 10);
        myVar = 2*myVar;
        System.out.println("2 x the previous value is "+myVar);
        int[] myAr = {0,1,2,3};
        printArray(myAr);
        printArray(myAr);
        System.out.println("Done");
    }
}