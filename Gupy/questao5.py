def reverseString(s):
    reversed_String = s[::-1]
    return reversed_String

string = input("Enter text: ")
reversed_String = reverseString(string)
print("This is the original text: ", string)
print("This is the reversed text: ", reversed_String)