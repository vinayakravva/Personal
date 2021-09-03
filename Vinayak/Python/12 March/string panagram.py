#Python set to check if string is panagram
from string import ascii_lowercase
def check(s):
    return set(ascii_lowercase)-set(s.lower())==set([])
str1=str(input("Enter the sentence:"))
if(check(str1)==True):
    print("The string is panagram")
else:
    print("The string isn't a pangram")