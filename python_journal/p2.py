def isPalindromeString(str):
    revstr = str[-1::-1]

    if str == revstr:
        return True
    return False

print(isPalindromeString('racecar'))
print(isPalindromeString('anagram'))
