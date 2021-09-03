# Program to input any alphabets and check it is vowel or consonent
vowels=["a","e","i","o","u"]
var = str(input("Enter the Alphabet :"))
for num in vowels:
    if(var==str(num)):
        print("Its a Vowel")
        break
    else:
        print("Consonant")
        break


