#Python program create function to check if a string is palindrome or not

def pal():
    var=str(input("Enter any word to check:"))
    var1=var[::-1]
    if(var1==var):
        print(f"{var} is a palindrome")
    else:
        print("Its not an palindrome")
pal()