import java.lang.String;
class Solution {
    public boolean backspaceCompare(String S, String T) {
        
        String ans1 = this.process(S);
        String ans2 = this.process(T);
        System.out.println(ans1);
        System.out.println(ans2);
        if(ans1.equals(ans2)){
            return true;
        }
        else return false;
    }
    public String process(String a){
        Stack<Character> aa = new Stack<Character>();
        char [] ac = a.toCharArray();
        String ans="";
        for(char each : ac){
            if(each!='#'){
                aa.push(each);
                //System.out.println(each);
                continue;
            }
            else{
                if(aa.size()>0){
                    aa.pop();
                }
                else continue;
            }
        }
        for (Character eac : aa){
            ans+=eac;
            //System.out.println(ans);
        }
        return ans;
    }
}