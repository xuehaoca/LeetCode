class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = list()
        l0 = list()
        l1 = list()
        s1 = '()'
        l0.append(s1)
        s21 = s1 + s1
        s22 = '(' +s1+ ')'
        
        l1.append(s22)
        l1.append(s21)
        res.append(l0)
        res.append(l1)
        
        if(n>2):
            for i in range(2,n):
                k = 0
                while(k < i-1):
                    lk = list()
                    res.append(lk)
                    t = i-k-1
                    l = list()
                    left = len(res[k])
                    right = len(res[t])
                    print k,t,i
                    for m in range(0,left):
                        for c in range(0,right):
                            flag = 1
                            flag2 = 1
                            strn = res[k][m] + res[t][c]
                            strn2 = res[t][c] + res[k][m]
                            check = len(res[i])
                            for jj in range(0,check):
                                if strn == res[i][jj]:
                                    flag = 0
                                    break
                            for jj in range(0,check):
                                if strn2 == res[i][jj]:
                                    flag2 = 0
                                    break
                            if(strn == strn2):
                                flag2 = 0
                            if(flag != 0):
                                res[i].append(strn)
                            if(flag2 != 0):
                                res[i].append(strn2)
                            
                    k = k + 1
                last = len(res[i-1])
                for g in range(0,last):
                    str3 = '(' + res[i-1][g] + ')'
                    res[i].append(str3)
                print res[i]
            return res[i]
        else:
            return res[n-1]
        
