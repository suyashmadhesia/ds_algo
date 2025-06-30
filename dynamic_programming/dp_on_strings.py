from functools import lru_cache

class Solution:
    """
    Dynamic Programming solution for Longest Common Subsequence (LCS).

    We want the longest sequence of characters that appears in both text1 and text2 in the same order
    (but not necessarily consecutively). To build this up, we consider all prefixes of the two strings
    and keep track of the best we can do so far.

    Key idea:
    Let dp[i][j] be the length of the LCS of:
        - the first i characters of text2 (i.e., text2[:i])
        - the first j characters of text1 (i.e., text1[:j])

    Then:
      • If the characters text2[i-1] and text1[j-1] match, we can extend the LCS of the prefixes
        by 1:
            dp[i][j] = dp[i-1][j-1] + 1
      • Otherwise, we must drop one of the two characters and take the best of those two possibilities:
            dp[i][j] = max(dp[i-1][j],   # drop text2[i-1]
                           dp[i][j-1])   # drop text1[j-1]

    Initialization:
      - dp[0][j] = 0 for all j (empty text2 has no common subsequence)
      - dp[i][0] = 0 for all i (empty text1 has no common subsequence)

    Final answer: dp[n2][n1], where n1 = len(text1), n2 = len(text2).

    Time Complexity: O(n1 * n2)
    Space Complexity: O(n1 * n2)
    """
    def longestCommonSubsequenceRescursive(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)
        @lru_cache(None)
        def solve(i, j):
            # Base case: if either index is below 0, one string is "empty" => no common subsequence
            if i < 0 or j < 0:
                return 0
            # If characters match, take it and recurse on both strings shortened by one
            if text1[i] == text2[j]:
                return 1 + solve(i-1, j-1)
            # Otherwise, try skipping a character from one string or the other
            return max(solve(i-1, j), solve(i, j-1))
        
        # Top-down call starting from the end of both strings:
        return solve(n1 - 1, n2 - 1)


    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)

        # Bottom-up DP table: (n2+1) rows for text2, (n1+1) cols for text1
        dp = [[0] * (n1 + 1) for _ in range(n2 + 1)]

        # Fill the table row by row
        for i in range(1, n2 + 1):
            # We're considering text2[:i], so the “new” character is text2[i-1]
            for j in range(1, n1 + 1):
                # We're considering text1[:j], so the “new” character is text1[j-1]
                if text2[i - 1] == text1[j - 1]:
                    # Characters match ➔ extend the LCS of the prefixes by 1
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # No match ➔ best of dropping one character from either string
                    dp[i][j] = max(
                        dp[i - 1][j],  # drop text2[i-1] and keep text1[:j]
                        dp[i][j - 1]   # drop text1[j-1] and keep text2[:i]
                    )

        # The bottom-right cell holds the LCS length for the full strings
        return dp[n2][n1]

def longestPalindromicSubsequence(s1):
    # NOTE: Use longest common subsequnce solution to find longest palindromic subsequence
    '''
    Reverse the string and then find longest common subsequence
    e.g: n = lcs(s1, s1[::-1])
    '''


def longestCommonSubstring(text1, text2):
    '''
    # We're considering text1[:j], so the “new” character is text1[j-1]
    if text2[i - 1] == text1[j - 1]:
        # Characters match ➔ extend the LCS of the prefixes by 1
        dp[i][j] = dp[i - 1][j - 1] + 1
    else:
        dp[i][j] = 0
    
    '''


def minimumInsertionToMakeStringPalindrome(s1):
    '''
    Solve by just n - longestPalindromicSubsequence(s1)
    
    intution: abcaa
    1. take longest palindrome
    a b c a a
    what if we copy bc in reverse order which will give us palindromic string
    a b c a c b a
      - -   - - 
    '''

def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        return n+m - 2 * self.lcs(word1, word2)


class Solution2:
    """
    Distinct Subsequences Problem

    You have:
      - A string `s`
      - A string `t`

    Goal: Count how many **distinct subsequences** of `s` equal `t`.

    A **subsequence** is a sequence that appears in the same relative order, but not necessarily contiguous.

    Intuition:
      - At each position `i` in `s` and `j` in `t`, ask:
        1. “What if I skip s[i]?” → solve the subproblem for s[0…i-1], t[0…j]
        2. “What if I use s[i] (only if s[i] == t[j])?” → solve for s[0…i-1], t[0…j-1]
        3. Sum both ways (only include the second if characters match)
      - Recurse all the way down to base cases.
      - Memoize or tabulate to avoid re-computation.

    Two implementations below:
      • `solve(i, j)` is a top-down recursive solution with memoization (lru_cache)
      • `dp` is a bottom-up tabulation solution
    """

    def numDistinct(self, s: str, t: str) -> int:
        from functools import lru_cache

        # Top-Down Recursive with Memoization
        @lru_cache(None)
        def solve(i: int, j: int) -> int:
            # Base case: If all characters of t matched
            if j < 0:
                return 1
            # Base case: If s is exhausted but t isn't
            if i < 0:
                return 0

            # If current characters match, we can either:
            # - use s[i] → match t[j], move both i and j
            # - or skip s[i] → move i only
            if s[i] == t[j]:
                return solve(i - 1, j - 1) + solve(i - 1, j)
            else:
                # Characters don't match → skip s[i]
                return solve(i - 1, j)

        # Bottom-Up Tabulation (DP)
        dp = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]

        # Base case: empty target t can be matched in exactly 1 way (by deleting all chars)
        for i in range(len(s) + 1):
            dp[i][0] = 1

        # First row already zero-initialized, since empty `s` can't form any non-empty `t`

        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j]

        # Return final answer from tabulation (same as solve(len(s)-1, len(t)-1))
        return dp[len(s)][len(t)]


    def numDistinctOptimized(self, s: str, t: str) -> int:
        """
        Space Optimized Tabulation:
        Instead of using a 2D dp table, we use two 1D arrays:
        - prev[j]: stores dp[i-1][j]
        - curr[j]: stores dp[i][j]

        We update row by row and copy over.
        """
        prev = [0] * (len(t) + 1)
        prev[0] = 1  # Empty t can always be formed by empty s

        for i in range(1, len(s) + 1):
            curr = [0] * (len(t) + 1)
            curr[0] = 1  # Empty target can always be matched

            # Fill current row in reverse to prevent overwriting
            for j in range(len(t), 0, -1):
                if s[i - 1] == t[j - 1]:
                    curr[j] = prev[j] + prev[j - 1]
                else:
                    curr[j] = prev[j]

            prev = curr  # Move to next row

        return prev[len(t)]