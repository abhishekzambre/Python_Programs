def isPalindrome(x):
    return True if str(x) == str(x)[::-1] else False


print("123 is palindrome?", isPalindrome(123))
print("1 is palindrome?", isPalindrome(1))
