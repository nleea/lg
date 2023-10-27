class Solution:
    def generateParenthesis(self, n: int) -> list[str]:

        if n <= 0:
            return []
        
        if n == 1:
            return ["()"]

        generate = []
        
        def back(left,right,parenthesis,list):
            
            if left == 0 and right == 0:
                list.append(parenthesis)
                return

            if left > 0:
                back(left-1,right+1,parenthesis + "(",list)
            
            if right > 0:
                back(left,right-1,parenthesis + ")",list)
        
        back(n,0,"",generate)

        return generate

"""  (
    / \
   ((  ()
  / \    \
((( (()  ()(
 /   \     \    \
((() (())  ()() ()(( 
 /     \     \      \
((()) (())() ()()() ()(()
 \      
((()))  
 """
 
s = Solution()
print(s.generateParenthesis(3))