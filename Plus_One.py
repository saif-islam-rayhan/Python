class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        n = len(digits)
        
        # Add carry starting from the last digit
        for i in range(n - 1, -1, -1):
            total = digits[i] + carry
            digits[i] = total % 10
            carry = total // 10
            if carry == 0:
                # No more carry to propagate
                break
        
        # If there's still a carry (e.g., [9,9] → [0,0] with carry=1), prepend it
        if carry:
            digits.insert(0, carry)
        
        return digits
