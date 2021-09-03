#Program to print anagrams together in Python using List and Dictionary
arr=['cat','dog','tac','god','act']
dict={}
for i in arr:
    key=''.join(sorted(i))
    if key in dict.keys():
        dict[key].append(i)
    else:
        dict[key]=[]
        dict[key].append(i)
output=""
for key,value in dict.items():
    output=output+' '.join(value)+" "
print(output)

