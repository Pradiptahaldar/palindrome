# palindrome
#a simple programme to check whether a number is palindrome
num = input("Enter a number: ")

if num == num[::-1]:
    print("Palindrome number")
else:
    print("Not a palindrome number")
'''
num = int(input("Enter a number: "))
original = num   # keep a copy of the original number
rev = 0

while num > 0:
    digit = num % 10         # Get the last digit
    rev = rev * 10 + digit   # Add it to reversed number
    num = num // 10          # Remove the last digit

print("Reversed number:", rev)

# Check if it's a palindrome
if original == rev:
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")
