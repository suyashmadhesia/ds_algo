from typing import List


class Solution:
    def is_palindrome(self, i, j, s):
        # Helper function to check if the substring s[i:j+1] is a palindrome
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        self.ans = []  # Stores all the valid palindrome partitions
        self.temp = [] # Temporary list to hold current partition/substrings

        def subsets(i):
            # Base Case: If we've processed the whole string
            if i >= len(s):
                # Append a copy of the current valid partition to the answer
                self.ans.append(self.temp[:])
                return

            # Try all substrings starting from index i to the end
            for j in range(i, len(s)):
                # Check if the substring s[i..j] is a palindrome
                if self.is_palindrome(i, j, s):
                    # If yes, include it in the current partition path
                    self.temp.append(s[i:j+1])

                    # Recurse to find further palindromic partitions from index j+1
                    subsets(j + 1)

                    # Backtrack: remove the last added substring to explore other possibilities
                    self.temp.pop()

        # Start the recursive partitioning from index 0
        subsets(0)

        # Return the list of all valid palindrome partitions
        return self.ans


print(list(zip(['a', 'b', 'c'], ['w', 'x', 'y', 'z'])))