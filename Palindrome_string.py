import regex as re
class Solution(object):
    def isPalindrome(self, x):
        x = re.sub(r"[^a-zA-Z0-9]", "", x)
        x=x.lower()
        #print(x)
        if x == x[::-1]:
            return True
        
        return False
    
if __name__ == "__main__":
    # Create an instance of the Solution class
    sol = Solution()

    # Get input from the user
    user_input = input("Enter a string or number to check if it's a palindrome: ")

    # Call the isPalindrome method with the user's input
    result = sol.isPalindrome(user_input)

    # Print the result to the console
    print(result)

