# Problem 1 - Longest Substring without repeating characters
# Author: Aayush Garg (Agrichain SDET Assignment)
# Here i am solving in 2 ways, simple and advanced

def longest_unique_substring_simple(s: str):
    max_length = 0
    longest_substring = ""

    for i in range(len(s)):
        current = ""
        for j in range(i, len(s)):
            if s[j] in current:
                break
            current += s[j]
            if len(current) > max_length:
                max_length = len(current)
                longest_substring = current
    return longest_substring, max_length


def longest_unique_substring_advanced(s: str):
    seen = set()
    left = 0
    max_length = 0
    longest_substring = ""

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])

        if right - left + 1 > max_length:
            max_length = right - left + 1
            longest_substring = s[left:right+1]

    return longest_substring, max_length


if __name__ == "__main__":
    test_strings = ["abcabcbb", "bbbbb", "pwwkew", "abcdxyz", "aab"]

    print("=== Simple Method Manual Run ===")
    for string in test_strings:
        substring, length = longest_unique_substring_simple(string)
        print(f"Input: {string} | Longest Substring: '{substring}' | Length: {length}")

    print("\n=== Advanced Method Manual Run ===")
    for string in test_strings:
        substring, length = longest_unique_substring_advanced(string)
        print(f"Input: {string} | Longest Substring: '{substring}' | Length: {length}")
