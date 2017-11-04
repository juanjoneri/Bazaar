import java.io.*;
import java.util.*;

public class Genetic {

    public static void main(String[] args) {
        String[] bank = {"GAAAAAAA", "AAGAAAAA", "AAAAGAAA", "GGAAAAAA", };

        int a = findMutationDistance("AAAAAAAA", "GGAAAAAA", bank);
        System.out.println("The distance is ");
        System.out.println(a);

    }

    public static int findMutationDistance(String start, String end, String[] bank) {

        Map<String, Integer> lpath = new HashMap<>();

        for (String word : bank) {
            lpath.put(word, -1);
        }

        if (!lpath.containsKey(end)) {
            return -1;
        }

        Queue<String> lqueue = new LinkedList<>();
        int counter = -1;
        lqueue.add(start);
        lpath.put(start, 0);

        while (!lqueue.isEmpty()) {
            String current = lqueue.poll();
            int pathSoFar = lpath.get(current);
            lpath.remove(current);
            if (current.equals(end)) {
                return pathSoFar;
            }
            List<String> next = nextWords(current, lpath);

            for (String word : next) {
                lpath.put(word, pathSoFar + 1);
                lqueue.add(word);
            }

        }
        return -1;
    }

    public static List<String> nextWords(String current, Map<String, Integer> lpath) {

        char[] tokens = {'A', 'C', 'T', 'G'};
        List<String> result = new LinkedList<>();
        for (int li = 0; li < current.length(); ++li) {
            char[] array = current.toCharArray();
            for (char c : tokens) {
                if (c == array[li]) { continue; }
                array[li] = c;
                String str = new String(array);
                if (lpath.containsKey(str)) { result.add(str); }
            }
        }
        return result;
    }

}
