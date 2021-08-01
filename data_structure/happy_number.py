class Solution:
    def isHappy(self, n: int) -> bool:
        digits_sum = 0
        s = set()
        while True:
            while n > 0:
                digit_num = n % 10
                digits_sum = digits_sum + digit_num^2
                n = n//10
            n = digits_sum
            if n == 1:
                return True
            elif digits_sum in s:
                return False
            else:
                s.add(digits_sum)
