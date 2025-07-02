# Leetcode no 71 : Simplify Path

class Solution(object):
    def simplifyPath(self, path):
        parts = path.split('/')
        
        stack = []
        stack.append("/")
        del parts[0]
        for part in parts:
            if len(part) == 0 :
                continue
            if part == ".":
                continue 
            elif part == "..":
                if stack[-1] != "/":
                    stack.pop()
            else:
                stack.append(part)
            
              
        final = ""
        
        # while len(stack) >1:
        for i  in range(len(stack)-1)  :
            if i == len(stack) -2 or i ==0:
                final += stack[i]  
            elif stack[i] =='':
                    continue 
            else:
                final = final+stack[i] +"/"
            # string = stack.pop()
            # if string=="/" and stack[-1] == "/":
            #     final = final + string
            #     stack.pop()
            #     continue
        
        if stack[-1] != "/" and len(stack[-1]) != 0:
            if final[-1] !='/':
                final = final + "/" + stack[-1]
            else: 
                final = final + stack[-1]
        #     final = final + string +"/"
            
        # if len(stack) >0:
        #     string = stack.pop()
        #     if string!= "/":
        #         final = final + string
             
        # final_final = final[::-1]
        if len(final) >0:
            if final[-1] == "/" and len(final) < 1:
                final = final[:-1] 
            
                
        if len(final) ==0:
            final = "/"
        
        return final
    
def main():
    lol = Solution ()
    path = "/home/"
    print(lol.simplifyPath(path))
    
    
if __name__ == '__main__':
    main()
        