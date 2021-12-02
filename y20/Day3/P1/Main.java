package y20.Day3.P1;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner in = new Scanner(new File("y20\\Day3\\input.txt"));

        //Pre-Processing
        String initialLine = in.nextLine();
        ArrayList<ArrayList<Boolean>> arr =  new ArrayList<ArrayList<Boolean>>();
        arr.add(new ArrayList<Boolean>());
        for(char a : initialLine.toCharArray()) arr.get(0).add(a == '.' ? false : true);
        while(in.hasNextLine()){
            ArrayList<Boolean> b = new ArrayList<Boolean>();
            String line = in.nextLine();
            for(char a : line.toCharArray()) b.add(a == '.' ? false : true);
            arr.add(b);
        }

        //Processing
        int x = 0;
        int y = 0;

    }
}

