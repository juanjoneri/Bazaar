import java.io.*;
import java.util.*;

/*
Input:
q(int)
m(number of shared lines) n(number of confidencial lines)
-folderID(int) [folderMembers(int) cows] #use id as hash for folder with cow members
-folderID(int) [folderMembers(int) cows]
-...
g(number of lines)
-u v

*/
public class Solution {

public static void main(String args[] ) throws Exception {
        Solution sol = new Solution();
        BufferedReader s = new BufferedReader(new InputStreamReader(System.in));

        // first line
        int q = Integer.parseInt(s.readLine());

        // second line
        String[] secondLine = s.readLine().split(" ");
        int m = Integer.parseInt(secondLine[0]);
        int n = Integer.parseInt(secondLine[1]);

        Map<Integer, Folder> folders = new HashMap<>();
        Set<Integer> cows = new HashSet<>();

        // next m lines --> shared
        for (int i = 0; i < m; i++) {
                String[] nextLine = s.readLine().split(" ");
                int folderID = Integer.parseInt(nextLine[0]);

                String[] folderMembers = Arrays.copyOfRange(nextLine, 2, nextLine.length);
                int[] members = new int[folderMembers.length];
                for (int j = 0; j < members.length; j++) {
                        members[j] = Integer.parseInt(folderMembers[j]);
                        // build list of cows
                        cows.add(members[j]);
                }

                folders.put(folderID, sol.new Folder(true, members));
        }

        // next n lines --> confidential
        for (int i = 0; i < n; i++) {
                String[] nextLine = s.readLine().split(" ");
                int folderID = Integer.parseInt(nextLine[0]);

                String[] folderMembers = Arrays.copyOfRange(nextLine, 2, nextLine.length);
                int[] members = new int[folderMembers.length];
                for (int j = 0; j < members.length; j++) {
                        members[j] = Integer.parseInt(folderMembers[j]);
                        // build list of cows
                        cows.add(members[j]);
                }

                folders.put(folderID, sol.new Folder(false, members));
        }

        // next line
        int g = Integer.parseInt(s.readLine());

        // next g lines
        for (int i = 0; i < g; i++) {
                String[] nextLine = s.readLine().split(" ");
                int u = Integer.parseInt(nextLine[0]);
                int v = Integer.parseInt(nextLine[1]);

                Folder parent = folders.get(u);
                Folder child = folders.get(v);

                // set up parent/child relationship
                parent.addChild(child);

                // update member lists to include inheritence
                if (child.shared) {
                        for (int mem : parent.members) {
                                child.addMember(mem);
                        }
                }
        }

        Set<Integer> uncoolCows = new TreeSet<>();

        // traverse map of folders
        for (Map.Entry<Integer, Folder> entry : folders.entrySet()) {
                Folder f = entry.getValue();

                // only check leaf folders (folders with no children)
                if (f.child == null) {
                        List<Integer> membersCopy = new ArrayList<>();
                        membersCopy.addAll(f.members);

                        List<Integer> cowsCopy = new ArrayList<>();
                        cowsCopy.addAll(cows);

                        // find all cows that can't access this leaf folder
                        cowsCopy.removeAll(membersCopy);
                        // add all those cows to the list of uncool cows
                        uncoolCows.addAll(cowsCopy);
                }
        }

        for (int c : uncoolCows) {
                System.out.print(c + " ");
        }
}

public class Folder {
public boolean shared;
public Set<Integer> members;
public Folder child;

public Folder(boolean shared, int[] members) {
        this.shared = shared;
        this.members = new HashSet<>();
        for (int m : members) {
                this.members.add(m);
        }
        this.child = null;
}

public void addMember(int member) {
        this.members.add(member);
}

public void addChild(Folder child) {
        this.child = child;
}
}
}
