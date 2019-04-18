/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        Stack<TreeNode> stack = new Stack<TreeNode>();
        TreeNode temp = root;
        List<Integer> ans = new ArrayList();
        while(temp != null){
            stack.push(temp);
            temp = temp.left;
        }
        while(stack.size()>0){
            TreeNode temp3 = stack.pop();
            ans.add(temp3.val);
            TreeNode temp2 = temp3.right;
            while(temp2 != null){
                stack.push(temp2);
                temp2 = temp2.left;
            }
        }
        return ans;
    }
}