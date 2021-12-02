package y21.Day2.P2;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner in = new Scanner(new File("y21\\Day2\\input.txt"));
        long depth = 0, position = 0, aim = 0;
        while(in.hasNextLine()){
            String action = in.next();
            long units = in.nextLong();
            if(action.equals("forward")) {
                position+=units; 
                depth+=aim*units;
            }
            else if(action.equals("down")) 
                aim+=units;
            else 
                aim-=units;
        }
        System.out.println(depth*position);
    }
}