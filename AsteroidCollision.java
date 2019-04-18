import java.lang.Math;
class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Stack<Integer> ss = new Stack<>();
        int le = asteroids.length;
        for ( int i = 0; i < le; i++){
            if(ss.isEmpty()){
                ss.push(asteroids[i]);
            }
            else if((asteroids[i] > 0 && ss.peek()>0) ||(asteroids[i] <0 && ss.peek()<0)){
                ss.push(asteroids[i]);
            }else if(asteroids[i] > 0 && ss.peek()<0) {
                ss.push(asteroids[i]);                
            }
            else{
                int flag = 0;
                while(ss.size()>0 &&(ss.peek()*asteroids[i])<0){
                    int temp = ss.peek();
                    if (Math.abs(temp) <= Math.abs(asteroids[i])){
                        ss.pop();
                        if(Math.abs(temp) == Math.abs(asteroids[i])){
                            flag = 1;
                            break;
                        }
                        else{
                            if(ss.size()==0){
                                ss.push(asteroids[i]);
                                flag = 1;
                            }
                        }
                    }
                    else{
                        break;
                    }
                }
                if(ss.size()>0 &&(ss.peek()*asteroids[i])>0&&flag !=1){
                    ss.push(asteroids[i]);
                }
            }
        }
        int [] res = new int[ss.size()];
        for (int i = ss.size()-1;i>=0;i--){
            res[i] = ss.pop();
        }
        return res;
    }  
}