# Create a Python reference file for Cantor's Diagonalization.
"""
# 🧠 Cantor’s Diagonalization — Practical Reference (Python)

## 🔍 Goal
Construct an object (usually a string/sequence) that **cannot** be in a given list by ensuring it differs from the *i-th* item at the *i-th* position.
This guarantees the constructed object avoids the entire list.

---

## ✅ When to Use
- You have **n strings of length n** (or a square list of sequences).
- You need **any string not in the list** (e.g., LeetCode 1980 style problem).
- You want to **prove a list can’t be complete** (finite or infinite variants).
- You need a construction that **differs from every listed item in at least one place**.

---

## 🧩 Core Idea (Finite Version)
Arrange the n strings into an n×n grid.
Take the diagonal bits/characters: the i-th character of the i-th string.
**Flip/modify each diagonal character** using a predetermined rule.
The result **differs from string i at position i**, so it’s not equal to any listed string.

---

## 🧠 Examples
### Binary Strings (LeetCode 1980)
Given `nums` with `n` unique binary strings of length `n`, return any binary string of length `n` **not** present in `nums`.

**Diagonal construction (O(n))**:
- For each `i`, look at `nums[i][i]`.
- Flip `'0'↔'1'` and append.
- The resulting string is guaranteed not to be in `nums`.

### General Strings
If characters aren’t binary, pick a **deterministic alternate character** at each diagonal position (e.g., cycle through an alphabet and choose the next distinct symbol different from the diagonal one).

---

## 🧮 Complexity
- **Time:** O(n)
- **Space:** O(1) auxiliary (O(n) for the output)

---

## 🧪 Why It Works (Intuition)
By construction, the result differs from `nums[i]` at index `i` for all `i`.
Therefore it can’t match any `nums[i]` and hence can’t be in the list.

---

## 🔧 Contents
- `find_different_binary_string(nums)` — canonical O(n) solution for binary strings.
- `diagonal_construct(strings, pick_alt)` — general diagonalizer for arbitrary alphabets.
- `pick_alt_binary(ch)` — helper to flip `'0'/'1'`.
- `pick_alt_from_alphabet(ch, alphabet)` — helper for general alphabets.
- Self-tests & demos in the `__main__` block.

---
"""


from typing import Callable, Iterable, List, Sequence


# -----------------------------
# Binary-specialized version
# -----------------------------
def find_different_binary_string(nums: List[str]) -> str:
    """
    Return a binary string of length n not present in `nums` (n strings, each length n).
    Uses Cantor's diagonalization: flip the diagonal bit at each index.
    Time: O(n), Space: O(1) aux

    Example:
        nums = ["01", "10"]  -> returns "11" (or "00" depending on flip rule)
    """
    # Assumes valid input per problem statement: len(nums) == len(nums[0])
    return "".join("1" if s[i] == "0" else "0" for i, s in enumerate(nums))


# -----------------------------
# General-purpose diagonalizer
# -----------------------------
def diagonal_construct(
    strings: Sequence[Sequence[str]],
    pick_alt: Callable[[str, int], str],
) -> str:
    """
    Construct a new string by taking the i-th char from the i-th string and
    applying `pick_alt` to obtain a different character.

    Parameters:
        strings: a sequence (length n) of sequences (each at least length n).
        pick_alt: function(old_char, index) -> new_char != old_char

    Returns:
        A string (length n) that differs from strings[i] at position i for all i.

    Notes:
        - Works for any alphabet; caller must ensure `pick_alt` returns
          a character distinct from the given diagonal character.
        - If strings[i] is shorter than i+1, raises IndexError.
    """
    out_chars = []
    for i, s in enumerate(strings):
        ch = s[i]
        out_chars.append(pick_alt(ch, i))
    return "".join(out_chars)


# -----------------------------
# Helpers for pick_alt
# -----------------------------
def pick_alt_binary(ch: str, _: int) -> str:
    """Flip '0' <-> '1'. Raises ValueError for non-binary input."""
    if ch == "0":
        return "1"
    if ch == "1":
        return "0"
    raise ValueError(f"Non-binary character encountered: {ch!r}")


def pick_alt_from_alphabet(ch: str, _: int, alphabet: Iterable[str] = ("a", "b", "c")) -> str:
    """
    Choose a deterministic alternative character from the given alphabet
    that is not equal to `ch`. If alphabet has just one symbol equal to `ch`,
    this raises a ValueError.
    """
    for cand in alphabet:
        if cand != ch:
            return cand
    raise ValueError("Alphabet must contain at least one character different from the input.")


# -----------------------------
# Minimal checks / demos
# -----------------------------
if __name__ == "__main__":
    # --- Binary examples ---
    nums1 = ["01", "10"]
    ans1 = find_different_binary_string(nums1)
    print("Example 1:", nums1, "->", ans1)
    assert ans1 not in set(nums1) and len(ans1) == len(nums1)

    nums2 = ["00", "01"]
    ans2 = find_different_binary_string(nums2)
    print("Example 2:", nums2, "->", ans2)
    assert ans2 not in set(nums2) and len(ans2) == len(nums2)

    nums3 = ["111", "011", "001"]
    ans3 = find_different_binary_string(nums3)
    print("Example 3:", nums3, "->", ans3)
    assert ans3 not in set(nums3) and len(ans3) == len(nums3)

    # --- General alphabet example ---
    # Using small alphabet {"a","b","c"}; pick the first symbol different from the diagonal.
    strings = ["abc", "bac", "caa"]
    # Diagonal is (a, a, a) -> pick 'b' for each -> "bbb"
    out_general = diagonal_construct(strings, lambda ch, i: pick_alt_from_alphabet(ch, i, ("a", "b", "c")))
    print("General example:", strings, "->", out_general)
    # Verify it differs from every row at position i
    for i, row in enumerate(strings):
        assert out_general[i] != row[i]

    print("All checks passed ✅")