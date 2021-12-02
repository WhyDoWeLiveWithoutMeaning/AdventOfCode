package y20.Day1.P1;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner in = new Scanner(new File("y20\\Day1\\input.txt"));

        ArrayList<Integer> input = new ArrayList<Integer>();

        while (in.hasNextInt()) input.add(in.nextInt());
        for (int i=0;i<input.size();i++) {
            for (int j=i+1;j<input.size();j++) {
                if (input.get(i) + input.get(j) == 2020) {
                    System.out.println(input.get(i) * input.get(j));
                    return;
                }
            }
        }
    }
}