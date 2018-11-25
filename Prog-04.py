def reverse(s): 
    s[::-1]
    if s==s[::-1]:
        print("Given string is a palindrome.")
    else:
        print("Given string is not a palindrome.")


inp= input("Enter string: ")
print(reverse(inp))
