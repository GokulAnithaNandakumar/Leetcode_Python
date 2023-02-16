class Solution:
    def numberOfSteps(self, num: int) -> int:
        def even(num) -> int:
            if num%2 == 0:
                return True
            else:
                return False
        if num == 0:
            return 0
        else:
            a = 0
            while num != 0:
                if even(num) == True:
                    num = num//2
                    a+=1
                else:
                    num = (num-1)//2
                    a+=2
            return a-1