class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digit_to_letters = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
        }
        def backtrack(index, current_com):
            if index == len(digits):
                com.append(current_com)
                return

            digit = digits[index]
            letters = digit_to_letters[digit]

            for letter in letters:
                backtrack(index+1, current_com + letter)
        com = []
        backtrack(0, "")
        return com

        
