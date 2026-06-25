''' 
 Write a function has_unique_chars(s) that checks whether a given string contains all unique characters.

 Do not use Python’s built-in set data structure. Allowed characters: All ASCII characters (a-z, A-Z, 0-9, symbols).
 Example: Input: s = python Output: True'''

# User defined function to check characters
def has_unique_chars(value):
    is_unique = True
    for i in range(0,len(value)):
        for j in range(i+1,len(value)):
            if(value[i]==value[j]):
                is_unique = False
    
    return is_unique
            

# Receive input string from user and convert all characters to lower

name = input("Enter a string : ").lower()

print("String characters are unique!") if has_unique_chars(name)==True else print("String characters are NOT UNIQUE!!!")