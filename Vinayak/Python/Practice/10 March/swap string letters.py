#Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
#Sample String : 'abc', 'xyz'
#Expected Result : 'xyc abz' 
str1=str(input("Enter the first word:"))
str2=str(input("Enter the second word:"))
c=str2[:2]+str1[2:]
d=str1[:2]+str2[2:]
print(c+d)





