#Remove items from Set until set not become empty set
thisset={"banana","cherry","apple","apple"}
for x in range(len(thisset)):
    thisset.pop()
print(thisset)