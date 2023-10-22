from itertools import combinations

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        d = {
            "2": ["a","b","c"],
            "3": ["d","e","f"],
            "4": ["g","h","i"],
            "5": ["j","k","l"],
            "6": ["m","n","o"],
            "7": ["p","q","r","s"],
            "8": ["t","u","v"],
            "9": ["w","x","y","z"]
        }

        res = []
        curr = []
        
        def backtrack(start):
            if start == len(digits):
                res.append("".join(curr))
            
            else:
                for letter in d[digits[start]]:
                    curr.append(letter)
                    backtrack(start+1)
                    curr.pop()
        
        if not digits: return []
        backtrack(0)
        return res
        

s = Solution()
print(s.letterCombinations("234"))

# [
# "adg","adh","adi","aeg","aeh","aei","afg","afh","afi",
# "bdg","bdh","bdi","beg","beh","bei","bfg","bfh","bfi",
# "cdg","cdh","cdi","ceg","ceh","cei","cfg","cfh","cfi"
# ]


            # """
            # g       h         i
            # dg      dh        di
            # adg     adh       adi
            
            # g       h         i
            # eg      eh        ei
            # aeg     aeh       aei
            
            # g       h         i
            # fg      fh        fi
            # afg     afh       afi
            
            # """