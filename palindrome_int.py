class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x=str(x)
        if x == x[::-1]: 
            return True
        return False


if __name__ == "__main__":
    # Create an instance of the Solution class
    sol = Solution()

    # Get input from the user
    user_input = input("Enter a number to check if it's a palindrome: ")

    # Call the isPalindrome method with the user's input
    result = sol.isPalindrome(user_input)

    # Print the result to the console
    print(result)

