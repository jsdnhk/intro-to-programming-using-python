#!/usr/bin/python3

def isPalindrome(s):
    return isPalindromeHelper(s, 0, len(s) - 1)

def isPalindromeHelper(s, low, high):
    if high <= low:
        return True
    elif s[low] != s[high]:
        return False
    else:
        return isPalindromeHelper(s, low + 1, high - 1)

"""
def isPalindrome(s):
    if len(s) <= 1: # Base case
        return True
    elif s[0] != s[len(s) - 1]: # Base case
        return False
    else:
        return isPalindrome(s[1 : len(s) - 1])
"""


def main():
    print("Is moon a palindrome?", isPalindrome("moon"))
    print("Is noon a palindrome?", isPalindrome("noon"))
    print("Is a a palindrome?", isPalindrome("a"))
    print("Is aba a palindrome?", isPalindrome("aba"))
    print("Is ab a palindrome?", isPalindrome("ab"))
    print("Is 猜一猜 a palindrome?", isPalindrome("猜一猜"))

main() # Call the main function
