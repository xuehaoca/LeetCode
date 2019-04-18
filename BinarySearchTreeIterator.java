/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class BSTIterator {
    private LinkedList<Integer> list = new LinkedList<>();
    private int count=0 ;
    public BSTIterator(TreeNode root) {
        get(root);
    }
    public void get(TreeNode root){
        if(root !=null){
            get(root.left);
            list.add(root.val);
            get(root.right);
        }
    }
    /** @return the next smallest number */
    public int next() {
        if((count >= 0) && (count <list.size())){
            int temp = list.get(count);
            count++;
            return temp;
        }
        else return 0;
    }
    
    /** @return whether we have a next smallest number */
    public boolean hasNext() {
        if(count <list.size()){
            return true;
        }
        else return false;
    }
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator obj = new BSTIterator(root);
 * int param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */