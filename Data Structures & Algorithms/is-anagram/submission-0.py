class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t): 
            return False

        sorted_s = sorted(s)
        sorted_t = sorted(t)

        print(sorted_s, sorted_t)

        for i in range(len(s)) :
            print(i)
            if sorted_s[i] != sorted_t[i]: 
               return False
        
        return True

            


        

