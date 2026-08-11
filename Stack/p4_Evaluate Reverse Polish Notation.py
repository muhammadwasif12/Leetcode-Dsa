from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in range(len(tokens)):
             if tokens[i] not in ['+','-','*','/']:
                stack.append(int(tokens[i]))
             else:
                b=stack.pop()
                a=stack.pop()
                if tokens[i]=='+':
                    stack.append(a+b)
                elif tokens[i]=='-':
                    stack.append(a-b)
                elif tokens[i]=='*':
                    stack.append(a*b)
                elif tokens[i]=='/':
                    stack.append(int(a/b))
        return stack[0]

s=Solution()
print(s.evalRPN(tokens=["1", "2", "+", "3", "*", "4", "-"]))
