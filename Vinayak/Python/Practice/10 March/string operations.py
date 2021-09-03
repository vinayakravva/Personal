str1=str(input("Enter any word:"))
print("Select any number from below operations to be performed on entered string\n"
"1. Length of String\n"
"2. Reverse String\n"
"3. Check Palindrome or not\n"
"4. Check Symmetrical or not\n"
"5. Check Permutations and combination\n"
"6. Check two strings are anagram or not\n"
"7. Exit\n")

def lenstr(a):
    print(len(a))
def rvrstr(b):
    print(b[::-1])
def palindrome(c):
    if(c==c[::-1]):
        print(f"{c} is palindrome")
    else:
        print(f"{c} is not a palindrome")
def sym(d):
    j=(len(d)//2)
    if(len(d)%2==0):
        for i in range((len(d))//2):
            if(d[i]==d[j]):
                j+=1
            else:
                print("Not Symmetrical")
    else:
        print("Its not symmetrical")
    if(j==len(d)):
        print("Its Symmetrical")
def percom(e):
    from itertools import permutations
    p=permutations(e)
    d=[]
    for i in list(p):
        if(i not in p):
            d.append(i)
            print("".join(i))
def anagram(f):
    s1=str(input("Enter second word:"))
    if(sorted(f)==sorted(s1)):
        print("The strings are anagrams")
    else:
        print("The strings aren't anagrams")
while(True):
    n=int(input("Enter any number to perform operations on string:"))
    if(n==1):
        lenstr(str1)
    elif(n==2):
        rvrstr(str1)
    elif(n==3):
        palindrome(str1)
    elif(n==4):
        sym(str1)
    elif(n==5):
        percom(str1)
    elif(n==6):
        anagram(str1)
    elif(n==7):
        exit()
    
