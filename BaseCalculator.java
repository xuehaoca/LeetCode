class Solution {
    public int calculate(String s) {
        Stack<Integer> num = new Stack<Integer>();
        Stack<Character> cha = new Stack<Character>();
        char[] res = s.toCharArray();
        int le = s.length();
        int t = 0;
        for(int i = 0;i<le;i++){
            if(res[i]>='0'&&res[i]<='9'){
                int numt = 0;
                while(i<le&&res[i]>='0'&&res[i]<='9'){
                    numt = numt*10 + (res[i]-'0');
                    i++;
                }
                num.push(numt);
            }
            if(i<le&&res[i] == '('){
                cha.push(res[i]);
            }
            else if (i<le&&res[i] == '+'){
                cha.push(res[i]);
            }
            else if (i<le&&res[i] == '-'){
                cha.push(res[i]);
            }
            else if (i<le&&res[i] == ')'&&cha.peek()!='(' ){
                char tt = cha.pop();
                int s1 = 0;
                while(tt!='('){
                    if(tt=='+'){
                         if(num.size()>0) s1 = num.pop();
                    }
                    else if(tt=='-'){
                         if(num.size()>0) s1 = num.pop()*(-1);
                    }
                    
                    tt = cha.pop();
                    t += s1;
                    
                }
                if(num.size()>0) t += num.pop();
                
                if(cha.size()>0&&cha.peek()=='-') {
                    t *=(-1);
                    cha.pop();
                    cha.push('+');
                }
                num.push(t);
                t = 0;
                
            }else if (i<le&&res[i] == ')'&&cha.peek()=='(' ){
                cha.pop();
                continue;
            }
        }
        while(num.size()>0&&cha.size()>0){
            char g = cha.pop();
            int k = num.pop();
            if (g == '-'){
                k*=(-1);
            }
            t = t + k;
        }
        if(num.size()==1){
            t+=num.pop();
        }
        return t;
    }
}