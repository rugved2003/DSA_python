class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ''
        for digit in digits:
            string += str(digit)
        number = int(string) +1
        ans = []
        for digit in str(number):
            ans.append(int(digit))
        return ans
