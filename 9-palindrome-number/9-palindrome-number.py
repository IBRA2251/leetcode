class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        arrx=[]
        while x>=1:
            arrx.append(x%10)
            x= int(x/10)
        same= True
        arry= arrx[::-1]
        for r in range(len(arrx)):
            if arrx[r] != arry[r]:
                same= False
                break
        return same