package y21.Day1.P2;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner in = new Scanner(new File("y21\\Day1\\input.txt"));
        int total = 0;
        int a = in.nextInt();
        int b = in.nextInt();
        int c = in.nextInt();
        while(in.hasNextInt()) {
            int d = in.nextInt();
            if(a + b + c < b + c + d) {
                total++;
            }
            a = b;
            b = c;
            c = d;
        }
        System.out.println(total);
    }
}