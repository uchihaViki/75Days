class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        
        carry = 1
        digits[-1] = 0
        i = len(digits) - 2
        while i >= 0 and carry != 0:
            if digits[i] + carry > 9:
                digits[i] = 0
            else:
                digits[i] += carry
                carry = 0
            i -= 1
        if carry != 0:
            digits = [1] + digits
        return digits