package y20.Day2.P1;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner in = new Scanner(new File("y20\\Day2\\input.txt"));
        int total = 0;
        while(in.hasNextLine()){
            // Pre Processing
            String[] data = in.nextLine().split(":");
            String[] policy = data[0].split(" ");
            String[] minmax = policy[0].split("-");

            int min = Integer.parseInt(minmax[0]);
            int max = Integer.parseInt(minmax[1]);
            char c = policy[1].charAt(0);
            String password = data[1];

            //Processing
            int charAmount = 0;
            for (int i = 0; i < password.length(); i++) 
                if (password.charAt(i) == c) 
                    charAmount++;

            //Result
            if (charAmount >= min && charAmount <= max) total++;

        }
        System.out.println(total);
    }
}