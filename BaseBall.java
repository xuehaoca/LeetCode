import java.lang.Integer;
import java.lang.String;
class Solution {
    public int calPoints(String[] ops) {
        int result=0;
        Stack<Integer> s = new Stack<Integer>();
        for(String ss : ops){
            try{
                Integer n = Integer.parseInt(ss);
                s.push(n);
                System.out.println(ss);
            }                
            catch(Exception e){
                System.out.println(ss);
                if(ss.equals("+") ){
                    Integer temp = s.pop();
                    Integer temp2 = temp + s.peek();
                    s.push(temp);
                    s.push(temp2);
                    System.out.println("1");
                }
                else if(ss.equals("C")){
                    s.pop();
                    System.out.println("2");
                }
                else if(ss.equals("D")){
                    s.push(s.peek()*2);
                    System.out.println("3");
                }
            }
        }
        for(Integer i : s){
            result = result + i;
        }
        return result;
    }
}