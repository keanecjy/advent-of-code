package day08;

import java.awt.event.WindowStateListener;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashSet;
import java.util.ArrayList;
import java.util.List;

public class Day08 {

    private ArrayList<String> instructions = new ArrayList<>();

    public static void main(String[] args) {
        try {
            String filePath = System.getProperty("user.dir") + "/src/day08/Day08Input.txt";
            BufferedReader bufferedReader = new BufferedReader(new FileReader(filePath));
            Day08 day08 = new Day08();
            day08.storeInstructions(bufferedReader);
            // int val = day08.runPartOne();
            // System.out.println(val);
            day08.runPartTwo();
        } catch (IOException e) {
            System.out.println("Error reading file: " + e.getMessage());
        }
    }

    public void storeInstructions(BufferedReader bufferedReader) throws IOException {
        String s = bufferedReader.readLine();
        while (s != null) {
            instructions.add(s);
            s = bufferedReader.readLine();
        }
    }

    public int runPartOne(List<String> instructions) {
        int lineNumber = 0;
        int accum = 0;
        HashSet<Integer> instructionsExecuted = new HashSet<>();
        while (lineNumber < instructions.size()) {
            if (instructionsExecuted.contains(lineNumber)) {
                return accum;
            } else {
                instructionsExecuted.add(lineNumber);
            }
            String inst = instructions.get(lineNumber);
            String instType = inst.substring(0, 3);
            int arg = Integer.parseInt(inst.substring(4));
            switch (instType) {
            case "acc":
                accum += arg;
                lineNumber++;
                break;
            case "jmp":
                lineNumber += arg;
                break;
            case "nop":
                lineNumber++;
                break;
            }
        }
        System.out.println("No loop and accum is: " + accum);
        return accum;
    }

    public void runPartTwo() {
        for (int i = 0; i < instructions.size(); i++) {
            String inst = instructions.get(i);
            String instType = inst.substring(0, 3);
            if (instType.equals("nop")) {
                List<String> newInstructions = new ArrayList<>(instructions);
                newInstructions.set(i, inst.replace("nop", "jmp"));
                runPartOne(newInstructions);
            } else if (instType.equals("jmp")) {
                List<String> newInstructions = new ArrayList<>(instructions);
                newInstructions.set(i, inst.replace("jmp", "nop"));
                runPartOne(newInstructions);
            }
        }
    }

}
