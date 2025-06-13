num_str = input("Enter a number or a string: ")
def IsPalindrome(num_str):
    last_index = len(num_str) - 1
    line = len(num_str) // 2
    for i in range(0, line):
        if num_str[i] != num_str[last_index - i]:
            return False
    return True
    
#IsPalindrome("racecar")
if IsPalindrome(num_str):
    print("Is Palindrome")
else:
    print("Not Palindrome")
