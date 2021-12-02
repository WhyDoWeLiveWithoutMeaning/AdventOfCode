package y21.Day1.P1;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner in = new Scanner(new File("y21\\Day1\\input.txt"));
        int total = 0;
        int curr = in.nextInt();
        while(in.hasNextInt()) {
            int next = in.nextInt();
            if(curr < next) {
                total++;
            }
            curr = next;
        }
        System.out.println(total);
    }
}