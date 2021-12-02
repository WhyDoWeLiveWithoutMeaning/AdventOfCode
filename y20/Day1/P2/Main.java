package y20.Day1.P2;

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
                for (int k=i+2;k<input.size();k++) {
                    if (input.get(i) + input.get(j) + input.get(k) == 2020) {
                        System.out.println(input.get(i) * input.get(j) * input.get(k));
                        return;
                    }
                }
            }
        }
    }
}
