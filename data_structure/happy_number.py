class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while True:
            digits_sum = 0
            while n > 0:
                digit_num = n % 10
                digits_sum = digits_sum + digit_num**2
                n = int(n/10)
            n = digits_sum
            if digits_sum == 1:
                return True
            elif digits_sum in s:
                return False
            else:
                s.add(digits_sum)

p = Solution()
print(p.isHappy(19))
