package y21.Day2.P1;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner in = new Scanner(new File("y21\\Day2\\input.txt"));
        int depth = 0, position = 0;

        while(in.hasNextLine()){
            String action = in.next();
            int units = in.nextInt();
            if(action.equals("forward")) position+=units;
            else if(action.equals("down")) depth+=units;
            else depth-=units;
        }
        System.out.println(depth*position);
    }
}