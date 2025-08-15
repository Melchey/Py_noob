"""
Py problem, will involve creating a function that a finds the
palindrome substring in a string,
the input will be a string 's' between 1-1000 characters
the output will be a string, the palindromic substring in inputed string >=1000
if no palindromic substring is found output is ""
"""

def longest_palindromic_substring(s):
    if not s:
        return ""
    
    # initialize the variables to track and start 
    # the length of the longest palindrome
    start = 0
    max_length = 1

    # a helper function to expand around the center
    def expand_around_centre(left, right):
        while left >=0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # return the left and starting index of the palindrome
        return right-left-1, left+1
    
    # go through each possible centre
    for i in range(len(s)):
        # check for odd length palindromes (centre i)
        length1, start1 = expand_around_centre(i, i)
        # check for even length (centre i, i+1)
        length2, start2 = expand_around_centre(i, i+1)

        # Update max_length and start if a longer palindrome is found
        if length1 > max_length:
            max_length = length1
            start = start1
        if length2 > max_length:
            max_length = length2
            start = start2

    # Return the substring from start to start + max_length
    return s[start:start + max_length]

# Test cases
test_cases = ["babad", "cbbd", "racecar", "ahfhghgduudhuigrfjgughcjcjizkghuhgugvvjakkkjfjfhu", ""]
for test in test_cases:
    print(f"Input: {test}")
    print(f"Output: {longest_palindromic_substring(test)}\n")

        
 