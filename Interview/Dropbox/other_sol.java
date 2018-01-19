import java.util.*;

public class UncoolCows{

  static class Folder {
    private int id;
    private boolean secret;
    private Set<Integer> members;

    public Folder(int id, boolean secret, HashSet<Integer> members){
      this.id = id;
      this.secret = secret;
      this.members = members;
    }

    public boolean isSecret(){
      return secret;
    }

    public boolean idInMembers(int id){
      return members.contains(id);
    }
  }

  static class Node {
    private List<Node> children = new ArrayList<Node>();
    private Node parent = null;
    private Folder data = null;

    public Node(Folder data) {
        this.data = data;
    }

    public void setParent(Node parent) {
        parent.addChild(this);
        this.parent = parent;
    }

    public void addChild(Node child) {
        child.setParent(this);
        this.children.add(child);
    }

    public Node getParent(){
      return parent;
    }

    public List<Node> getChildren(){
      return children;
    }

    public boolean checkAccess(int cow){
      if(data.isSecret()){
        return data.idInMembers(cow);
      } else {
        Node pointer = this;
        //we'll repeatedly look higher up all the way to our root folder
        //in order to see if our cow has access to our original folder
        while (pointer != null){
          if (pointer.data.idInMembers(cow)){
            return true;
          }
          pointer = pointer.getParent();
        }
        return false;
      }
    }
  }

  public static void main(String[] args){
    //I can't remember exactly what the input format is
    //but the general idea was: First I get Q? representing number of cows.

    //Then I would be given 2 numbers (M N) meaning M shared folders and N secret folders I think?
    //Each line corresponding to a folder would have in space delimited format (id, # of members, and then cow id's space incremented)

    //And then finally a number G which is number of relations
    //Each line corresponding to a relation would be (parent_folder_id child_folder_id)

    //The ultimate goal was to find all the cows that didn't have access to every leaf in the tree file hierarchy structure
    //These cows being deemed as "uncool" or something?

    Scanner in = new Scanner(System.in);
    int numCows = in.nextInt(); //first line Q

    int numShared = in.nextInt(); // M
    int numSecret = in.nextInt(); // N
    //there are M+N folders and each folder should have a corresponding id from 1 to M+N
    Node[] folders = new Node[numShared+numSecret];

    for(int i = 0; i < numShared + numSecret; i++){
      String[] line = in.nextLine().split(" ");

      int id = Integer.parseInt(line[0]);
      boolean secret = (i < numShared) ? false : true;
      HashSet<Integer> members = new HashSet<Integer>();
      for(int index = 2; index < line.length; index++){
        members.add(Integer.parseInt(line[index]));
      }
      
      Folder f = new Folder(id, secret, members);
      folders[id] = new Node(f);
    }

    int numRelations = in.nextInt(); //G number that is how many lines of relations we'll have
    for(int i = 0; i < numRelations; i++){
      int parent = in.nextInt();
      int child = in.nextInt();
      folders[parent].addChild(folders[child]);
    }

    ArrayList<Node> leafs = new ArrayList<Node>();
    for(Node node : folders){
      if (node.getChildren().size() == 0) {
        leafs.add(node);
      }
    }

    //Now that pre-processing is finished, we go through each cow to see if it has access to all leaf nodes in tree
    //if not print it out
    for(int cow = 0; cow < numCows; cow++){
      for(Node leaf : leafs){
        if (!leaf.checkAccess(cow)){
          System.out.println(cow); //cow did not have access to this particular leaf and so is outed as uncool
          break;
        }
      }
    }
  }
}
