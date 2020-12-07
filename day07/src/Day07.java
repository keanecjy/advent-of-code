import static java.lang.Integer.parseInt;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day07 {

    private final Map<String, Map<String, Integer>> map = new HashMap<>();

    public static void main(String[] args) {
        try {
            String filePath = System.getProperty("user.dir") + "\\Day07Input.txt";
            BufferedReader bufferedReader = new BufferedReader(new FileReader(filePath));
            Day07 day07 = new Day07();
            day07.initializeGraph(bufferedReader);
            day07.solvePartOne();
            day07.solvePartTwo();
        } catch (IOException e) {
            System.out.println("Error reading file: " + e.getMessage());
        }
    }

    public void initializeGraph(BufferedReader bufferedReader) throws IOException {
        String s = bufferedReader.readLine();
        while (s != null) {
            Pattern pattern = Pattern.compile("^(.+) bags contain (.+)\\.$");
            Matcher matcher = pattern.matcher(s);

            if (!matcher.find()) {
                throw new IllegalArgumentException("Invalid string in file: " + s);
            }
            String pointer = matcher.group(1);
            String pointedTo = matcher.group(2);
            String[] arr = pointedTo.split(", ");
            HashMap<String, Integer> innerMap = new HashMap<>();
            for (String value : arr) {
                Pattern innerPattern = Pattern.compile("^(\\d+) (.+) bags?$");
                Matcher matched = innerPattern.matcher(value);
                if (matched.find()) {
                    innerMap.put(matched.group(2), parseInt(matched.group(1)));
                }
            }
            if (!innerMap.isEmpty()) {
                map.put(pointer, innerMap);
            }
            s = bufferedReader.readLine();
        }
    }

    int count = 0;
    public void solvePartOne() {
        depthFirstSearch("shiny gold", new HashSet<>());
        System.out.println(count);
    }

    public void depthFirstSearch(String query, HashSet<String> visited) {
        for (String parent : map.keySet()) {
            if (!visited.contains(parent)) {
                Map<String, Integer> children = map.get(parent);
                if (children.containsKey(query)) {
                    visited.add(parent);
                    count++;
                    depthFirstSearch(parent, visited);
                }
            }
        }
    }

    int total = 0;
    public void solvePartTwo() {
        depthFirstSearch2("shiny gold", 1);
        System.out.println(total);
    }

    public void depthFirstSearch2(String query, int accum) {
        if (map.containsKey(query)) {
            Map<String, Integer> innerMap = map.get(query);
            for (String s : innerMap.keySet()) {
                int value = innerMap.get(s) * accum;
                total += value;
                depthFirstSearch2(s, value);
            }
        }
    }

}
