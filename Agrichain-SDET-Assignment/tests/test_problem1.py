import unittest
from problem1 import longest_unique_substring_simple, longest_unique_substring_advanced

class TestLongestSubstring(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(longest_unique_substring_simple("abcabcbb"), ("abc", 3))
        self.assertEqual(longest_unique_substring_simple("bbbbb"), ("b", 1))
        self.assertEqual(longest_unique_substring_simple("pwwkew"), ("wke", 3))
        self.assertEqual(longest_unique_substring_simple("abcdxyz"), ("abcdxyz", 7))
        self.assertEqual(longest_unique_substring_simple("aab"), ("ab", 2))

    def test_advanced(self):
        self.assertEqual(longest_unique_substring_advanced("abcabcbb"), ("abc", 3))
        self.assertEqual(longest_unique_substring_advanced("bbbbb"), ("b", 1))
        self.assertEqual(longest_unique_substring_advanced("pwwkew"), ("wke", 3))
        self.assertEqual(longest_unique_substring_advanced("abcdxyz"), ("abcdxyz", 7))
        self.assertEqual(longest_unique_substring_advanced("aab"), ("ab", 2))

if __name__ == "__main__":
    unittest.main()
