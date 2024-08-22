def isValid(s):
        stack=[]
        for i in s:
            if i=='(':
                stack.append(i)
            if i=='{':
                stack.append(i)
            if i=='[':
                stack.append(i)
            if i==')':
                if '(' in stack and stack[-1]=='(':
                    stack.remove('(')
            if i=='}':
                if '{' in stack and stack[-1]=='{':
                    stack.remove('{')
            if i==']':
                if '[' in stack and stack[-1]=='[':
                    stack.remove('[')
        if len(s)==1 and (s==')' or s=='}' or s==']'):
            return False
        if len(stack)==0:
            return True
        else:
            return False
        
s="[({[})]"
print(isValid(s))